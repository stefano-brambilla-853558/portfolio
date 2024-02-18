import streamlit as st

def get_lang():
    if 'lang' not in st.session_state:
        st.session_state.lang = 'ita'
    return st.session_state.lang

def set_lang():
    if 'lang' not in st.session_state:
        st.session_state.lang = 'ita'
    st.session_state.lang = "eng" if st.session_state.lang == "ita" else "ita"
    
def lang_toggle():
    
    if 'lang' not in st.session_state:
        st.session_state.lang = 'ita'
    default= False if st.session_state.lang == 'ita' else True
    col1, col2 = st.sidebar.columns([0.3, 0.7])
    col1.markdown("""<div style="text-align: right"> Italiano </div>""", unsafe_allow_html=True)
    on = col2.toggle('English', value=default, on_change=set_lang)
     