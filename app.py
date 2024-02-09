import streamlit as st
from summarizer import Summarizer

st.header(" Summary of Input Text")
text = st.text_area("Input the text to get questions",placeholder="Enter the text", height=200)
button = st.button("Get Summarised")

if text and button:
    model = Summarizer()
    result = model(text, min_length=60, max_length = 500 , ratio = 0.4)
    summarized_text = ''.join(result)
    st.write(summarized_text)
    
    