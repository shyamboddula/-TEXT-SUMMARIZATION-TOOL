import streamlit as st
from txtai.pipeline import Summary
from PyPDF2 import  PdfReader
from transformers import pipeline
from transformers import pipeline







@st.cache_resource
def summary_text(text):
    summary_model = Summary() 
    summary_model = pipeline("summarization")
    summary = summary_model(text) 
    return summary_model(text)





choice = st.sidebar.selectbox("select your choice",["Summarize Text"])

if choice == "Summarize Text":
    st.header("Summarize Text")
    input_text=st.text_area("ENTER YOUR TEXT")
    if input_text is not None:

        if st.button("summarize Text"):
            col1, col2= st.columns([1,1])
            with col1:
                st.markdown("**YOUR OUTPUT TEXT**")
                st.info(input_text)
            with col2:
                result = summary_text(input_text)
                st.markdown("**Summarize text**")
                st.success(result)
                with open("doc_file.pdf","wb")as f:
                    # Apply background color using CSS
                     st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffcccb; /* Light Grayish Blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

