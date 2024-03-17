## OCT이미지 데이터 기반 시력 예측 연구(KSC 2022)
### 📌 논문
- **Abstract**
  
시력 검사는 안과 방문 시 기본적으로 수행하는 검사 중 하나로, 특정 거리에서 Snellen 차트 또는 ETDRS 차트를 이용하여 시력을 측정한다. 수검자가 자신의 특정 목적을 이루고자 전통적인 시력 차트의 허점을 이용하여, 고의로 시력을 높이거나 낮추는 답변을 하거나, 수검자의 의식이 불명한 경우 답변이 불가능할 수 있다. 이러한 문제점을 해결하고자 본 논문에서는 망막질환의 진단 및 경과 관찰에 유용하게 이용되는 OCT(Optical Coherence Tomography) 이미지와 ViT(Vision Transformer) 모델을 활용하여 4개의 시력 레벨로 나누어진 데이터 셋에 대하여 시력 예측 모델을 제공한다. 본 연구에서는 테스트에 사용된 17,139개의 테스트 셋에 대하여 90%의 정확도를 보였다. 본 논문은 이전 Fundus 이미지를 사용한 시력 측정의 연장선에서 보다 많은 데이터를 가지고 효과적으로 시력 측정이 가능함을 보인다. 

### 📆 논문 게재
  - 2023/02/02
---

### 데이터 전처리
- **데이터 구성** :  `OCT 이미지` `시력 차트 테이블`
  - **OCT Image**
    <p align="center">  
    <img src="https://github.com/ssh6lq/Development-of-AI-based-technology-for-diagnosis-and-treatment-of-ophthalmic-diseases/assets/154342847/a0a56ce1-611a-443f-84f2-7a7a9f849535.png" align="center" width="50%">  
    </p>
  - **시력 차트 테이블**
    - | Record key | Patient number | Name | Gender | Birth date | Writer | Date | Objective | Accessment | R)UCVA | R)CVA | R)BCVA | L)UCVA | L)CVA | L)BCVA |
      |------------|----------------|------|--------|------------|--------|------|-----------|------------|--------|-------|--------|--------|-------|--------|
---
  - **데이터 셋**
    -   | class1(0.0~0.05) | class2(0.1~0.2) | class3(0.3~0.7) | class4(0.8~1.0) | total  |
        |------------------|-----------------|-----------------|-----------------|--------|
        |      20,100      |      22,576     |      21,450     |      21,568     | 85,694 |

### 모델
<p align="center">  
    <img src="https://github.com/ssh6lq/Development-of-AI-based-technology-for-diagnosis-and-treatment-of-ophthalmic-diseases/assets/154342847/e0b5f190-2d63-460b-a3ae-57cfb6471b8b.png" align="center" width="70%">  
    </p>

- `ViT(Vision Transformer)`
---
### ⚙️ 개발환경
- `Python`
- **Framework** : `pytorch` 
  
---

### ✔️ 역할
#### **팀원:** 3명







