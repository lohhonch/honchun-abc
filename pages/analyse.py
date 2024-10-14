import streamlit as st

from helper import constant
from navigation import make_sidebar

st.set_page_config(
  page_title=f'{constant.TITLE_ANALYSE} | {constant.TITLE_MAIN}', page_icon=":page_with_curl:")

make_sidebar()

# Debugging what is in st.session_state
st.write(st.session_state)

st.title(f':material/rebase: {constant.TITLE_ANALYSE}')
st.write("Start by uploading a set of documents below and we will analyse them for conflicts.")

# Documents uploader using `st.file_uploader`.
uploaded_files = st.file_uploader(
  label=f"Upload up to ***{constant.MAX_NUMBER_OF_FILES}*** documents (.docx or .pdf)", type=("docx", "pdf", "txt"),
  accept_multiple_files=True,
  key="documents_uploaded"
)

if len(uploaded_files) > constant.MAX_NUMBER_OF_FILES:
  st.warning(
    f'Maximum number of documents reached. Only the first {constant.MAX_NUMBER_OF_FILES} will be processed.')
  uploaded_files = uploaded_files[:constant.MAX_NUMBER_OF_FILES]
