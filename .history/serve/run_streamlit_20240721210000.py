import streamlit as st

from llm import zhipuai_llm

st.title("我的QA助手")
api_key = st.sidebar.text_input()

def generate_response(input_text):
    llm = zhipuai_llm.ZhipuAILLM()
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "who are you?")
    submitted = st.form_submit_button("submit")
    if submitted:
        generate_response(text)

def main():
    st.title("QAAssistant")
    
    api_key = st.sidebar.text_input("请输入api_key")

    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        st.session_state.messages.append({"role": "user", "text": prompt})

        answer = generate_response(prompt)

        if answer is not None

