import streamlit as st
import base64
from assets.content import *
from utils.get_content import get_text, get_cv, get_info
from utils.streamlit_utils import lang_toggle
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")
lang_toggle()
st.sidebar.image(get_info('Photo'))

st.title(get_text("cv"))

#st.write("[Click here if it's blocked by your browser](https://cognitiveclass.ai/)")

with open(get_cv(),"rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
