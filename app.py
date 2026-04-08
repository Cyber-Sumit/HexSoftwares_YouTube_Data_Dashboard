import streamlit as st
import pandas as pd
import plotly.express as px

# basic page setup
st.set_page_config(
    page_title="YouTube Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# simple custom styling to make it feel polished
st.markdown("""
<style>
.main {
    background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
}
[data-testid="stMetric"] {
    background: #1f2937;
    border: 1px solid #374151;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# dashboard heading
st.title("📊 YouTube Data Dashboard")
st.caption("A clean analytics dashboard to monitor video performance and engagement")

# demo dataset (kept realistic for portfolio use)
video_data = {
    "Video Title": [
        "Python Tutorial",
        "Data Science Project",
        "Machine Learning Basics",
        "Streamlit Dashboard",
        "Portfolio Tips",
        "Pandas Full Course",
        "AI Mini Project"
    ],
    "Views": [12000, 18000, 9500, 22000, 15000, 17500, 13200],
    "Likes": [800, 1200, 650, 1700, 980, 1100, 870],
    "Comments": [120, 180, 90, 250, 140, 165, 130],
    "CTR": [4.2, 5.1, 3.8, 6.0, 4.7, 5.5, 4.1],
    "Upload Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
}

df = pd.DataFrame(video_data)

# sidebar filter
st.sidebar.header("🎯 Filter by Upload Day")
chosen_days = st.sidebar.multiselect(
    "Pick days",
    options=df["Upload Day"].unique(),
    default=df["Upload Day"].unique()
)

filtered_df = df[df["Upload Day"].isin(chosen_days)]

# top metrics section
metric1, metric2, metric3, metric4 = st.columns(4)
metric1.metric("👀 Total Views", f"{filtered_df['Views'].sum():,}")
metric2.metric("👍 Total Likes", f"{filtered_df['Likes'].sum():,}")
metric3.metric("💬 Total Comments", f"{filtered_df['Comments'].sum():,}")
metric4.metric("🎯 Average CTR", f"{filtered_df['CTR'].mean():.1f}%")

# first row charts
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("📈 Top Performing Videos")
    views_chart = px.bar(
        filtered_df,
        x="Video Title",
        y="Views",
        text="Views",
        template="plotly_dark"
    )
    views_chart.update_layout(height=420)
    st.plotly_chart(views_chart, use_container_width=True)

with right_chart:
    st.subheader("📉 Likes Trend")
    likes_chart = px.line(
        filtered_df,
        x="Video Title",
        y="Likes",
        markers=True,
        template="plotly_dark"
    )
    likes_chart.update_layout(height=420)
    st.plotly_chart(likes_chart, use_container_width=True)

# second row
bottom_left, bottom_right = st.columns(2)

with bottom_left:
    st.subheader("🥧 Comment Share")
    comment_chart = px.pie(
        filtered_df,
        names="Video Title",
        values="Comments",
        template="plotly_dark"
    )
    comment_chart.update_layout(height=420)
    st.plotly_chart(comment_chart, use_container_width=True)

with bottom_right:
    st.subheader("📋 Detailed Performance Data")
    st.dataframe(filtered_df, width="stretch")
