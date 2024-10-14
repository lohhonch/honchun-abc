from time import sleep

import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

from helper import constant


def get_current_page_name():
  ctx = get_script_run_ctx()
  if ctx is None:
    raise RuntimeError("Couldn't get script context")

  pages = get_pages("")

  return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
  with st.sidebar:
    if st.session_state.get("logged_in", False):
      st.header(f':page_with_curl: {constant.TITLE_MAIN}')
      st.page_link("pages/analyse.py", label=constant.TITLE_ANALYSE,
                   icon=":material/rebase:")
      st.page_link("pages/about_us.py", label=constant.TITLE_ABOUT_US,
                   icon=":material/info:")
      st.page_link("pages/methodology.py", label=constant.TITLE_METHODOLOGY,
                   icon=":material/psychology:")

      st.write("")
      st.write("")

      if st.button("Sign out", icon=":material/logout:"):
        logout()

    elif get_current_page_name() != "login":
      # Redirect to the login page if anyone tries to access secret page without logging in
      st.switch_page("login.py")


def logout():
  del st.session_state['logged_in']
  st.info("Logged out successfully!")
  sleep(0.5)
  st.switch_page("login.py")
