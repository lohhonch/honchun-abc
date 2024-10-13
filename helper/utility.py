import os

from dotenv import load_dotenv
import streamlit as st


def get_keyvalue(k):
  """
  Return value of secret key.
  Take from .streamlit/secrets.toml, followed by .env
  """

  load_dotenv('.env')

  ret = ''
  if st.secrets.load_if_toml_exists() and k in st.secrets:
    ret = st.secrets[k]
  else:
    if k in os.environ:
      ret = os.getenv(k)

  return ret
