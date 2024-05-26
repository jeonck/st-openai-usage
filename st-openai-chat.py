# https://github.com/openai/openai-python

import streamlit as st
from openai import OpenAI

# Streamlit 애플리케이션
st.title("OpenAI Chat App")

# 사이드바에서 API 키 입력 받기
api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
if not api_key:
    st.sidebar.error("API key is required to proceed.")
    st.stop()

# OpenAI 클라이언트 인스턴스 생성
client = OpenAI(api_key=api_key)

# 폼 생성
with st.form(key='chat_form'):
    user_input = st.text_input("You:", key="user_input")
    submit_button = st.form_submit_button(label='Send')
# Streamlit에서 텍스트 입력 필드에서 엔터 키를 눌렀을 때 특정 동작을 수행하는 방법은
# st.form과 st.form_submit_button을 사용하는 것입니다.

# 폼이 제출되었을 때 OpenAI API 호출
if submit_button and user_input:
    with st.spinner("Waiting for response..."):
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="gpt-4o",
        )
        # 응답 출력
        st.write("OpenAI:", response.choices[0].message.content)
elif submit_button and not user_input:
    st.error("Please enter a message to send.")

# Run the Streamlit app
if __name__ == "__main__":
    st.write("Streamlit app is running.")