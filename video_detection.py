import torch
import cv2
import os

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/bee_detect_light/weights/best.pt', force_reload=True)
model.conf = 0.3  # confidence threshold

# 비디오 로드
video_path = '/home/soyun/bee/output_video.mp4'
cap = cv2.VideoCapture(video_path)

# 저장용 비디오 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOv5 모델 추론
    results = model(frame)
    df = results.pandas().xyxy[0]

    # confidence > 0.3 필터링
    df = df[df['confidence'] > 0.3]
    count = len(df)

    # Bounding box 그리기
    for i in range(count):
        x1, y1, x2, y2 = map(int, df.iloc[i][['xmin', 'ymin', 'xmax', 'ymax']])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 카운트 텍스트 표시
    cv2.putText(frame, f'Bees: {count}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    # 첫 프레임에서 출력 영상 초기화
    if out is None:
        h, w = frame.shape[:2]
        out = cv2.VideoWriter('/home/soyun/bee/output_detected/video_0619/detected_video.mp4', fourcc, 24, (w, h))

    out.write(frame)

cap.release()
out.release()
print("🎬 처리 완료! 'detected_video.mp4' 저장됨")
