import streamlit as st

from helper import constant
from navigation import make_sidebar

st.set_page_config(
    page_title=f'{constant.TITLE_ANALYSE} | {constant.TITLE_MAIN}', page_icon=":page_with_curl:")

make_sidebar()
