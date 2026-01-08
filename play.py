import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("IMDB TV Shows Analysis")

@st.cache_data
def load_and_prep_data():
    try:
        df = pd.read_csv("imdb_top_250_series_episode_ratings(1).csv")
        df = df[['season', 'episode', 'aggregateRating', 'title']]
        df.columns = ['season', 'episode', 'rating', 'title']
        return df
    except FileNotFoundError:
        return None

df = load_and_prep_data()

if df is not None:
    df = df[df['season'] != 'Unknown']
    df['season'] = pd.to_numeric(df['season'])
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Line Chart (Trends)", "Histogram (Distributions)", "Boxplot (Variability)", "Raw Data"])
    
    st.sidebar.markdown("---") 

    st.sidebar.header("Filter Options")
    
    season_counts = df.groupby('title')['season'].nunique()
    min_seasons = st.sidebar.slider("Minimum number of seasons", 1, 20, 5)
    
    long_running_shows = season_counts[season_counts >= min_seasons].index
    main_df = df[df['title'].isin(long_running_shows)]

    all_titles = sorted(main_df['title'].unique())
    selected_shows = st.sidebar.multiselect("Select shows to compare", all_titles, default=all_titles[:3])

    if selected_shows:
        plot_data = main_df[main_df['title'].isin(selected_shows)]
    else:
        plot_data = main_df

    if page == "Line Chart (Trends)":
        st.header("Rating Trends over Seasons")
        st.caption("How do ratings change as a show gets older?")
        
        fig, ax = plt.subplots(figsize=(10, 5))
        avg_ratings = plot_data.groupby(['title', 'season'])['rating'].mean().reset_index()
        
        if len(selected_shows) > 0:
            sns.lineplot(data=avg_ratings, x='season', y='rating', hue='title', marker='o', ax=ax)
        else:
            sns.lineplot(data=avg_ratings, x='season', y='rating', ax=ax, errorbar=None)
            st.info("Showing aggregate trend. Select specific shows in the sidebar for details.")

        ax.set_title("Average Rating per Season")
        ax.set_xlabel("Season")
        ax.set_ylabel("Rating")
        ax.grid(True)
        st.pyplot(fig)

    elif page == "Histogram (Distributions)":
        st.header("Rating Distributions")
        st.caption("How common are high or low ratings?")
        
        fig, ax = plt.subplots(figsize=(10, 5))
        use_hue = 'title' if 0 < len(selected_shows) < 5 else None
        
        sns.histplot(data=plot_data, x='rating', bins=20, kde=True, ax=ax, hue=use_hue)
        
        ax.set_title("Distribution of Episode Ratings")
        ax.set_xlabel("Rating")
        st.pyplot(fig)
        st.info("The curve (KDE) represents the probability density of the ratings.")
    elif page == "Boxplot (Variability)":
        st.header("Season-wise Variability")
        st.caption("Which seasons were consistent? Which had the best/worst outliers?")
        
        fig, ax = plt.subplots(figsize=(12, 6))
        use_hue = 'title' if 0 < len(selected_shows) < 3 else None
        
        sns.boxplot(data=plot_data, x='season', y='rating', ax=ax, hue=use_hue)
        
        ax.set_title("Rating Spread by Season")
        ax.set_xlabel("Season")
        ax.set_ylabel("Episode Rating")
        st.pyplot(fig)
        st.info("Dots represent outlier episodes that were significantly better or worse than the season average.")

    elif page == "Raw Data":
        st.header("Raw Dataset")
        st.caption(f"Showing data for {len(plot_data['title'].unique())} shows.")
        st.dataframe(plot_data)

else:
    st.error("Data file not found. Please place 'imdb_top_250_series_episode_ratings(1).csv' in the same folder.")