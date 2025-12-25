Cinema Recommender 
Revitalizing Rural Cinema through Data Analysis & Machine Learning
Context
This project answers a business need for "Les Toiles de la Creuse," a cinema in rural France facing declining attendance. 
The goal is to modernize their offering by building a recommendation engine tailored specifically to their unique local demographic.
The Challenge:
Cold Start: No historical user data is available.
Specific Audience: The target demographic is 45+, rural, and heavily prefers French-language content (VF).
Technical Constraint: Must process massive datasets (IMDb/TMDB) on limited resources.
Objectives
Market Research: Define the "Persona" of the local moviegoer using INSEE/CNC data.
Data Engineering: Process and filter the 7M+ row IMDb dataset using memory-efficient techniques (chunking).
Machine Learning: Build a Content-Based Filtering system (Scikit-Learn) to solve the Cold Start problem.
Application: Deploy a "testable" tool using Streamlit for the client to explore KPIs and test recommendations.
Key Insights (Market Research)
Demographics: The region is underpopulated with an aging population (>50% are over 45).
Preferences: Strong bias towards French Cinema (Drama/Comedy) and dubbed content (VF).
Strategy: The recommendation algorithm prioritizes French content and genres favored by families and seniors, while not aggressively penalizing older films (1980-2000).
Tech Stack
Language: Python
Data Processing: Pandas (Chunking strategy), NumPy
Machine Learning: Scikit-Learn (NearestNeighbors, CosineSimilarity, CountVectorizer).
Visualization: Matplotlib, Seaborn
App Interface: Streamlit
