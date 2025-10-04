# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 1. Load the data
df = pd.read_csv("data/metadata.csv")

# 2. Basic Exploration
print("Shape:", df.shape)
print(df.info())
print("Missing values:\n", df.isnull().sum())

# 3. Data Cleaning
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# Drop rows without titles or publication date
df = df.dropna(subset=['title', 'publish_time'])

# 4. Analysis & Visualization

# a) Publications by year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.savefig("publications_by_year.png")
plt.show()

# b) Top 10 Journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.savefig("top_journals.png")
plt.show()

# c) Word Cloud of Paper Titles
titles = " ".join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Frequent Words in Paper Titles")
plt.savefig("wordcloud_titles.png")
plt.show()

# d) Distribution by Source
source_counts = df['source_x'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=source_counts.values, y=source_counts.index, palette="coolwarm")
plt.title("Top Sources of COVID-19 Research Papers")
plt.xlabel("Number of Papers")
plt.ylabel("Source")
plt.savefig("source_distribution.png")
plt.show()
