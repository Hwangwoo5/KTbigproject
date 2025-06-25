# 🐟 Kaquarium - Aquarium Fish Mortality Detection 실행 코드

# -------------------------------
# 🔧 환경 설정 및 패키지 설치
# -------------------------------

# YOLOv8 설치
# pip install ultralytics

# TensorFlow 설치 (선택적, 학습 환경 구성 시 사용 가능)
# pip install tensorflow
# pip install tensorflow-gpu

# PyTorch 설치 (YOLO 학습에 필요)
# pip install torch torchvision torchaudio

# -------------------------------
# 📦 라이브러리 임포트
# -------------------------------

from ultralytics import YOLO, settings
import cv2
import yaml
import torch

# -------------------------------
# ⚙️ YOLO 학습 설정용 YAML 생성
# -------------------------------

data = dict(
    train='C:/Users/User/bigpro_modeling/data2/train/images/',
    val='C:/Users/User/bigpro_modeling/data2/valid/images/',
    nc=2,
    names=['Dead', 'Alive']
)

# ./data.yaml 파일로 저장
with open('./data.yaml', 'w') as f:
    yaml.dump(data, f)

# -------------------------------
# 📁 YOLO 환경 설정 경로 지정
# -------------------------------

settings['datasets_dir'] = './data2'

# -------------------------------
# 🏋️ YOLOv8 모델 학습
# -------------------------------

# 모델 로드 (사전 학습된 yolov8n 사용)
model = YOLO('./yolov8n.pt')

# 학습 실행
model.train(
    model='./yolov8n.pt',
    data='./data.yaml',
    epochs=100  # 학습 epoch 수 (예: 100회)
)

# -------------------------------
# 🎥 학습된 모델로 영상 감지 실행
# -------------------------------

# 학습된 best.pt 모델 로드
model = YOLO('./runs/detect/train5/weights/best.pt')  # train 폴더 경로에 맞게 수정 필요

# 테스트용 영상 경로
video_path = './butterfly_fish_dead_video.mp4'
cap = cv2.VideoCapture(video_path)

# 디스플레이 창 설정
cv2.namedWindow("YOLOv8 Inference", cv2.WINDOW_NORMAL)
cv2.resizeWindow("YOLOv8 Inference", 1000, 800)

# 영상 프레임 반복 처리
while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame)  # YOLO 추론
        annotated_frame = results[0].plot()  # 결과 시각화
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
