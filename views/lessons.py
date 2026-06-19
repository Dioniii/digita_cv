import streamlit as st

from views.lecture_12 import render_lecture_12_content


LESSONS = [
    {
        "number": "12",
        "title": "Databases, Data Storage & SQL Concepts",
        "render": render_lecture_12_content,
    }
]


def render_lessons():
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                background: #ffffff;
            }

            div[data-testid="stMainBlockContainer"] {
                max-width: 940px;
                padding-top: 8.75rem;
            }

            .lessons-hero {
                text-align: center;
            }

            .lessons-title {
                align-items: center;
                display: inline-flex;
                font-size: 3rem;
                font-weight: 800;
                gap: 1rem;
                letter-spacing: 0;
                line-height: 1.1;
                margin: 0;
            }

            .lessons-icon {
                font-size: 3.25rem;
                line-height: 1;
            }

            .lessons-subtitle {
                color: #6b7280;
                font-size: 1rem;
                margin: 1.75rem 0 4rem;
            }

            .lessons-rule {
                border-top: 1px solid rgba(15, 23, 42, 0.18);
                margin: 0 0 3rem;
            }

            div[data-testid="stExpander"] {
                background: transparent;
                border: 1px solid rgba(15, 23, 42, 0.22);
                border-radius: 8px;
                box-shadow: none;
                margin-top: 0;
            }

            div[data-testid="stExpander"] details summary {
                min-height: 3rem;
            }

            div[data-testid="stExpander"] details summary p {
                font-size: 1rem;
            }

            div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
                background: rgba(255, 255, 255, 0.54);
                border-top: 1px solid rgba(15, 23, 42, 0.12);
            }

            @media (max-width: 700px) {
                div[data-testid="stMainBlockContainer"] {
                    padding-top: 4rem;
                }

                .lessons-title {
                    font-size: 2.25rem;
                }

                .lessons-icon {
                    font-size: 2.5rem;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="lessons-hero">
            <h1 class="lessons-title">Lesson Summaries</h1>
        </div>
        <div class="lessons-rule"></div>
        """,
        unsafe_allow_html=True,
    )

    for lesson in LESSONS:
        label = f":blue_book: Lecture {lesson['number']} - {lesson['title']}"
        with st.expander(label):
            lesson["render"]()
