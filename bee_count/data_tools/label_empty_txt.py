import os

# 경로 설정
image_dir = "/mnt/c/Users/asx12/OneDrive/사진/bee_images/images"
label_dir = "/mnt/c/Users/asx12/Downloads/second_project/all_data"

# 이미지 파일들에서 확장자 제거하고 파일명 추출
image_names = [os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith((".jpg", ".jpeg", ".png"))]

# 각 이미지 이름을 기준으로 라벨 파일 존재 확인
for name in image_names:
    label_filename = f"{name}_label.txt"
    label_path = os.path.join(label_dir, label_filename)

    if not os.path.exists(label_path):
        # 없으면 빈 텍스트 파일 생성
        with open(label_path, "w") as f:
            pass
        print(f"[생성됨] {label_filename}")
    else:
        print(f"[존재함] {label_filename}")
