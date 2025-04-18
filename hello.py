# ----------------------------------------
# Load the dataset
# ----------------------------------------
from preswald import connect, get_df
connect()
df = get_df("imdb_top_5000_tv_shows_csv")

# ----------------------------------------
# SQL-style static query: Most Voted + High Rating
# ----------------------------------------
from preswald import query, table, text

sql = """
SELECT primaryTitle, averageRating, numVotes
FROM imdb_top_5000_tv_shows_csv
ORDER BY numVotes DESC, averageRating DESC
LIMIT 20
"""
filtered_df = query(sql, "imdb_top_5000_tv_shows_csv")

text("# 🎬 IMDB TV Shows Explorer")
text("## 📌 SQL Query: Most Voted & Highly Rated Shows")
table(filtered_df.head(20), title="📋 Top Shows (Sorted by Votes & Ratings)")

# ----------------------------------------
# Clean the data
# ----------------------------------------
import pandas as pd
df = df.dropna(subset=['averageRating', 'numVotes', 'primaryTitle', 'startYear', 'genres'])
df['averageRating'] = pd.to_numeric(df['averageRating'], errors='coerce')
df['numVotes'] = pd.to_numeric(df['numVotes'], errors='coerce')
df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')
df = df[(df['averageRating'] >= 1) & (df['startYear'] >= 1900)]

# ----------------------------------------
# Dynamic filter with slider
# ----------------------------------------
from preswald import slider

threshold = slider("🎚️ Minimum Number of Votes", min_val=0, max_val=5000000, default=100000)
filtered_by_slider = df[df["numVotes"] > threshold]
filtered_by_slider = filtered_by_slider.sort_values(by=["averageRating", "numVotes"], ascending=[False, False]).head(10)

text("## 🔧 Dynamic Top 10 Shows Based on Vote Threshold")
text(f"Shows with more than {threshold} votes, ranked by rating and popularity.")

table(
    filtered_by_slider[['primaryTitle', 'averageRating', 'numVotes', 'genres']],
    title="🌟 Top 10 Shows by Rating (Live Filter)"
)

# ----------------------------------------
# 📈 Chart: Rating Trends of Most Repeated Shows
# ----------------------------------------
import plotly.express as px
from preswald import plotly

text("## 📈 Rating Trends of Top 10 Most Repeated Series")

top_repeated_titles = df['primaryTitle'].value_counts().head(10).index.tolist()
df_repeated = df[df['primaryTitle'].isin(top_repeated_titles)]
df_repeated = df_repeated.sort_values(by=['primaryTitle', 'startYear'])

fig_trend = px.line(
    df_repeated,
    x='startYear',
    y='averageRating',
    color='primaryTitle',
    markers=True,
    title="📊 IMDB Rating Trends Over Years – Top 10 Repeated Series",
    labels={'startYear': 'Year', 'averageRating': 'IMDB Rating'}
)

fig_trend.update_layout(
    template='plotly_white',
    title_font_size=20,
    legend_title="TV Show"
)

plotly(fig_trend)
