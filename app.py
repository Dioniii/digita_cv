import streamlit as st

from components.sidebar import get_selected_page
from config import PAGE_ICON, PAGE_TITLE
from views.about import render_about
from views.home import render_home
from views.lecture_12 import render_lecture_12
from views.projects import render_projects


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

page = get_selected_page()

if page == "Home":
    render_home()
elif page == "About":
    render_about()
elif page == "Projects":
    render_projects()
elif page == "Lecture 12":
    render_lecture_12()
