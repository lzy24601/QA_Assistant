import streamlit as st

from llm import zhipuai_llm

st.title("我的QA助手")


def generate_response(input_text):
    llm = zhipuai_llm.ZhipuAILLM()
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "who are you?")
    submitted = st.form_submit_button("submit")
    if submitted:
        generate_response(text)

def main():
    st.title("QA")
