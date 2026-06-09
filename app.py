import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Dion Gurgule"
PAGE_ICON = ":wave:"
NAME = "Dion Gurgule"
DESCRIPTION = """
Data Scientist student highly passionate in AI and LLMs.
"""

EMAIL = "dgurgule@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/diongurgule"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/CV - English.pdf"
profile_pic_file = "assets/profile-pic.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Certifications or Voluntary Experience")
    st.write(
        """
- 🧠 Second Place in Hackathon “Digital Skills Festival” - Hack for Green
- 🧠 Automate the Boring Stuff with Python Programming - Certificate
- 🧠 Loyola Professional - Basics of Robotics 
- 🧠 Workshop “My city made different” - Ryco Superschool
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👨‍💻 Programming: Python, JavaScript / TypeScript, React Native, SQL
- 📱 Mobile Development: Expo, EAS, WidgetKit, TestFlight, iOS deployment
- 🤖 AI & Machine Learning: Local LLMs, AI agent configuration
- 🗄️ Databases & Cloud: SQL, PostgreSQL, Hetzner Cloud VPS, Docker, AWS
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Data Entry | Workflow Prishtina**")
    st.write("05/2024 - 09/2024")
    st.write(
        """
- ● Performed accurate data entry with a focus on minimizing errors
- ● Efficiently managed and organized data to meet deadlines and project requirements
- ● Utilized software tools such as Microsoft Excel and Google Sheets for data processing
- ● Maintained data confidentiality and adhered to company policies and regulatory standards 

""")
# --- Projects ---
    st.write("\n")
    st.subheader("Projects")
    st.write("---")

    # --- JOB 2
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

    # --- JOB 3
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

    # --- JOB 4
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

elif page == "About":
    st.title("About Me")
    st.write("""
    I am a computer science student with a strong passion for learning 
    everything around data science, AI, machine learning. I am also
    highly intrigued by AI agents and implementing them, models such as
    ClawdBot, Hermes Agent spike my intrests and allow me to explore the future of 
    such technologies.
 
    Throughout my studies I have taken part in different projects that allowed me to 
    build and improve my skills in Java, PHP, Python and also taught me
    best practices in implementing different system architectures
    payment methods and delivering a full system ready for businesses to deploy.
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
