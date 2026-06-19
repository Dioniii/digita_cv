import streamlit as st

from components.sidebar import get_selected_page
from config import PAGE_ICON, PAGE_TITLE
from views.about import render_about
from views.home import render_home
from views.lessons import render_lessons
from views.projects import render_projects


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

page = get_selected_page()

if page == "Home":
    render_home()
elif page == "About":
    render_about()
elif page == "Lessons":
    render_lessons()
elif page == "Projects":
    render_projects()
