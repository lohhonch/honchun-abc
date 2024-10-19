import uuid
import streamlit as st
import streamlit_antd_components as sac

REPOSITORY_NAME_LENGTH = 100


def save_repository_to_db(unique_id, uploaded_files, repository_name):
  # Simple validation
  if repository_name == "" or len(repository_name) > REPOSITORY_NAME_LENGTH or not uploaded_files:
    sac.alert(label="Oops", description="Something went wrong", color="error", banner=False, icon=True, closable=True)
    return False

  # Logic to save

  return True


def repository_uploader(max_files):
  placeholder = st.empty()

  with placeholder.container():
    st.subheader("Upload files to start building your repository")
    max_files = int(max_files)

    # Name the repository
    repository_name = st.text_input("Name of repository:", max_chars=REPOSITORY_NAME_LENGTH,
                                    key="key_repository_setup_name")

    # Files uploader using `st.file_uploader`.
    uploaded_files = st.file_uploader(
      label=f"Support up to ***{max_files}*** files (.docx, .pdf, .txt)", type=["docx", "pdf", "txt"],
      accept_multiple_files=True,
      key="key_repository_setup_files"
    )

    if len(uploaded_files) > max_files:
      st.warning(f'Maximum number of files reached. Only the first {max_files} will be processed.')

    # Setup fields
    uploaded_files = uploaded_files[:max_files]
    repository_name = repository_name.strip()[:REPOSITORY_NAME_LENGTH]
    unique_id = str(uuid.uuid4())

    if repository_name != "" and uploaded_files:
      if st.button("Upload", type="primary"):
        if save_repository_to_db(unique_id=unique_id, uploaded_files=uploaded_files, repository_name=repository_name):
          placeholder.empty()
          st.session_state["save_repository_to_db"] = True

  if st.session_state.get("save_repository_to_db", False):
    # Show Success acknowledgement screen
    sac.result(label="Setting Up New Repository", description=f"unique id: {unique_id}", status="success")
    del st.session_state["save_repository_to_db"]

  # End of repository_uploader()
