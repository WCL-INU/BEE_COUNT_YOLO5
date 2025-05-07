import cv2
import torch
from pathlib import Path

model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/bee_detect_light/weights/best.pt')
img_path = 'path/to/image.jpg'
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

cv2.imwrite('output_with_count.jpg', img)
