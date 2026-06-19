import streamlit as st

from config import MAIN_PAGES


def get_selected_page():
    return st.sidebar.radio("Navigate", MAIN_PAGES)
