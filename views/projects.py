import streamlit as st


def render_projects():
    st.write("\n")
    st.subheader("Projects")
    st.write("---")

    st.write("\n")
    st.write("🚧", "**Hotel Management System React, NodeJS, MySQL**")
    url = "https://github.com/Dioniii/LabCourse1"
    st.write("[Github Repository](%s)" % url)
    st.write(
        """
A full-stack web application that allows hotel staff to manage bookings, customer data,
and room availability. Features include user authentication, real-time room status
updates, and a responsive admin dashboard
"""
    )

    st.write("\n")
    st.write("🚧", "**Real Time Traffic Monitoring System**")
    url1 = "https://github.com/KledionBerisha/CityFlow"
    st.write("[Github Repository](%s)" % url1)
    st.write(
        """
**This project monitors city traffic and public transport in real time.
It tracks buses, detects traffic jams and delays, and shows the data on a dashboard with maps and charts.
It can also send alerts and predict traffic for the next few minutes. It is a simulation of Prishtina-Kosovo.
"""
    )

    st.write("\n")
    st.write("🚧", "**Job Listings Scraper**")
    url2 = "https://github.com/Dioniii/JobScraperBot"
    st.write("[Github Repository](%s)" % url2)
    st.write(
        """
A small python script that scrapes sites like "KosovaJobs" and "Superpuna" for jobs based on keywords and user requiremets. Also implemented
automatic messaging via a Discord bot setup.
"""
    )
