import streamlit as st
import pickle
import requests
from pathlib import Path
import numpy as np

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")

# ================== PATHS ==================
BASE_DIR = Path(__file__).resolve().parent
MOVIE_PATH = BASE_DIR /  "movies_list.pkl"
SIM_PATH = BASE_DIR / "similarity_topk.pkl"

# ================== LOAD DATA ==================
@st.cache_data
def load_movies():
    with open(MOVIE_PATH, "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_similarity():
    with open(SIM_PATH, "rb") as f:
        return pickle.load(f)  # (topk_indices, topk_scores)

movies = load_movies()
topk_indices, topk_scores = load_similarity()

# ================== TMDB POSTER ==================
def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

# ================== RECOMMENDATION ==================
def recommend(movie_title):
    idx = movies[movies["title"] == movie_title].index[0]

    indices = topk_indices[idx]
    scores = topk_scores[idx]

    # sort by similarity score
    order = np.argsort(scores)[::-1]

    # skip itself, take top 5
    movie_idxs = indices[order][1:6]

    names = []
    posters = []

    for i in movie_idxs:
        names.append(movies.iloc[i].title)
        posters.append(fetch_poster(movies.iloc[i].movie_id))

    return names, posters

# ================== UI ==================
movie_name = st.text_input("🔍 Enter a movie name")

if st.button("Search"):
    if movie_name not in movies["title"].values:
        st.error("❌ Movie not found. Please check spelling.")
    else:
        names, posters = recommend(movie_name)

        cols = st.columns(5)
        for col, name, poster in zip(cols, names, posters):
            with col:
                if poster:
                    st.image(poster)
                st.caption(name)
