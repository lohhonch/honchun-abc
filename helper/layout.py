import hmac

import streamlit as st

from helper.utility import get_keyvalue


def prompt_login():
  """Returns `True` if user had entered the correct password"""

  def password_entered():
    # Checks if a password entered by the user is correct
    if hmac.compare_digest(st.session_state["password_to_enter"], get_keyvalue("PASSWORD_TO_ENTER")):
      st.session_state["logged_in"] = True
      del st.session_state["password_to_enter"]  # Never store the password
    else:
      st.session_state["logged_in"] = False

  # Return True if the password is validated
  if st.session_state.get("logged_in", False):
    return True

  st.info("1. You are required to read and agree to the following *Disclaimer*.",
          icon=":material/check_circle:")

  expander = st.expander("DISCLAIMER", icon="🔔")
  expander.write('''**IMPORTANT NOTICE:** This web application is developed as a proof-of-concept prototype. 
                 The information provided here is **NOT intended for actual usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters''')
  expander.write('**Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**')
  expander.write(
    'Always consult with qualified professionals for accurate and personalized advice.')

  agree = st.checkbox('I have read and agree to the disclaimer.')

  if agree:
    st.info("2. Key in *Password* to continue.", icon="🔑")

    # Show input for password
    st.text_input("Password", type="password", label_visibility="collapsed",
                  on_change=password_entered, key="password_to_enter")
    if "logged_in" in st.session_state and not st.session_state['logged_in']:
      st.error("😕 Password incorrect")

  return False
