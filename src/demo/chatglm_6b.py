import gradio as gr
import random
import time
from transformers import AutoTokenizer, AutoModel
from itertools import chain

ckpt_path = '../ckpt/chatglm-6b'

tokenizer = AutoTokenizer.from_pretrained(ckpt_path, trust_remote_code=True)
model = AutoModel.from_pretrained(ckpt_path, trust_remote_code=True, device_map='auto', load_in_8bit=True)

def gen_response(query, history):
    response, history = model.chat(tokenizer, query, history=history)
    # print(response)
    return response, history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history):
        user_message, history = history[-1][0], history[:-1]
        response, history = gen_response(query=user_message, history=history)
        return history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()

