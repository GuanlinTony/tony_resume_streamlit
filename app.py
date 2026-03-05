import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# pip install streamlit pandas matplotlib
# streamlit run app.py

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(page_title="Tony Chen - Interactive Resume", layout="wide")

st.title("Guanlin (Tony) Chen - Interactive Resume")
st.subheader("Data Scientist | Financial Analytics | Machine Learning")

st.write("""
Analytical and goal-oriented data professional with expertise in statistical modeling,
data visualization, and financial analytics. Passionate about transforming complex
data into actionable insights.
""")

# ---------------------------------------------------
# Sidebar Widgets (Interactive)
# ---------------------------------------------------

st.sidebar.header("Customize View")

section = st.sidebar.selectbox(
    "Choose Resume Section",
    ["Overview", "Education", "Experience", "Skills"]
)

skill_level = st.sidebar.slider(
    "Minimum Skill Level",
    1,
    10,
    5
)

show_projects = st.sidebar.checkbox("Show Technical Projects", True)

# ---------------------------------------------------
# Education Section
# ---------------------------------------------------

education_data = {
    "Institution": [
        "Rotman School of Management, University of Toronto",
        "University of Toronto"
    ],
    "Degree": [
        "Master of Management Analytics (Candidate)",
        "Honours Bachelor of Science (Statistics)"
    ],
    "Year": [
        "2026",
        "2025"
    ]
}

edu_df = pd.DataFrame(education_data)

# ---------------------------------------------------
# Experience Section
# ---------------------------------------------------

experience_data = {
    "Company": [
        "Desjardins Insurance",
        "University of Toronto",
        "GF Securities"
    ],
    "Role": [
        "Analyst Practicum",
        "Statistical Analyst Intern",
        "Financial Product Assistant Intern"
    ],
    "Key Achievement": [
        "Improved insurance pricing model accuracy",
        "Built student retention prediction models",
        "Conducted IPO due diligence"
    ]
}

exp_df = pd.DataFrame(experience_data)

# ---------------------------------------------------
# Skills Table + Chart
# ---------------------------------------------------

skills_data = {
    "Skill": [
        "Python",
        "R",
        "SQL",
        "Machine Learning",
        "Financial Modeling",
        "Data Visualization",
        "Tableau",
        "Excel (VBA)"
    ],
    "Level": [
        9, 8, 8, 8, 7, 9, 7, 8
    ]
}

skills_df = pd.DataFrame(skills_data)

filtered_skills = skills_df[skills_df["Level"] >= skill_level]

# ---------------------------------------------------
# Display Sections
# ---------------------------------------------------

if section == "Overview":

    st.header("Profile Summary")

    st.write("""
    Graduate student at the Rotman School of Management specializing in Management Analytics.
    Experienced in machine learning, financial modeling, and statistical forecasting.
    """)

    st.metric("Programming Languages", "Python, R, SQL")
    st.metric("Tools", "Tableau, Excel, MySQL")

if section == "Education":

    st.header("Education")

    st.dataframe(edu_df)

if section == "Experience":

    st.header("Professional Experience")

    st.dataframe(exp_df)

    if show_projects:

        st.subheader("Technical Projects")

        st.write("""
        • Built predictive models for insurance claim pricing using GLM and Gradient Boosting  
        • Developed student retention prediction models using logistic regression  
        • Conducted financial market analysis using WIND database  
        """)

if section == "Skills":

    st.header("Skills")

    st.write("Filter using the slider in the sidebar.")

    st.dataframe(filtered_skills)

    st.subheader("Skill Proficiency Chart")

    fig, ax = plt.subplots()

    ax.bar(filtered_skills["Skill"], filtered_skills["Level"])

    ax.set_ylabel("Skill Level")
    ax.set_title("Skills Proficiency")

    plt.xticks(rotation=45)

    st.pyplot(fig)

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.write("---")
st.write("Contact: guanlin.chen@rotman.utoronto.ca")