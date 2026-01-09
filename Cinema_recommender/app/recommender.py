import streamlit as st
import pandas as pd
import pickle
import os
import requests

# 1. CONFIGURATION & STYLE 
st.set_page_config(page_title="Les Toiles de la Creuse", page_icon="🍿", layout="centered")

# Custom CSS for a cinematic look
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    div[data-testid="stExpander"] { background-color: #262730; border-radius: 10px; }
    h1 { color: #E50914; text-align: center; font-family: 'Helvetica Neue', sans-serif; }
    h3 { color: #f5c518; }
    </style>
""", unsafe_allow_html=True)

# 2. DATA LOADING
@st.cache_resource
def load_data():
    app_folder = os.path.dirname(os.path.abspath(__file__))
    try:
        movies = pickle.load(open(os.path.join(app_folder, 'movie_list.pkl'), 'rb'))
        cosine_sim = pickle.load(open(os.path.join(app_folder, 'count_matrix.pkl'), 'rb'))
        model_knn = pickle.load(open(os.path.join(app_folder, 'knn_model.pkl'), 'rb'))
        return movies, cosine_sim, model_knn
    except FileNotFoundError:
        return None, None, None

movies, count_matrix, model_knn = load_data()

# 4. THE APP UI 
if movies is not None:
    
    # Header
    st.title("🍿 Les Toiles de la Creuse")
    st.markdown("<h4 style='text-align: center; color: gray;'>Vos films à portée de main</h4>", unsafe_allow_html=True)
    st.divider()

    # Search Bar (Centered)
    col_spacer_l, col_search, col_spacer_r = st.columns([1, 2, 1])
    with col_search:
        movie_titles = movies['primaryTitle'].values
        selected_movie = st.selectbox("🔍 Taper votre film préféré:", movie_titles, index=None)

    # Logic
    if selected_movie:
        st.divider()
        try:
            # Get Index & Neighbors
            idx = movies[movies['primaryTitle'] == selected_movie].index[0]
            distances, indices = model_knn.kneighbors(count_matrix[idx], n_neighbors=6)
            
            # Display Recommendations
            st.subheader(f"Because you watched '{selected_movie}'...")
            
            # Create a 5-column layout
            cols = st.columns(5)
            
            # Loop through the 5 neighbors (skipping the first one which is the input movie)
            for i, col in enumerate(cols):
                if i + 1 < len(indices[0]):
                    neighbor_idx = indices[0][i+1]
                    row = movies.iloc[neighbor_idx]
                    
                    with col:
                        # 1. Fetch Poster
                        poster_url = movies['poster_url'].iloc[neighbor_idx]
                
                        st.image(poster_url, use_container_width=True)
                        
                        # 2. Movie Details
                        safe_title = row['title'] if row['title'] else row['primaryTitle']
                        st.markdown(f"**{safe_title}**")
                        
                        # 3. Metadata Badge
                        st.caption(f"⭐ {row['averageRating']} | 📅 {row['year']}")
                        
                        # 4. Expandable Plot/Details (Optional)
                        with st.expander("Details"):
                            st.write(f"🎭 {row['genres']}")
                            st.write(f"🎬 {row['director_name']}")

        except IndexError:
            st.error("Movie not found in database.")

else:
    st.error("❌ Data files not found. Please ensure .pkl files are in the 'app' folder.")