import streamlit as st
import requests
from gtts import gTTS
from streamlit_chat import message
from datetime import datetime
import os
import pygame
import speech_recognition as sr
from pydub import AudioSegment

st.title("📝도배하자 with 챗봇")
st.markdown(
    "<p style='color:gray; font-size:20px; font-family:Arial;'>어서오세요 고객님! 음성 인식 챗봇 '딥봇'입니다.</p>",
    unsafe_allow_html=True
)

# 이전 대화 기록을 저장하는 세션 상태 변수
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []


def record_audio(filename):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.text("음성 채팅 시작 버튼을 누른 후 말씀해 주세요")
        try:
            audio_data = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            st.text("5초 동안 아무런 소리도 감지되지 않았습니다. 채팅을 종료하시겠습니까?")
            return False
        with open(filename, "wb") as f:
            f.write(audio_data.get_wav_data(convert_rate=16000))
    return True


def convert_wav_to_mp3(wav_filename, mp3_filename):
    sound = AudioSegment.from_wav(wav_filename)
    sound.export(mp3_filename, format="mp3")


def process_audio_input(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        user_input = r.recognize_google(audio_data, language="ko-KR")
    return user_input


if st.button("음성 채팅 시작 🔊"):
    for file in os.listdir():
        if file.endswith(".mp3") and file.startswith("recorded_audio"):
            os.remove(file)

    wav_filename = f"recorded_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
    mp3_filename = f"recorded_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"

    if record_audio(wav_filename):
        convert_wav_to_mp3(wav_filename, mp3_filename)
        user_input = process_audio_input(wav_filename)

        st.session_state.conversation_history.append(('user', user_input))
    # Flask 서버로 요청 전송
        response = requests.post("http://localhost:5000/predict", json={"user_text": user_input})
        if response.status_code == 200:
            data = response.json()
            chatbot_response = data['chatbot_response']
            st.session_state.conversation_history.append(('chatbot', chatbot_response))

            for i, (role, text) in enumerate(st.session_state.conversation_history):
                if role == 'user':
                    message(text, is_user=True, key=f"user_{i}")
                else:
                    message(text, key=f"chatbot_{i}")
                    file_name = f"chatbot_response_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
                    tts = gTTS(text=text, lang="ko")
                    tts.save(file_name)

                    if i == len(st.session_state.conversation_history) - 1:
                        pygame.init()
                        pygame.mixer.music.load(file_name)
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(10)
        else:
            st.text("오류가 발생했습니다. 서버에 요청을 보내지 못했습니다.")

    else:
        button_clicked = st.button('채팅 종료')
        if button_clicked :
            st.session_state['conversation_history'].clear()  # 대화 기록을 클리어
            st.write("채팅이 종료되었습니다. 이용해주셔서 감사합니다.")
            st.write("채팅 창을 닫아주세요")

        elif st.button("계속 대화하기"):
             st.write("음성 채팅 시작 버튼을 누르고 대화를 이어가주세요.")




