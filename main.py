#Importing the requried libraries
import os

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from PyPDF2 import PdfReader

#importing the functions from Geminiutil.py
from Geminiutil import load_gemini_ai_model

from Geminiutil import gemini_ai_vision

from Geminiutil import Emebbed_Text_Generation

from Geminiutil import gemini_user_response

from Geminiutil import document_summary
working_directory=os.path.dirname(os.path.abspath(__file__))

#createing an streamlit app
st.set_page_config(
    page_title="Gemini AI",
    page_icon="🧠",
    layout="centered",
)

#create an option_menu
with st.sidebar:

    selected=option_menu("Gemini AI",
                         ['Chatbot',
                          'Image Captioning',
                          'Embeddings',
                          'Ask me Anything',
                          'Document Summary'],
                         menu_icon="robot",
                         icons=['chat-dots-fill',
                                'image-fill',
                                'textarea-t',
                                'patch-question-fill',
                                'file-earmark-text-fill'],
                         default_index=0
                         )


def translate_role_for_streamlite(user_role):
    if user_role=='model':
        return 'assistant'
    else:
        return user_role

#creating a chatbot 
if selected=='Chatbot':
    model=load_gemini_ai_model()

    if 'chat_session' not in st.session_state:
        st.session_state.chat_session=model.start_chat(history=[])

    st.title('🤖 ChatBot')

    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlite(message.role)):
            st.markdown(message.parts[0].text)


    user_prompt=st.chat_input("Ask Gemini Pro.....")

    if user_prompt:
        st.chat_message('user').markdown(user_prompt)

        gemini_response=st.session_state.chat_session.send_message(user_prompt)

        with st.chat_message('assistant'):
            st.markdown(gemini_response.text)

#creating an image captioning

if selected=='Image Captioning':

    st.title("📷 Snap Narrate")

    uploaded_image=st.file_uploader("Upload an Image....",type=['jpg','jpeg','png'])



    if st.button('Generate Caption'):
        image=Image.open(uploaded_image)

        col1, col2 =st.columns(2)

        with col1:
            resized_image=image.resize((800,500))
            st.image(resized_image)

        default_prompt = 'Write a Short Caption for this Image'

        caption=gemini_ai_vision(default_prompt,image)

        with col2:
            st.info(caption)
#creating an embeddings

if selected=='Embeddings':
    st.title('🗟 Text Embeddings')

    input_text=st.text_area(label="",placeholder="Enter the Text TO get Embedding")

    if st.button('Get Embeddings'):
        respone=Emebbed_Text_Generation(input_text)

        st.markdown(respone)

#creating Question and Answer with AI
if selected=="Ask me Anything":
    st.title('❓ Ask me a Question')

    user_input=st.text_area(label="",placeholder="Ask Google Gemini AI.....")

    if st.button('Get Response'):
        respone=gemini_user_response(user_input)

        st.markdown(respone)

#creating a summary of the pdf document.
if selected=="Document Summary":
    st.title('🗎 PDF Summariser')

    pdf_file=st.file_uploader("Upload a PDF File",type=['pdf'])
    if pdf_file is not None:
        if st.button('Summarise'):
            if pdf_file.name.endswith(".pdf"):
                pdf_reader = PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()

                document_response=document_summary(text)
                st.write("Summarised content:")
                st.write(document_response)
            else:
                st.write("Upload a Pdf document")

