import cv2
import os
from natsort import natsorted  # 설치 필요: pip install natsort

# 이미지가 저장된 폴더 경로
image_folder = "/home/soyun/bee/images_to_detect/0619"  # 이미지 폴더 경로
output_video_path = "output_video.mp4"  # 결과 영상 저장 이름
fps = 24  # 초당 프레임 수

# 이미지 파일 목록 가져오기
images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
images = natsorted(images)  # 자연 정렬

# 첫 번째 이미지로 크기 확인
first_image = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = first_image.shape

# 비디오 작성자 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# 이미지들을 하나씩 비디오에 작성
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video_writer.write(frame)

video_writer.release()
print("🎬 영상 저장 완료:", output_video_path)
