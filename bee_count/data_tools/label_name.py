import os
from pathlib import Path

# 경로 설정
image_dir = Path("/home/soyun/bee/dataset_ready/0619/images")
label_dir = Path("/home/soyun/bee/dataset_ready/0619/labels")

# 이미지와 라벨 쌍 리네이밍
images = sorted([f for f in os.listdir(image_dir) if f.endswith(".jpg")])
labels = sorted([f for f in os.listdir(label_dir) if f.endswith(".txt")])

count = 1
for img_file, lbl_file in zip(images, labels):
    new_id = f"{count:03d}"  # 0001, 0002, ...

    new_img_name = f"image_{new_id}.jpg"
    new_lbl_name = f"image_{new_id}.txt"
    os.rename(image_dir / img_file, image_dir / new_img_name)
    os.rename(label_dir / lbl_file, label_dir / new_lbl_name)

    print(f"✅ {img_file} → {new_img_name}")
    print(f"✅ {lbl_file} → {new_lbl_name}")

    count += 1
