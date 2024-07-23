import gradio as gd
import os

def generte(imput, temperature):
    """ 
    根据输入生成文本

    参数：
    input:输入内容
    temperature:LLM的温度系数，越接近1
    """