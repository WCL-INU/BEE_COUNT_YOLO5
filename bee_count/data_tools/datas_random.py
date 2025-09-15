import os, shutil, random
from pathlib import Path
import yaml

# 베이스 경로
base = Path("/home/soyun/bee")
dataset_dirs = [base / "dataset_ready/0203", base / "dataset_ready/0619"]

# 결과 저장 경로
image_dir_train = base / "dataset/dataset2/images/train"
image_dir_val = base / "dataset/dataset2/images/val"
label_dir_train = base / "dataset/dataset2/labels/train"
label_dir_val = base / "dataset/dataset2/labels/val"

# 폴더가 없으면 생성
for d in [image_dir_train, image_dir_val, label_dir_train, label_dir_val]:
    os.makedirs(d, exist_ok=True)

# 모든 이미지 경로 수집
all_image_paths = []
for d in dataset_dirs:
    img_dir = d / "images"
    all_image_paths += [img_dir / f for f in os.listdir(img_dir) if f.endswith(".jpg")]

# 섞고 분할
random.shuffle(all_image_paths)
split = int(0.8 * len(all_image_paths))
train_images = all_image_paths[:split]
val_images = all_image_paths[split:]

# 복사 함수
def copy_data(image_paths, img_dst, lbl_dst):
    for img_path in image_paths:
        label_path = img_path.parent.parent / "labels" / img_path.with_suffix('.txt').name

        shutil.copy(img_path, img_dst / img_path.name)

        if label_path.exists():
            shutil.copy(label_path, lbl_dst / label_path.name)
        else:
            open(lbl_dst / label_path.name, "w").close()

# 실행
copy_data(train_images, image_dir_train, label_dir_train)
copy_data(val_images, image_dir_val, label_dir_val)

print("✅ 데이터셋 병합 및 분할 완료!")

# 마지막에 data.yaml 생성
data_yaml = {
    'train': str(image_dir_train.resolve()),
    'val': str(image_dir_val.resolve()),
    'nc': 1,
    'names': ['bee']
}

with open(base / 'dataset/dataset2/data.yaml', 'w') as f:
    yaml.dump(data_yaml, f)

print("📄 data.yaml 생성 완료!")
