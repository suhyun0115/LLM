import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from pydub import AudioSegment
import requests
from transformers import GPT2LMHeadModel, AutoTokenizer
import torch

# Streamlit app title and description
st.title("📝도배하자 with 챗봇")
st.markdown(
    "<p style='color:gray; font-size:20px; font-family:Arial;'>어서오세요 고객님! 음성 인식 챗봇 '딥봇'입니다.</p>",
    unsafe_allow_html=True
)

# 모델 및 토크나이저 초기화
model_dir = './service/model'
tokenizer = AutoTokenizer.from_pretrained(model_dir, bos_token='</s>', eos_token='</s>', pad_token='<pad>')
model = GPT2LMHeadModel.from_pretrained(model_dir)

# 함수 정의: 사용자 입력을 받아 챗봇 응답을 반환
def return_answer_by_chatbot(user_text):
    sent = '<usr>' + user_text + '<sys>'
    input_ids = [tokenizer.bos_token_id] + tokenizer.encode(sent, add_special_tokens=False)
    input_ids = torch.tensor([input_ids], dtype=torch.long)
    output = model.generate(input_ids, max_length=150, do_sample=True, top_k=2)
    sentence = tokenizer.decode(output[0].tolist())
    chatbot_response = sentence.split('<sys> ')[1].replace('</s>', '')
    return chatbot_response

# Streamlit app code
@st.cache(allow_output_mutation=True)
def get_audio_buffer():
    return AudioSegment.empty()

audio_buffer = get_audio_buffer()

webrtc_ctx = webrtc_streamer(
    key="audio-record",
    mode=WebRtcMode.SENDRECV,
    audio_receiver_size=1024,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"audio": True, "video": False},
)

if webrtc_ctx.state.playing:
    st.audio(
        audio_buffer.export(format="wav", codec="pcm_s16le", bitrate="128k").read(),
        format='audio/wav'
    )

    st.text("Recording...")

    while True:
        if webrtc_ctx.audio_receiver:
            try:
                audio_frames = webrtc_ctx.audio_receiver.get_frames(timeout=3)
            except queue.Empty:
                st.write("No audio received...")
            sound_chunk = AudioSegment.empty()
            try:
                for audio_frame in audio_frames:
                    sound = AudioSegment(
                        data=audio_frame.to_ndarray().tobytes(),
                        sample_width=audio_frame.format.bytes,
                        frame_rate=audio_frame.sample_rate,
                        channels=len(audio_frame.layout.channels),
                    )
                    sound_chunk += sound
                if len(sound_chunk) > 0:
                    audio_buffer += sound_chunk
            except UnboundLocalError:
                st.write("No audio detected...")
        else:
            break

if st.button("전송"):
    audio_buffer.export("recorded_audio.wav", format="wav")
    files = {"file": open("recorded_audio.wav", "rb")}
    response = requests.post("http://localhost:5000/predict", files=files)
    if response.status_code == 200:
        data = response.json()
        chatbot_response = data['chatbot_response']
        st.write(f"챗봇 응답: {chatbot_response}")
    else:
        st.text("오류가 발생했습니다. 서버에 요청을 보내지 못했습니다.")
