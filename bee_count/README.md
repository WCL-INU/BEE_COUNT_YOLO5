# 🐝 Bee Counting with YOLOv5/YOLOv8

## 📌 프로젝트 개요
- **목표**: YOLOv5/YOLOv8을 활용하여 꿀벌을 탐지하고 개체 수를 정확하게 계수하는 모델 개발  
- **연구 배경**: 양봉 산업에서 벌 개체 수 모니터링은 꿀벌 건강 상태와 생산성 파악에 핵심적임  
- **주요 기여**: 데이터셋 구축부터 모델 학습 및 평가까지 엔드투엔드 파이프라인 개발

![벌 이미지](results/bee_count.png)

---

## 👩‍💻 역할
- 데이터셋 제작 및 모델 학습 담당  
- YOLO 학습/검증 파이프라인 구축 및 파라미터 튜닝  

---

## 📂 데이터셋 구축
- **Labeling 도구**: [LabelImg](https://github.com/heartexlabs/labelImg) 사용  
- **작업량**: 수천 장 단위의 프레임에 대해 벌 개체 수 라벨링 진행  
- **라벨 포맷 변환**: Pascal VOC → YOLO 포맷(.txt) 변환  
- **디렉토리 구조**

- **특이사항**: 벌이 없는 프레임에도 **빈 라벨 파일(.txt)** 생성 → False Positive 최소화  

---

## ⚙️ 학습/검증 파이프라인
- **환경 세팅**
- Python, PyTorch, CUDA 환경 구성
- 가상환경(`yoloenv`) 관리
- **학습 코드 실행**
```bash
python train.py --img 640 --batch 16 --epochs 100 \
                --data data.yaml --weights yolov5s.pt \
                --name bee_count_exp

```

## 📈 평가 및 개선 과정
- 학습 결과 **mAP / Precision / Recall** 지표 분석  
- False detection 발생 시 **추가 이미지 라벨링 & 재학습**  
- 다양한 **날씨 / 조명 조건**의 프레임을 수집하여 데이터셋 보강  

---

## 🔑 기술 스택
- **Frameworks**: YOLOv5, PyTorch  
- **Tools**: LabelImg, Python 가상환경 관리  
- **Dataset Management**: Custom dataset split (train/val), YOLO format 관리  

---

## 📊 실험 결과
- **YOLOv5s 기준**: 높은 Precision 확보  
- Recall 개선을 위해 **반복적인 데이터 증강 및 재학습** 진행  

