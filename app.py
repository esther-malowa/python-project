# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv("data/metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("📊 CORD-19 Research Data Explorer")
st.write("Explore COVID-19 research papers interactively.")

# 2. Filter by year
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range:", min_year, max_year, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# 3. Visualization: Publications by Year
st.subheader("📅 Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color='skyblue')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)

# 4. Visualization: Top Journals
st.subheader("🏛️ Top 10 Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax, palette="viridis")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

# 5. Show sample data
st.subheader("📄 Sample Data")
st.dataframe(filtered_df[['title', 'authors', 'journal', 'publish_time']].head(10))
