import uuid

import pandas as pd
import streamlit as st
import streamlit_antd_components as sac

from helper.database import execute_non_query, fetch_all

REPOSITORY_NAME_LENGTH = 100


def repository_manage():
  def show_repository_option(repository_ids):
    placeholder = st.session_state.show_repository_option_placeholder
    with placeholder.container():
      lst_repository_ids = repository_ids.split(",")
      edited_rows = st.session_state.key_repository_manage_data["edited_rows"]
      for row in edited_rows:
        row_id = row
        is_selected = edited_rows[row_id]["select"]
        if is_selected:
          st.write(f'{lst_repository_ids[row_id]} is selected')

  data = fetch_all("""
                    SELECT t1.name, t1.creation_date, t1.repository_id
                    FROM Repository t1
                    ORDER BY t1.creation_date DESC""")
  if data:
    df = pd.DataFrame(data).set_axis(["name", "creation_date", "repository_id"], axis="columns")
    df["select"] = False
  else:
    df = pd.DataFrame(columns=['name', 'creation_date', 'repository_id', 'select'])
    sac.alert(label="Repository is empty. Please setup new repository.", description=None,
              color="info", banner=False, icon=True, closable=False)

  st.data_editor(
    df,
    column_config={
      "name": st.column_config.Column("Name", width="medium", required=True),
      "creation_date": st.column_config.DatetimeColumn("Creation Date", width="medium", format="D MMM YYYY, h:mm a", required=True),
      "select": st.column_config.CheckboxColumn(label="Option", help="Select to view _files_ or to delete _repository_"),
      "repository_id": None,
    },
    disabled=["name", "creation_date", "repository_id"],
    hide_index=True,
    num_rows="fixed",
    on_change=show_repository_option,
    args=[",".join(df['repository_id'].to_list())],
    key="key_repository_manage_data"
  )

  if "show_repository_option_placeholder" not in st.session_state:
    placeholder = st.empty()
    st.session_state['show_repository_option_placeholder'] = placeholder

  # End of repository_manage()


def save_repository_to_db(unique_id, uploaded_files, repository_name):
  # Simple validation
  if repository_name == "" or len(repository_name) > REPOSITORY_NAME_LENGTH or not uploaded_files:
    sac.alert(label="Oops", description="Something went wrong", color="error", banner=False, icon=True, closable=True)
    return False

  # Repository - Save to database
  execute_non_query("INSERT INTO Repository (repository_id, name) VALUES (?, ?)", [unique_id, repository_name])
  # Files - Save to database
  for uploaded_file in uploaded_files:
    file_name = uploaded_file.name
    type = uploaded_file.type
    size = uploaded_file.size
    file_content = uploaded_file.read()
    st.write((file_name, type, size, len(file_content)))
    execute_non_query(
      "INSERT INTO Files (repository_id, file_name, type, size, data) \
      VALUES (?, ?, ?, ?, ?)", [unique_id, file_name, type, size, file_content])

  return True

  # End of save_repository_to_db()


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
