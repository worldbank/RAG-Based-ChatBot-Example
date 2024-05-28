import streamlit as st

from local_loader import list_pdf_files

paths = list(list_pdf_files())

file_path = st.selectbox("Select a data file to view", paths, index=None)

if file_path:
    with open(file_path,"r") as f:
        md_content = f.read()
        st.markdown(md_content)
