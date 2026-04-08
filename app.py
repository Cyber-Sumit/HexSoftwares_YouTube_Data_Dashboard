import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="YouTube Data Dashboard", layout="wide")

st.title("📊 YouTube Data Dashboard with Streamlit")
st.write("Analyze YouTube video performance using interactive charts and filters")

df = pd.DataFrame({
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
    "Upload Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
})

st.sidebar.header("🎯 Filter Dashboard")
selected_day = st.sidebar.multiselect(
    "Select Upload Day",
    options=df["Upload Day"].unique(),
    default=df["Upload Day"].unique()
)

filtered_df = df[df["Upload Day"].isin(selected_day)]

st.subheader("📌 Key Performance Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Views", f"{filtered_df['Views'].sum():,}")
col2.metric("Total Likes", f"{filtered_df['Likes'].sum():,}")
col3.metric("Total Comments", f"{filtered_df['Comments'].sum():,}")

st.subheader("📋 Video Performance Table")
st.dataframe(filtered_df, width="stretch")

st.subheader("📈 Views Per Video")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(filtered_df["Video Title"], filtered_df["Views"])
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("📉 Likes Trend")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(filtered_df["Video Title"], filtered_df["Likes"], marker="o")
plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("🥧 Comments Distribution")
fig3, ax3 = plt.subplots(figsize=(6, 6))
ax3.pie(
    filtered_df["Comments"],
    labels=filtered_df["Video Title"],
    autopct="%1.1f%%"
)
st.pyplot(fig3)