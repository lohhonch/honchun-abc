import streamlit as st

from helper import constant
from navigation import make_sidebar

st.set_page_config(
  page_title=f'{constant.TITLE_ABOUT_US} | {constant.TITLE_MAIN}', page_icon=":page_with_curl:")

make_sidebar()

st.title(f':material/info: {constant.TITLE_ABOUT_US}')

st.header("Problem Statement")
st.write("""
         The current process of reviewing lengthy tender documentations is time - consuming and prone to human error, especially in identifying conflicting clauses.
         This manual review process can lead to delays and potential legal issues if conflicting clauses are not identified and resolved accurately.
         """)
st.header("Proposed Solution")
st.write("""
         Implementing LLM technology to assist in the review of tender documentations can significantly reduce the time and effort required to identify conflicting clauses. 
         By leveraging LLM's natural language processing capabilities, the system can efficiently analyse the various clauses and sub - clauses to flag potential conflicts, thereby streamlining the review process and minimising the risk of oversight.
         """)
st.header("Impact")
st.write("""
         Integrating LLM into the tender documentation review process will lead to improved efficiency and accuracy. 
         This will result in faster turnaround times for tender reviews, reduced potential for legal disputes due to conflicting clauses, and overall cost savings for the organisation. 
         Additionally, the use of LLM technology demonstrates a commitment to leveraging innovative solutions for enhancing operational processes within the organisation.
         """)
