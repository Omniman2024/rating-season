#### rating-season
# Exploratory Data Analysis : possible effect on show ratings with progressing seasons

This project performs an exploratory data analysis (EDA) on IMDB's top TV series episode ratings dataset. It studies how TV series ratings evolve across seasons and investigates potential trends in episode counts, rating distributions, and show longevity.

---

##  Dataset

**File:** `imdb_top_250_series_episode_ratings(1).csv`

This dataset is available in kaggle - https://www.kaggle.com/datasets/wittmannf/episode-ratings-from-imdb-top-250-tv-series

---

##  Analysis Performed

- **Grouping by Season Counts:**
  - Created groups:
    - `5 Seasons`
    - `6 Seasons`
    - `7 Seasons`
    - `8-11 Seasons`
    - `12-41 Seasons`

- **Visualizations:**
  - **Line plots:** Season vs. Average Rating for individual shows.
  - **Grouped line plots:** Shows with similar season counts plotted together.
  - **Boxplots:** Distribution of ratings by `Episode_Group` (based on number of episodes).
  - **Histograms:** Number of seasons distribution across shows.
  - **Correlation analysis:** Between season number and rating.

---

## Key Insights

- TV shows often start with higher ratings in their early seasons.
- Many long-running shows (8+ seasons) show gradual decline in ratings over time.
- Shows with 5–7 seasons tend to maintain relatively stable ratings with mild fluctuations.
- A moderate negative correlation (~-0.5) was observed between season number and average rating for multi-season shows.

---

## Technologies Used

- **Python 3 (Jupyter Notebook)**
- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Matplotlib** and **Seaborn** for data visualization

---


