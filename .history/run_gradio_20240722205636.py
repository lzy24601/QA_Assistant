import os

import gradio as gr


def generate(imput, temperature):
    """
    根据输入生成文本

    参数：
    input:输入内容
    temperature:LLM的温度系数，越接近1随机性越高

    返回：
    output:生成的文本
    """
    output = "LLM返回的结果"
    return output


def format_chat_prompt(message, chat_history):
    prompt = ""
    for turn in chat_history:
        user_message, bot_message = turn
        prompt = f"{prompt}\nUser:{user_message}\nAssistant:{bot_message}"
    prompt = f"{prompt}\nUser:{message}\nAssistant:"
    return prompt

def respond(message, chat_history):
    formatted_prompt = format_chat_prompt(message=message, chat_history=chat_history)
    bot_message = llm.invoke()
    chat_history.append()



demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Slider(label="temperature", value=0, maximum=1, minimum=0),
    ],
    outputs=[gr.Textbox(label="Completion")],
    title="QA Assistant",
    description="welcome",
)
demo.launch()
