#### rating-season
# Exploratory Data Analysis along with an Interactive Dashboard 

This project performs an exploratory data analysis (EDA) on IMDB's top TV series episode ratings dataset and shows the relationships via an interactive dashboard. It studies how TV series ratings evolve across seasons and investigates potential trends in episode counts, rating distributions, and show longevity.

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
## Interactive Dashboard

You can explore the data interactively using the built-in Streamlit app.

### 1. Running Locally

To run the dashboard on your local machine, follow these steps:

**Prerequisites:**
Ensure you have Python installed. You will need to install the required libraries.

```bash
pip install streamlit pandas matplotlib seaborn
```
Run the App: Navigate to the project directory in your terminal and run the following command:
```Bash

streamlit run play.py
```

   A local web server will start, and the dashboard should open automatically in your default browser at http://localhost:8501.
   
   ### 2. Deployment
   
   This app is ready to be deployed to the Streamlit Community Cloud (or other hosting services like Heroku/Render).

Steps to Deploy on Streamlit Cloud:
- Push your code to GitHub: Ensure your project (including the python script and the .csv dataset) is in a public GitHub repository.
- Add a requirements file: Create a file named requirements.txt in your repository containing the necessary libraries:
    Plaintext
    streamlit
    pandas
    matplotlib
    seaborn
- Sign up/Login: Go to share.streamlit.io and log in with your GitHub account.
- Deploy:
    Click "New app".
    Select your repository, branch, and the main file path (e.g., app.py).
    Click "Deploy".
Your app will be live and accessible via a public URL!
---
## URL
URL for the website I created - https://rating-season-bwahpwwjo9ala2g5bcblyd.streamlit.app/

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
- **Streamlit** for web dashboard

---
## Project Structure

Here is an overview of the file organization for this project:

```text
rating-season/
│
├── imdb_top_250_series_episode_ratings(1).csv        # The dataset file
├── play.py                                           # Main Streamlit application script
├── IMDB shows.ipynb                                  # Jupyter Notebook containing the EDA code
├── requirements.txt                                  # List of dependencies for deployment
└── README.md                                         # Project documentation and instructions
```
---
