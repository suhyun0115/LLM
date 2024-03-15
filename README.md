# ✒️ NLP project</br>AI copywriting service using product review sentiment analysis and keyword extraction
## 👥 Team
- Team name : ⚔️
- Team members : 
- * :clock1:시작일 : 2024.02.26(월)
  * ⏰목표일 : 2024.03.15(금)
## :books: skill
- **Programming** <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
- **Framework** <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"> <img src="https://img.shields.io/badge/flask-412991?style=for-the-badge&logo=flask&logoColor=white">
- **Tools** <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/pycharm-000000?style=for-the-badge&logo=pycharm&logoColor=white"> <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"> <img src="https://img.shields.io/badge/powerbi-E97627?style=for-the-badge&logo=powerbi&logoColor=white">
- **Git** <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

## 목차(INDEX)
&emsp;&ensp;Ⅰ. 주제 선정</br>&emsp;&ensp;Ⅱ. 목표 설정</br>&emsp;&ensp;Ⅲ. 프로젝트 순서도</br>&emsp;&ensp;Ⅳ. 모델 선정</br>&emsp;&ensp;Ⅴ. 데이터 전처리</br>&emsp;&ensp;Ⅵ. 모델링</br>&emsp;&ensp;Ⅶ. 키워드 추출</br>&emsp;&ensp;Ⅷ. 서비스 구현</br>&emsp;&ensp;Ⅸ. 프로젝트 결과</br>&emsp;&ensp;

## Ⅰ. 주제선정
  **1. 대화형 AI Chatbot 서비스 구현**</br>
       &nbsp;&nbsp;&nbsp; 1) 관련된 다양한 질문과 상황을 제공함으로써 정확하고 신속한 응답을 제공하는게 목표</br>
       &nbsp;&nbsp;&nbsp; 2) 고객의 문의에 신속, 정확하게 답변할 수 있는 시스템 구축</br>
       
  **2. 자료출처**</br>
       &nbsp;&nbsp;&nbsp; Dacon https://dacon.io/competitions/official/236216/overview/description/

## Ⅱ. 목표설정
**1. 리뷰 감정분석**</br>
       &nbsp;&nbsp;&nbsp; 1) KoBERT 모델을 Fine-tuning</br>
       &nbsp;&nbsp;&nbsp; 2) 감정분석 후 긍정, 중립, 부정으로 분류</br>
       &nbsp;&nbsp;&nbsp; 3) 긍정 리뷰 데이터만 사용</br>
       
**2. 핵심 키워드 추출**</br>
       &nbsp;&nbsp;&nbsp; 1) KeyBERT와 Kiwi 형태소분석기 사용해 핵심 키워드 추출 </br>
       &nbsp;&nbsp;&nbsp; 2) 긍정 리뷰 데이터에서 핵심 키워드 3개 추출</br>
       
**3. 카피라이팅 서비스**</br>
       &nbsp;&nbsp;&nbsp; 1) OpenAI API를 사용</br>
       &nbsp;&nbsp;&nbsp; 2) 긍정 리뷰 데이터 csv파일을 업로드하면 핵심 키워드 3개를 추출해주는 서비스 구현</br>
       &nbsp;&nbsp;&nbsp; 3) 추출한 핵심 키워드 3개와 광고할 제품의 이름, 설명을 조합해 카피라이팅을 해주는 서비스 구현</br>

## Ⅲ. 프로젝트 순서도
