import gradio as gr
import os

def generte(imput, temperature):
    """ 
    根据输入生成文本

    参数：
    input:输入内容
    temperature:LLM的温度系数，越接近1随机性越高
    
    返回：
    output:生成的文本
    """

    demo = gr.Interface(
        fn=generate,
        inputs=[gr.Textbox(label="Prompt"),

    )