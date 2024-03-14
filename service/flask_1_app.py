from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, AutoTokenizer
import torch

app = Flask(__name__)

# 모델 및 토크나이저 초기화
model_dir = './service/model'
tokenizer = AutoTokenizer.from_pretrained(model_dir, bos_token='</s>', eos_token='</s>', pad_token='<pad>')
model = GPT2LMHeadModel.from_pretrained(model_dir)


def return_answer_by_chatbot(user_text):
    sent = '<usr>' + user_text + '<sys>'
    input_ids = [tokenizer.bos_token_id] + tokenizer.encode(sent, add_special_tokens=False)
    input_ids = torch.tensor([input_ids], dtype=torch.long)
    output = model.generate(input_ids, max_length=150, do_sample=True, top_k=2)
    sentence = tokenizer.decode(output[0].tolist())
    chatbot_response = sentence.split('<sys> ')[1].replace('</s>', '')
    return chatbot_response


@app.route("/predict", methods=["POST"])
def predict():
    user_text = request.json['user_text']
    chatbot_response = return_answer_by_chatbot(user_text)
    return jsonify({'chatbot_response': chatbot_response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
