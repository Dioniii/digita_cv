import streamlit as st

from config import DESCRIPTION, NAME
from utils.assets import load_profile_pic, load_resume_bytes


def render_home():
    profile_pic = load_profile_pic()
    resume_bytes = load_resume_bytes()

    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=resume_bytes,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    st.write("\n")
    st.subheader("Certifications or Voluntary Experience")
    st.write(
        """
- 🧠 Second Place in Hackathon "Digital Skills Festival" - Hack for Green
- 🧠 Automate the Boring Stuff with Python Programming - Certificate
- 🧠 Loyola Professional - Basics of Robotics
- 🧠 Workshop "My city made different" - Ryco Superschool
"""
    )

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

    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    st.write("🚧", "**Data Entry | Workflow Prishtina**")
    st.write("05/2024 - 09/2024")
    st.write(
        """
- ● Performed accurate data entry with a focus on minimizing errors
- ● Efficiently managed and organized data to meet deadlines and project requirements
- ● Utilized software tools such as Microsoft Excel and Google Sheets for data processing
- ● Maintained data confidentiality and adhered to company policies and regulatory standards
"""
    )
