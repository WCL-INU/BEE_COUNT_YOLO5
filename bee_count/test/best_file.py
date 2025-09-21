import cv2
import torch
from pathlib import Path

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/soyun/BEE_COUNT_YOLO5/bee_count/runs/train/bee_detect_light2/weights/best.pt', force_reload=True)
img_path = '/home/soyun/BEE_COUNT_YOLO5/bee_count/bee_data/original_input/device105.jpg'
img = cv2.imread(img_path)

results = model(img_path)
df = results.pandas().xyxy[0]
bee_count = len(df)

# Draw boxes
for i in range(len(df)):
    x1, y1, x2, y2 = map(int, df.loc[i, ['xmin', 'ymin', 'xmax', 'ymax']])
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Draw count
cv2.putText(img, f'Bees: {bee_count}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

# 출력 폴더 준비
output_dir = Path('/home/soyun/BEE_COUNT_YOLO5/bee_count/bee_data/original_output')
output_dir.mkdir(parents=True, exist_ok=True)

# 출력 파일명 (원본이름 + _output.jpg)
orig_name = Path(img_path).stem   # ex1
output_path = output_dir / f"{orig_name}_output.jpg"

# 저장
cv2.imwrite(str(output_path), img)
print(f"✅ 결과 저장 완료: {output_path}")
