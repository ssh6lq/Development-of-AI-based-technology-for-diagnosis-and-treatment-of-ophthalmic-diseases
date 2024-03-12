## 안저이미지(Fundus imag)데이터 기반 시력 예측 연구
### 📌 논문
- **Abstract**
  
본 논문은 안과 질환에서 가장 손쉽게 그리고 다양한 방법으로 얻을 수 있는 fundus photography를 활용하여, 머신러닝 기법으로 통해서 개발한 AI를 통한 시력 측정 기법을 제공한다. 본 논문에서는 Decimal 시력의 0.0부터 1.0까지 11단계를 4단계로 단순화하여 구분하고, AI를 통한 시력 측정 결과를 도출한다. 본 논문에서는 각 단계의 데이터 편차 및 수집 가능한 데이터의 한계로, 한 가지 기계학습이 아닌 3가지 기계학습 기법을 기반으로 한 앙상블 기법을 제안한다. 본 논문에서는 전체 시스템에 대한 대한 85%의 정확성을 보인다. 본 논문은 우리가 아는 한 fundus 이미지 기반 최초  VA 측정에 관한 논문이다.

---

### 📆 논문 일자
2022.03.11

---
#### 데이터 전처리
- **데이터 구성** : `안저이미지(Fundus image)` `OCT 이미지` `환자정보 CSV 데이터`
  - **안저이미지(Fundus image)**
    <p align="center">  
    <img src="https://github.com/ssh6lq/Development-of-AI-based-technology-for-diagnosis-and-treatment-of-ophthalmic-diseases/assets/154342847/630f0c1f-dfcf-4aa4-8715-c61af3fc3067.png" align="center" width="50%">  
  - **환자 정보 관리 차트**
    - 기존 테이블
      -  | Record key | Patient number | Name | Gender | Birth date | Writer | Date | Objective | Accessment |
         |------------|----------------|------|--------|------------|--------|------|-----------|------------|
       
    - 시력 변수 추가 테이블
      - | Record key | Patient number | Name | Gender | Birth date | Writer | Date | Objective | Accessment | R)UCVA | R)CVA | R)BCVA | L)UCVA | L)CVA | L)BCVA |
        |------------|----------------|------|--------|------------|--------|------|-----------|------------|--------|-------|--------|--------|-------|--------|

- **데이터 셋**
  - 이미지와 테이블 매칭한 시력 데이터 셋 생성   
    



---
### 모델 아키텍처

<p align="center"> 
<img src="https://github.com/ssh6lq/Development-of-AI-based-technology-for-diagnosis-and-treatment-of-ophthalmic-diseases/assets/154342847/659c37db-dbab-41a9-a4eb-30eb9a3ec4c4.png" align="center" >

- **Model** : `VGG19` `Effieint-B7` `SVM` 
---
### ⚙️ 개발환경
- `Python`
- **Framework** : `tensorflow` `pytorch` `keras` `scikit-learn`
  
---

### ✔️ 역할
- **팀원** : 4명












