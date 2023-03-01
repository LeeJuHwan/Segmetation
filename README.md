# 의료진을 위한 알약 검색 서비스
<img width="1108" alt="image" src="https://user-images.githubusercontent.com/118493627/219282644-842dc209-aa75-4e16-a7b7-2d4a16381483.png">

## Service Video
- [유튜브 링크](https://youtu.be/U7irzA0zeKs)

## Team
<img width="1127" alt="image" src="https://user-images.githubusercontent.com/118493627/221560665-251929a9-968c-4f1f-97dc-504e2f321a2d.png">

### Background
- 의료진의 약 식별 업무 의뢰율이 굉장히 높은 77% 이상에 달하는 통계치를 확인 했습니다. 그렇다면, 왜 **약 식별 업무**가 현재 의료업계에 어려움을 내비추고 있을까요?

- 약의 색상, 모양, 식별자 등을 판단 하여 직접 체크 또는 입력 하여 약을 검색 하는 것이 아닌, **실제 촬영** 또는 **이미지**를 기반으로 생산적인 작업을 딥러닝 모델이 대신 하여 생산성을 높히는 개발 방향을 선정 하였고, 웹 형태의 구조를 모바일에서 쉽게 이용 할 수 있도록 설계 하였습니다.

### Environment
||Library|
|------|---|
|**WAS**|Python 3.8 + **Django** 4.1.6  
|**WS**|**Nginx** + **Gunicorn**
|**Deep learning**|**torch** 1.7.1 && torchvision 0.8.2 <br> **tensorflow** 2.7.1 && **keras** 2.7.0 && **keras-ocr** 0.9.2 <br> **opencv** 4.5.1.48 <br> **Yolo** v7
|**Deploy**|**AWS EC2**
|**Database**|**PostgreSQL** with psycopg2-binary 2.9.5

### Dataset
<img width="1127" alt="image" src="https://user-images.githubusercontent.com/118493627/221569388-7639e690-dac4-4c9f-b00f-2c1d0b8ddbf9.png">

<img width="1732" alt="image" src="https://user-images.githubusercontent.com/118493627/221569530-0369063d-be1a-438d-a409-35b25d6a179d.png">

<img width="1728" alt="image" src="https://user-images.githubusercontent.com/118493627/221569616-adbf0a4c-6d44-49af-bdcd-96b2e9dd5fa3.png">

- [DUR 성분 정보](https://www.data.go.kr/iim/api/selectAPIAcountView.do)
- [알약 낱알 식별정보](https://www.data.go.kr/data/15057639/openapi.do)
- [용법 정보](https://www.data.go.kr/iim/api/selectAPIAcountView.do)

<img width="921" alt="image" src="https://user-images.githubusercontent.com/118493627/221570302-b9923dc4-060a-462c-9afa-d3350d25fd21.png">

- [kaggle](https://www.kaggle.com/)
- [roboflow](https://roboflow.com/)

### Used Class
<img width="993" alt="image" src="https://user-images.githubusercontent.com/118493627/221570631-fe85c7e7-1064-45b1-8102-d5e9d2989a2b.png">

- 클래스 중, 식별 문자의 한글 데이터는 전체 데이터셋에 5%정도 존재 하였고 실제 OCR 기법을 이용 했을 때 문자가 인식되지 못한 점에서 제외하였다.

### Process
<img width="1200" alt="image" src="https://user-images.githubusercontent.com/118493627/221573628-8da040a9-5de1-4bb5-b08f-f5b852a4d252.png">

1. Object detection with **Yolo v7**
2. Shape Classification with **CNN**
3. extract color algorithm with **OpenCV**
4. Image Similarity algorithm with **Metric learning**

### Model Accuracy
<img width="1051" alt="image" src="https://user-images.githubusercontent.com/118493627/221576915-c7082994-aa23-44bb-9e60-71e60a3a2229.png">

### System Architecture
<img width="1145" alt="image" src="https://user-images.githubusercontent.com/118493627/221577179-5029eec8-fc1b-4028-8c7b-eb79839f1795.png">

### before Deep learning - dockerizing
![제목 없는 디자인](https://user-images.githubusercontent.com/118493627/217997039-a107f29e-51a3-4b30-b541-89624af58095.png)
- [dockerizing](https://github.com/LeeJuHwan/dockerizing)
- GPU 환경 구성 전 사용 된 도커로 개발 환경 셋팅
