import streamlit as st

from config import EMAIL, LINKEDIN_URL


def render_about():
    st.title("About Me")
    st.write(
        """
    I am a computer science student with a strong passion for learning
    everything around data science, AI, machine learning. I am also
    highly intrigued by AI agents and implementing them, models such as
    ClawdBot, Hermes Agent spike my intrests and allow me to explore the future of
    such technologies.

    Throughout my studies I have taken part in different projects that allowed me to
    build and improve my skills in Java, PHP, Python and also taught me
    best practices in implementing different system architectures
    payment methods and delivering a full system ready for businesses to deploy.
    """
    )

    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
