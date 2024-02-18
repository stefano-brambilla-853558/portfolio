import streamlit as st
from PIL import Image
from assets.content import *
from utils.get_content import get_info, get_link, get_text
import requests
import streamlit.components.v1 as components
from streamlit_carousel import carousel
from utils.streamlit_utils import lang_toggle

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")
lang_toggle()
st.sidebar.image(get_info('Photo'))

st.title(get_text("hobbies"))

with st.container():
   # Instagram photos of 3d printing
   st.markdown("""""")
   st.markdown(f"""## <a href={get_link("instagram", "main")}>Instagram</a>""", unsafe_allow_html=True)
   st.markdown(get_text("instagram")) 
   components.html(get_link("instagram", "widget"),height=500)

with st.container():
   # Thingiverse designs
   st.markdown(f"""## <a href={get_link("thingiverse", "main")}>Thingiverse</a>""", unsafe_allow_html=True)
   st.markdown(get_text("thingiverse")) 
   token="38a0a9cf5c3667dd6fd0eb761f47d4cc"
   thingiverse = requests.get(get_link("thingiverse", "designs"), headers={"Authorization": f"Bearer {token}"}).json()
   designs= [{'title': design["name"], 'img': design["thumbnail"], 'text': ""}
            for design in thingiverse["hits"]]
   carousel(items=designs, width=0.5)
