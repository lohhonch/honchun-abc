import streamlit as st

from helper import constant
from navigation import make_sidebar

st.set_page_config(
  page_title=f'{constant.TITLE_METHODOLOGY} | {constant.TITLE_MAIN}', page_icon=":page_with_curl:")

make_sidebar()

st.title(f':material/psychology: {constant.TITLE_METHODOLOGY}')
st.write("""
         Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Aenean sit amet felis nulla. 
         Nunc fringilla consectetur enim, et blandit libero imperdiet eu. 
         Ut lobortis metus vel nunc sollicitudin dignissim. 
         Fusce maximus non metus vel vulputate. 
         Cras feugiat, ante eget viverra laoreet, neque dui pellentesque ipsum, sagittis fringilla tortor nisl ut massa. 
         In rutrum, massa ac mattis scelerisque, mauris sapien accumsan enim, pretium congue dolor eros quis libero. 
         Donec elementum enim non fringilla rutrum. 
         Cras interdum purus in consequat consectetur. 
         Phasellus elit turpis, iaculis interdum diam ac, varius dignissim sapien.
         """)
