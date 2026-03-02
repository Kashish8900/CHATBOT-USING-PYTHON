import os
import streamlit as st
from langchain_groq import ChatGroq
os.environ["GROQ_API_KEY"]=""
LLM=ChatGroq(
    model_name = "llama-3.1-8b-instant",
    temperature=0.7
)
st.set_page_config(page_title="Chatbot")
st.title("KASHISH CHATBOT")
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]
    


user_input =st.text_input("ASK SOMETHINGS")


if user_input:
   # response= LLM.invoke(user_input)
    #st.write("BOT")
   # st.write(response.content)
   st.session_state.chat_history.append(user_input)
   response=LLM.invoke(st.session_state.chat_history)
   st.session_state.chat_history.append(response.content)
   st.write(response.content)