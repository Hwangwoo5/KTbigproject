# 🐟 Kaquarium - Aquarium Fish Mortality Detection

YOLOv8 기반 객체 인식 기술을 활용하여  
아쿠아리움 내 폐사한 어류를 실시간 감지하는 솔루션입니다.

어류 폐사는 연쇄 폐사의 주요 원인 중 하나이며,  
빠른 탐지와 대응을 통해 관람객 만족도 향상 및 수조 생태 안정화에 기여합니다.

---

## 🔍 주요 기능

- YOLOv8을 활용한 어류 폐사 인식
- 실시간 bounding box 시각화 (OpenCV)
- 폐사 발생 시 관리자에게 즉시 대응 가능하도록 데이터화 가능

---

## 🧰 사용 기술

- Python 3.8+
- [ultralytics](https://github.com/ultralytics/ultralytics) YOLOv8
- OpenCV
- NumPy

---

## ▶️ 실행 방법

```bash
git clone https://github.com/your-id/Kaquarium-FishMortality-Detection.git
cd Kaquarium-FishMortality-Detection
pip install -r requirements.txt
python object_tracking_fish.py
```

> `fish.mp4`, `best.pt` 파일이 실행 디렉토리에 존재해야 합니다.

---

## 🧠 프로젝트 정보

- 📆 개발 기간: 2024년 4월 ~ 2024년 5월
- 📌 기여도: 100% (데이터 수집, 모델 학습, 코드 작성, 시각화)
- 🎯 목적: 실시간 어류 폐사 탐지 → 연쇄 폐사 방지 → 운영 효율 및 관람 만족도 향상

---

## 🖼️ 시연 예시

> 폐사 개체가 감지되면 실시간으로 bounding box를 통해 구분  
> 추가적으로 관리자 페이지나 IoT 연동도 가능하도록 확장 가능

---

## 📄 라이선스

MIT License
