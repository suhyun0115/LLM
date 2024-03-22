# ✒️ NLP, LLM project</br>AI 대화형 Chatbot 모델 개발
## 👥 Team
- Team name : DBDBDeep
- Team members : 김유진, 이수현, 조서현
- * :clock1:시작일 : 2024.02.26(월)
  * ⏰목표일 : 2024.03.15(금)
## :books: skill
- **Programming** <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
- **Framework** <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"> <img src="https://img.shields.io/badge/flask-412991?style=for-the-badge&logo=flask&logoColor=white">
- **Tools** <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/pycharm-000000?style=for-the-badge&logo=pycharm&logoColor=white"> <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"> <img src="https://img.shields.io/badge/powerbi-E97627?style=for-the-badge&logo=powerbi&logoColor=white">
- **Git** <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

## 목차(INDEX)
&emsp;&ensp;Ⅰ. 주제 선정</br>&emsp;&ensp;Ⅱ. Data preprocessing</br>&emsp;&ensp;Ⅲ. Modeling</br>&emsp;&ensp;Ⅳ. Chatbot 구현</br>&emsp;&ensp;Ⅴ. 프로젝트 결과</br>&emsp;&ensp;</br>&emsp;&ensp;

## Ⅰ. 주제선정
  **1. 대화형 AI Chatbot 서비스 구현**</br>
       &nbsp;&nbsp;&nbsp; 1) 관련된 다양한 질문과 상황을 제공함으로써 정확하고 신속한 응답을 제공하는게 목표</br>
       &nbsp;&nbsp;&nbsp; 2) 고객의 문의에 신속, 정확하게 답변할 수 있는 시스템 구축</br>
       ![스크린샷 2024-03-22 125456](https://github.com/suhyun0115/LLM/assets/151902283/6f50a8b7-132f-4ecc-834e-47bd3a89f2a7)

       
  **2. 자료출처**</br>
       &nbsp;&nbsp;&nbsp; Dacon https://dacon.io/competitions/official/236216/overview/description/

## Ⅱ. Data preprocessing & Modeling
**1. 데이터 전처리**</br>
       &nbsp;&nbsp;&nbsp; 1) DataFrame 변경 (id, category 삭제)</br>
       &nbsp;&nbsp;&nbsp; 2) Dataset 증강 (기존 카테고리를 제외하고 다른 카테고리 질문을 추가)</br>
       &nbsp;&nbsp;&nbsp; 3) Tokenizer</br>
       
**2. 모델 학습**</br>
       &nbsp;&nbsp;&nbsp; 1) skt, kykim, kakao : Fine-tuning</br>
       &nbsp;&nbsp;&nbsp; 2) edentns, LDCC : QLoRA</br>
       &nbsp;&nbsp;&nbsp; 3) RAG</br>

  - 최종 모델 SKT 사용

## Ⅲ. Chatbot 구현
**1. 챗봇 서비스**</br>
       &nbsp;&nbsp;&nbsp; 1) Streamlit 사용</br>
       &nbsp;&nbsp;&nbsp; 2) speech_recognition 모듈 사용으로 대화형 챗봇 서비스 구현</br>
       &nbsp;&nbsp;&nbsp; 3) 웹 배포</br>








