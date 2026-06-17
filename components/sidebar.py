import streamlit as st

from config import LECTURE_PAGES, MAIN_PAGES


def get_selected_page():
    page = st.sidebar.radio("Navigate", MAIN_PAGES)
    dropdown_page = st.sidebar.selectbox(
        "Lectures",
        ["", *LECTURE_PAGES],
        format_func=lambda value: "Select a Lecture" if value == "" else value,
    )

    if dropdown_page:
        return dropdown_page

    return page
