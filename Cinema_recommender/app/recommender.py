import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import os

# 1) PAGE CONFIGURATION
st.set_page_config(
    page_title="Les Toiles de la Creuse",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2) LOAD DATA & MODELS (Cached for performance) 
@st.cache_resource
def load_data():
    # Use os.path.join for safety across Mac/Windows
    data_path = "" 
    
    # If running locally from the 'app' folder, adjust path
    if not os.path.exists(data_path):
        data_path = 'data' 

    try:
        movies = pickle.load(open(os.path.join(data_path, 'movie_list.pkl'), 'rb'))
        cosine_sim = pickle.load(open(os.path.join(data_path, 'count_matrix.pkl'), 'rb'))
        model_knn = pickle.load(open(os.path.join(data_path, 'knn_model.pkl'), 'rb'))
        return movies, cosine_sim, model_knn
    except FileNotFoundError:
        st.error("❌ Error: Pickle files not found. Run Notebook 03 first!")
        return None, None, None

df_movies, count_matrix, model_knn = load_data()

if df_movies is not None:
    
    # --- 3. SIDEBAR FILTERS (Global) ---
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2503/2503508.png", width=100)
    st.sidebar.title("Cinema Controls")
    
    # Year Filter
    min_year = int(df_movies['year'].min())
    max_year = int(df_movies['year'].max())
    year_range = st.sidebar.slider("📅 Release Year", min_year, max_year, (1980, 2020))
    
    # Language Filter (The "Creuse" Requirement)
    languages = st.sidebar.multiselect("🗣️ Language", df_movies['detected_language'].unique(), default=['fr'])

    # Apply Filters to the Dataframe (for Dashboard only)
    filtered_df = df_movies[
        (df_movies['year'] >= year_range[0]) & 
        (df_movies['year'] <= year_range[1])
    ]
    if languages:
        filtered_df = filtered_df[filtered_df['detected_language'].isin(languages)]

    # --- 4. TABS UI ---
    tab1, tab2 = st.tabs(["📊 Market Dashboard", "🤖 Movie Recommender"])

    # ==========================
    # TAB 1: DASHBOARD
    # ==========================
    with tab1:
        st.header("📈 Market Analysis: La Creuse")
        
        # KPIs
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Catalog Size", f"{filtered_df.shape[0]:,}")
        col2.metric("Avg Rating", f"{filtered_df['averageRating'].mean():.1f} ⭐")
        col3.metric("French Content", f"{(filtered_df['detected_language']=='fr').sum()} Movies")
        col4.metric("Avg Runtime", f"{int(filtered_df['runtimeMinutes'].replace('',0).astype(float).mean())} min")
        
        st.divider()

        # Visualizations
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("🎭 Top Genres (Selection)")
            # We assume 'genres' is a string like "Comedy,Drama". We split for counting.
            # Explode logic for chart
            df_genres = filtered_df.assign(genres=filtered_df['genres'].str.split(',')).explode('genres')
            top_genres = df_genres['genres'].value_counts().head(10)
            
            fig_genre = px.bar(
                x=top_genres.values, 
                y=top_genres.index, 
                orientation='h',
                labels={'x': 'Count', 'y': 'Genre'},
                color=top_genres.values,
                color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig_genre, use_container_width=True)

        with c2:
            st.subheader("📅 Content Era Distribution")
            fig_year = px.histogram(filtered_df, x='year', nbins=20, color_discrete_sequence=['#F1C40F'])
            fig_year.add_vrect(x0=1990, x1=2010, annotation_text="Target Audience Era", annotation_position="top left", fillcolor="green", opacity=0.1)
            st.plotly_chart(fig_year, use_container_width=True)

    # ==========================
    # TAB 2: RECOMMENDER
    # ==========================
    with tab2:
        st.header("🍿 The Recommendation Engine")
        st.markdown("Select a movie to find similar films for your local audience.")

        # 1. Search Box
        # Create a list of titles for the dropdown
        movie_titles = df_movies['primaryTitle'].values
        selected_movie = st.selectbox("Type or Select a Movie:", movie_titles, index=None, placeholder="Ex: Anatomy of a Fall")

        if selected_movie:
            # 2. Find the Index
            try:
                # Get index of the selected movie
                idx = df_movies[df_movies['primaryTitle'] == selected_movie].index[0]
                
                # 3. Run the "Brain" (Nearest Neighbors)
                # We ask for 6 neighbors because the first one is always the movie itself
                distances, indices = model_knn.kneighbors(count_matrix[idx], n_neighbors=6)
                
                # 4. Display Results
                st.success(f"Because you watched **{selected_movie}**, we recommend:")
                
                cols = st.columns(5)
                # Skip the first result (index 0) because it's the input movie itself
                for i, col in enumerate(cols):
                    if i + 1 < len(indices[0]):
                        movie_idx = indices[0][i+1] # Get the neighbor index
                        row = df_movies.iloc[movie_idx]
                        
                        with col:
                            # Display Title
                            st.markdown(f"**{row['primaryTitle']}**")
                            # Display French Title if different
                            if row['title'] != row['primaryTitle']:
                                st.caption(f"🇫🇷 {row['title']}")
                            
                            # Display Metadata
                            st.text(f"⭐ {row['averageRating']}")
                            st.text(f"📅 {row['year']}")
                            st.text(f"🎭 {row['genres']}")
                            
                            # Poster Placeholder (Optional: Add TMDB logic here if you have links)
                            st.image("https://via.placeholder.com/150x225?text=No+Poster", use_container_width=True)

            except IndexError:
                st.error("Movie not found in the database.")