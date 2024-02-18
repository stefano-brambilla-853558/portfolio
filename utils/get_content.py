import os
from assets import content
from utils.streamlit_utils import get_lang

def get_info(field):
    try:
        return content.info[field]
    except:
        return f" >> Field {field} not found!"

def get_link(site, selection):
    try:
        return content.links[site][selection]
    except:
        return f" >> Link {site}-{selection} not found!"
    
def get_text(text, lang=None):
    if lang is None:
        lang = get_lang()
    try:
        return content.texts[text][lang]
    except:
        return f" >> Text {text}-{lang} not found!"
    
def get_certificate(certificate):
    try:
        return content.certificates[certificate]
    except:
        return f" >> Certificate {certificate} not found!"
    
def get_cv(lang=None):
    if lang is None:
        lang = get_lang()
    try:
        path = f"assets/cv-{lang}.pdf"
        if os.path.exists(path):
            return f"assets/cv-{lang}.pdf"
        else:
            return f" >> CV {lang} not found!"
    except:
        return f" >> CV {lang} not found!"