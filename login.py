from time import sleep

import streamlit as st

from helper import constant, layout

st.set_page_config(page_title=constant.TITLE_LOGIN,
                   page_icon=":page_with_curl:")

st.title(f'📄{constant.TITLE_LOGIN}')

if layout.prompt_login():
  st.success("Logged in successfully!")
  sleep(0.5)
  st.switch_page("pages/analyse.py")
