# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Tony Chen | Interactive Resume", layout="wide")

# -----------------------------
# Light styling (subtle, content-first)
# Note: Streamlit theming is ideally done via .streamlit/config.toml; CSS below
# is intentionally minimal and focused on readable “cards”. :contentReference[oaicite:1]{index=1}
# -----------------------------
st.markdown(
    """
    <style>
      /* Layout */
      .block-container { padding-top: 1.2rem; padding-bottom: 1.2rem; }
      /* Header chips */
      .chip {
        display:inline-block; padding: 6px 10px; border-radius: 999px;
        border: 1px solid rgba(49,51,63,0.18);
        margin-right: 8px; margin-top: 6px; font-size: 0.9rem;
      }
      /* Cards for experiences/projects */
      .card {
        padding: 14px 16px;
        border: 1px solid rgba(49,51,63,0.16);
        border-radius: 14px;
        background: rgba(255,255,255,0.02);
        margin-bottom: 12px;
      }
      .card-title { font-weight: 800; font-size: 1.05rem; margin-bottom: 6px; }
      .card-meta  { opacity: 0.82; font-size: 0.92rem; margin-bottom: 8px; }
      .card-body  { font-size: 0.97rem; line-height: 1.5; }
      .muted { opacity: 0.75; }
      /* Small section spacing */
      .section-gap { margin-top: 0.25rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Resume Content (based on your uploaded resume)
# -----------------------------
NAME = "Guanlin (Tony) Chen"
EMAIL = "guanlin.chen@rotman.utoronto.ca"
PHONE = "+1 (437) 254-5698"
LINKEDIN = "linkedin.com/in/guanlin-chen-607a6a24a"

PROFILE_SUMMARY = (
    "Analytical and goal-oriented data professional with strong expertise in modeling, forecasting, "
    "and data visualization using statistical techniques and programming tools. My career goal is to grow "
    "as a Financial Analyst / Data Scientist in the Financial Industry or FinTech by turning complex data "
    "into clear, actionable business decisions."
)

education_df = pd.DataFrame(
    [
        {
            "Institution": "Rotman School of Management, University of Toronto",
            "Program": "Master of Management Analytics (Candidate)",
            "Year": "2026",
            "Location": "Toronto, ON, Canada",
        },
        {
            "Institution": "University of Toronto",
            "Program": "Honours BSc (Statistics) — with Distinction",
            "Year": "2025",
            "Location": "Toronto, ON, Canada",
        },
    ]
)

experience_items = [
    {
        "location": "Montreal (Hybrid), QC, Canada",
        "title": "Desjardins Insurance Group — Analyst Practicum (2025 – Present)",
        "meta": "Insurance pricing · feature engineering · ML modeling",
        "bullets": [
            "Explored 500+ candidate features to improve insurance claims pricing for agents and underwriters.",
            "Built GLM and gradient-boosting models; strengthened likelihood / loss-cost signals versus prior approach.",
            "Applied NLP + structured risk-factor engineering to convert property risk into usable model inputs.",
        ],
    },
    {
        "location": "Toronto, ON, Canada",
        "title": "University of Toronto — Statistical Analyst Internship (2024 – 2025)",
        "meta": "Retention forecasting · interpretable risk modeling · validation",
        "bullets": [
            "Led a 3-person consulting team to forecast second-year retention using LMS (Canvas) engagement data.",
            "Developed cumulative week-by-week logistic models to support early-intervention decisions.",
            "Built a validation workflow with k-fold CV + ROC analysis and threshold selection aligned to outcomes.",
        ],
    },
    {
        "location": "Guangzhou, Guangdong, China",
        "title": "GF Securities Co., Ltd. — Assistant to Financial Products Manager (Jun–Jul 2023)",
        "meta": "Due diligence · client ops · Excel/VBA automation",
        "bullets": [
            "Executed due diligence for 150+ IPO-prep clients with legal/risk/financial activity disclosure summaries.",
            "Automated daily client-product matching (8,000+ customer records/day) using Excel + VBA workflows.",
            "Collected client questionnaire feedback via daily calls to support portfolio service planning.",
        ],
    },
]

project_items = [
    {
        "location": "Guangzhou, Guangdong, China",
        "title": "China Merchants Bank (Private Banking) — Industry Research (Jul–Aug 2023)",
        "meta": "Market screening · WIND · Tableau storytelling",
        "bullets": [
            "Tracked and analyzed 12-month market performance using WIND; shortlisted top New Energy picks.",
            "Built Tableau visuals comparing hydrogen production/transmission cost efficiency and sustainability trade-offs.",
            "Presented a decision-oriented research narrative to senior stakeholders.",
        ],
    },
]

skills_df = pd.DataFrame(
    {
        "Skill": [
            "Python",
            "R",
            "SQL",
            "Excel (VBA)",
            "Tableau",
            "Statistical Modeling",
            "Data Visualization",
            "Time Series / Forecasting",
            "Machine Learning",
            "Financial Analytics",
        ],
        "Level (1-10)": [9, 8, 8, 8, 7, 8, 9, 7, 8, 8],
        "Category": [
            "Programming",
            "Programming",
            "Programming",
            "Tools",
            "Tools",
            "Analytics",
            "Analytics",
            "Analytics",
            "Analytics",
            "Finance",
        ],
    }
)

timeline_events = pd.DataFrame(
    [
        {"Year": 2023.5, "Label": "GF Securities Internship"},
        {"Year": 2023.7, "Label": "CMB Private Banking Research"},
        {"Year": 2024.7, "Label": "UofT Retention Modeling Internship"},
        {"Year": 2025.0, "Label": "Honours BSc (Statistics)"},
        {"Year": 2025.2, "Label": "Desjardins Insurance Practicum"},
        {"Year": 2026.0, "Label": "MMA (Candidate)"},
    ]
)

# -----------------------------
# Helpers
# -----------------------------
def render_card(item: dict):
    bullets_html = "<ul>" + "".join([f"<li>{b}</li>" for b in item["bullets"]]) + "</ul>"
    st.markdown(
        f"""
        <div class="card">
          <div class="card-title">{item['title']}</div>
          <div class="card-meta"><b>{item['location']}</b> · {item['meta']}</div>
          <div class="card-body">{bullets_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def plot_timeline(df: pd.DataFrame):
    """
    Vertical arrow timeline:
    - Left: Year (date)
    - Right: Event label
    - Title: "My Experience Progress"
    """
    df = df.sort_values("Year").reset_index(drop=True)

    fig, ax = plt.subplots()

    # Y positions from top to bottom
    y_positions = list(range(len(df)))[::-1]  # top = most recent if you want; keep as is
    x_line = 0

    # Draw vertical arrow (timeline spine)
    ax.annotate(
        "",
        xy=(x_line, min(y_positions) - 0.6),
        xytext=(x_line, max(y_positions) + 0.6),
        arrowprops=dict(arrowstyle="->", lw=2),
    )

    # Plot event markers and labels
    for y, (_, row) in zip(y_positions, df.iterrows()):
        # marker
        ax.scatter([x_line], [y], s=80)

        # left date
        ax.text(
            x_line - 0.25,
            y,
            f"{row['Year']:.1f}".rstrip("0").rstrip("."),
            ha="right",
            va="center",
            fontsize=10,
        )

        # right event label
        ax.text(
            x_line + 0.25,
            y,
            row["Label"],
            ha="left",
            va="center",
            fontsize=10,
        )

    # Styling
    ax.set_title("My Experience Progress")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(min(y_positions) - 1, max(y_positions) + 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    st.pyplot(fig)

def plot_skill_bars(df: pd.DataFrame):
    df = df.sort_values("Level (1-10)", ascending=True)
    fig, ax = plt.subplots()
    ax.barh(df["Skill"], df["Level (1-10)"])
    ax.set_xlabel("Proficiency (1–10)")
    ax.set_title("Skill Proficiency")
    ax.grid(True, axis="x", linestyle="--", alpha=0.25)
    st.pyplot(fig)

def plot_skill_pie(skills: pd.DataFrame):
    # Bucket to keep it readable & meaningful
    bucket_map = {
        "Programming": "Programming",
        "Analytics": "Data Analytics",
        "Finance": "Data Analytics",
        "Tools": "Tools",
    }
    tmp = skills.copy()
    tmp["Bucket"] = tmp["Category"].map(bucket_map).fillna("Other")

    # Weighted by proficiency level to approximate “coverage intensity”
    agg = tmp.groupby("Bucket")["Level (1-10)"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots()
    ax.pie(agg.values, labels=agg.index, autopct="%1.0f%%", startangle=90)
    ax.set_title("Skill Coverage (Weighted)")
    st.pyplot(fig)

# -----------------------------
# Header
# -----------------------------
hdr_left, hdr_right = st.columns([2.4, 1])
with hdr_left:
    st.title(NAME)
    st.markdown(
        f"""
        <span class="chip">📧 {EMAIL}</span>
        <span class="chip">📞 {PHONE}</span>
        <span class="chip">🔗 {LINKEDIN}</span>
        """,
        unsafe_allow_html=True,
    )
with hdr_right:
    st.markdown(
        """
        <div class="muted">
          Use the sidebar to navigate. Widgets update tables and charts instantly.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Resume Navigator")

section = st.sidebar.selectbox(
    "Go to section",
    ["Overview", "Education", "Experience", "Projects", "Skills"],
)

category_filter = st.sidebar.multiselect(
    "Show skill categories",
    options=sorted(skills_df["Category"].unique().tolist()),
    default=sorted(skills_df["Category"].unique().tolist()),
)

show_projects_details = st.sidebar.checkbox("Show project details", value=True)

# -----------------------------
# Pages
# -----------------------------
if section == "Overview":
    st.header("Profile Summary")
    st.write(PROFILE_SUMMARY)

    st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

    # ---- Full-width timeline (top) ----
    st.subheader("Career Timeline")
    plot_timeline(timeline_events)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---- Pie chart below ----
    st.subheader("Skills Coverage")
    st.caption("A compact view of how your skills cluster across programming, analytics, and tools.")
    plot_skill_pie(skills_df)

    st.subheader("Core Focus Areas")
    focus = [
        "Financial analytics & modeling",
        "Statistical forecasting",
        "ML-based prediction",
        "Visualization for decision-making",
        "Python / R / SQL + Excel (VBA)",
    ]
    st.markdown("".join([f'<span class="chip">{x}</span>' for x in focus]), unsafe_allow_html=True)

elif section == "Education":
    st.header("Education")
    st.dataframe(education_df, use_container_width=True, hide_index=True)

elif section == "Experience":
    st.header("Internships / Professional Experience")
    st.caption("Experience presented as readable cards (titles bolded; no numeric indices).")
    for item in experience_items:
        render_card(item)

elif section == "Projects":
    st.header("Technical Projects")

    if not project_items:
        st.info("No projects added yet.")
    else:
        # Clean table: location replaces numeric index
        proj_tbl = pd.DataFrame(
            [
                {
                    "Location": p["location"],
                    "Project": p["title"].split("—")[0].strip(),
                    "Focus": p["meta"],
                }
                for p in project_items
            ]
        )
        st.dataframe(proj_tbl, use_container_width=True, hide_index=True)

        if show_projects_details:
            st.subheader("Project Details")
            for item in project_items:
                render_card(item)

elif section == "Skills":
    st.header("Skills")

    # Category filter from sidebar
    skills_view = skills_df[skills_df["Category"].isin(category_filter)].copy()

    # Put slider *under* the chart: use session_state threshold
    if "min_skill_level" not in st.session_state:
        st.session_state.min_skill_level = 6

    filtered = skills_view[skills_view["Level (1-10)"] >= st.session_state.min_skill_level].copy()

    st.subheader("Skills Table")
    st.dataframe(
        filtered[["Skill", "Level (1-10)", "Category"]].sort_values(
            ["Category", "Level (1-10)"], ascending=[True, False]
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Skill Proficiency Chart")
    if filtered.empty:
        st.warning("No skills match the current minimum level filter. Lower the slider to see more.")
    else:
        plot_skill_bars(filtered[["Skill", "Level (1-10)"]])

    # Slider appears at the bottom (under the chart)
    st.session_state.min_skill_level = st.slider(
        "Minimum skill level (drag to filter the chart above)",
        min_value=1,
        max_value=10,
        value=int(st.session_state.min_skill_level),
        key="min_skill_level_slider",
    )

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption(f"Contact: {EMAIL}")