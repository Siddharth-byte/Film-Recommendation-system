#  Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on user input.  
The system uses cosine similarity on precomputed movie feature vectors and displays movie posters using the TMDB API.

**Live Demo**: https://film-recommendation-system-aik4gmgamwnorkasece56l.streamlit.app/

---

# Features
- Search for a movie by name
- Get **Top 5 similar movies**
- Displays:
  - Movie title
  - Movie poster (fetched in real-time)
- Fast recommendations using precomputed similarity matrix
- Clean and interactive UI built with Streamlit

---

# Working
1. Movie metadata is vectorized using content-based features
2. Cosine similarity is computed between movies
3. A similarity matrix is stored for fast lookup
4. When a user selects a movie:
   - The system finds the most similar movies
   - Fetches posters using TMDB API
   - Displays results instantly

---

# Tools
- **Python**
- **Pandas, NumPy**
- **Scikit-learn** (Cosine Similarity)
- **Streamlit** (Frontend + Deployment)
- **TMDB API** (Movie posters & metadata)
- **Pickle** (Model persistence)

---

# Project Structure
Film-Recommendation-System/
│
├── app.py
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
# Deployment
The application is deployed using **Streamlit Cloud**, enabling instant access without backend setup.

---

# Notes
- Large similarity matrix is precomputed to ensure fast recommendations
- TMDB API key is used to fetch movie posters dynamically
- API key can be stored securely using Streamlit secrets

---

# Future Improvements
- Add fuzzy search for misspelled movie names
- Support genre-based filtering
- Hybrid recommendation (content + collaborative)
- Replace pickle with optimized storage (FAISS / ANN)

---

# Author
**Siddharth Tyagi**  
M.Tech CSE | Machine Learning | Systems & Data  
