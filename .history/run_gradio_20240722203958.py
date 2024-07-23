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
                gr.Slider(label="temperature", value=0, maximum=1, minimum=0)],
        outputs=[gr.Textbox(label="Completion")],
        title="QA Assistant",
        des

    )