import streamlit as st
import webbrowser

st.title("📝도배하자 with 챗봇")
st.markdown(
    "<p style='color:gray; font-size:20px; font-family:Arial;'>어서오세요 고객님! 도배하자 챗봇 서비스 '딥봇'입니다.</p>",
    unsafe_allow_html=True
)

# 1단계: 서비스 종류 선택
service_type = st.selectbox(
    "👀 원하는 서비스 종류를 선택하세요:",
    ["도배 견적 확인하기", "챗봇 상담하기"]
)

# 2단계: 각 서비스에 따른 옵션 선택
if service_type == "챗봇 상담하기":
    option = st.radio("상담 방식을 선택하세요:", ["음성으로 대화하며 상담", "글자로 채팅하며 상담"])

    # 챗봇 상담 시작 버튼
    if st.button("챗봇 상담 시작"):
        chat_link = ''
        if option == "음성으로 대화하며 상담":
            chat_link = 'http://localhost:8501/'  # 음성 챗봇 상담 링크
        elif option == "글자로 채팅하며 상담":
            chat_link = 'http://localhost:8502/'  # 글자 챗봇 상담 링크

        # 새 웹페이지 주소 설정
        webbrowser.open_new_tab(chat_link)

elif service_type == "도배 견적 확인하기":
    st.markdown(
        "<p style='color:dark gray; font-size:18px; font-family:Arial;'>세부사항을 입력하세요</p>",
        unsafe_allow_html=True
    )

    with st.form(key='wallpaper_form'):
        wall_type = st.radio(
            "시공할 벽지를 선택하세요",
            ('합지', '실크', '합지+실크'),
            index=0
        )
        quality = st.radio(
            "벽지 브랜드는 어떤걸 사용하나요?",
            ('프리미엄', '일반', '무관'),
            index=1
        )
        area = st.selectbox(
            "시공할 공간의 평수가 어떻게 됩니까?",
            ('66m² (20평대)', '82m² (30평대)', '99m² (40평대)'),
            index=2
        )
        wallpaper_type = st.radio(
            "천장 포함여부를 선택하세요",
            ('천장포함', '부분포함', '미포함'),
            index=1
        )
        submit_button = st.form_submit_button(label='견적 확인')

    if submit_button:
        st.success(f'{wall_type} 소재의 {quality} 벽지로 {area} 크기에 {wallpaper_type}을(를) 시공하는 견적을 계산합니다.')
        # 여기에 견적 계산 로직을 추가하세요.
        # calculated_cost = calculate_cost(room_type, quality, area, wallpaper_type)
        # st.write(f"예상 견적은 {calculated_cost}원 입니다.")
        st.write(f"예상 견적은 {35}원 입니다.")
