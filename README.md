# 🎬 IMDB TV Shows Explorer

An interactive data application built using the **Preswald SDK**, designed to explore the IMDb Top 5000 TV Shows dataset through real-time filters, SQL-like queries, and visualizations.

## 📌 Project Overview
This project demonstrates the ability to:
- Work with real-world datasets
- Perform data cleaning and SQL-like queries
- Build minimal user-facing data-driven UIs
- Utilize SDKs to develop analytical applications

## 🗃️ Dataset
- **Source**: IMDb Top 5000 TV Shows
- **Format**: CSV
- **Fields**: Title, Genre, Rating, Votes, Runtime, Release Year
- **Path**: `data/imdb_top_5000_tv_shows.csv`

## 🧰 Technologies & SDK
- **Language**: Python 3.8+
- **SDK**: Preswald
- **Configuration**:  
  - `preswald.toml` – project settings and dataset config  
  - `pyproject.toml` – build and dependency management  

## 🖥️ Features
| Component    | Description                                       |
|--------------|---------------------------------------------------|
| `text()`     | Static text headers and titles                    |
| `table()`    | Render tabular data views                         |
| `slider()`   | Adjust filter thresholds dynamically              |
| `query()`    | Execute SQL-style queries behind the scenes       |
| `plotly()`   | Display visual data trends                        |

## 📊 Visualization
- **Type**: Scatter Plot (via Plotly)
- **X-axis**: Release Year
- **Y-axis**: IMDb Rating
- **Color**: Genre
- **Purpose**: Explore how ratings vary over time and genre



