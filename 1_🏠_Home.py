import streamlit as st
import requests
#from streamlit_lottie import st_lottie
#from streamlit_timeline import timeline
import streamlit.components.v1 as components
#from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from assets.content import *
#from PIL import Image
#import openai
#from langchain.chat_models import ChatOpenAI
#from bs4 import BeautifulSoup
#from streamlit_carousel import carousel
#from st_clickable_images import clickable_images
from utils.get_content import get_text, get_link, get_info
from utils.streamlit_utils import lang_toggle

st.set_page_config(page_title='Home' ,layout="wide",page_icon='🏠')

# # -----------------  loading assets  ----------------- #
lang_toggle()
st.sidebar.image(get_info('Photo'))
    

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")


# # ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

full_name = get_info("Full_Name")

gradient('#FFD4DD','#000395','e0fbfc',get_text("greetings"), get_text("intro"))
st.write("")
st.write(get_text("about"))
    
# # -----------------  contact  ----------------- #

with st.container():
    col1,col2 = st.columns([4,8])
with col1:
    st.subheader(get_text("contact"))
    contact_form = f"""
    <form action="https://formsubmit.co/{get_info("Email")}" method="POST">
        <input type="hidden" name="_captcha value="false">
        <input type="text" name="name" placeholder="{get_text("contact_name")}" required>
        <input type="email" name="email" placeholder="{get_text("contact_mail")}" required>
        <textarea name="message" placeholder="{get_text("contact_message")}" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
