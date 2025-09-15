import torch
import cv2
import os
from pathlib import Path

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/bee_detect_light2/weights/best.pt', force_reload=True)
model.conf = 0.3  # 이 아래 confidence는 무시

# 이미지 폴더 경로
img_folder = Path('~/bee/test_images_to_detect/0619').expanduser()
output_folder = Path('~/bee/output_detected/light2_0619').expanduser()
output_folder.mkdir(parents=True, exist_ok=True)

# 이미지별 카운트 저장용
results_log = []

for img_path in sorted(img_folder.glob('*.png')): # png인지 jpg인지 확인하기기
    img = cv2.imread(str(img_path))
    results = model(str(img_path))
    df = results.pandas().xyxy[0]

    # confidence > 0.3 필터링
    df = df[df['confidence'] > 0.3]

    count = len(df)

    # Bounding box 그리기
    for i in range(count):
        x1, y1, x2, y2 = map(int, df.iloc[i][['xmin', 'ymin', 'xmax', 'ymax']])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 카운트 텍스트 표시
    cv2.putText(img, f'Bees: {count}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    # 저장
    output_path = output_folder / f'{img_path.stem}_counted.png' # png인지 jpg인지 확인하기기
    cv2.imwrite(str(output_path), img)

    # 기록
    results_log.append((img_path.name, count))

# CSV로 저장
import pandas as pd
pd.DataFrame(results_log, columns=['image', 'count']).to_csv(output_folder / 'counts.csv', index=False)
print("✅ 완료! 결과 저장 폴더:", output_folder)
