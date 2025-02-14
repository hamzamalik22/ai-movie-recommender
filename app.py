# import streamlit as st 
# import pandas as pd 
# # import numpy as np 
# from sklearn.feature_extraction.text import TfidfVectorizer 
# from sklearn.metrics.pairwise import cosine_similarity 
# import ast 

# # Load and process the TMDB dataset 
# @st.cache_data 
# def load_data(): 
#     movies = pd.read_csv('tmdb_5000_movies.csv') 
#     credits = pd.read_csv('tmdb_5000_credits.csv') 
    
#     movies = movies.merge(credits, on='title') 
#     features = ['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew', 'vote_average', 'vote_count'] 
#     movies = movies[features] 
    
#     def convert_ast(obj): 
#         try: 
#             return [item['name'] for item in ast.literal_eval(obj)] 
#         except: 
#             return [] 
    
#     movies['genres'] = movies['genres'].apply(convert_ast) 
#     movies['keywords'] = movies['keywords'].apply(convert_ast) 
    
#     def get_director(crew): 
#         try: 
#             directors = [item['name'] for item in ast.literal_eval(crew) if item['job'] == 'Director'] 
#             return directors[0] if directors else '' 
#         except: 
#             return '' 
    
#     movies['director'] = movies['crew'].apply(get_director) 
    
#     def get_top_cast(cast): 
#         try: 
#             cast_list = ast.literal_eval(cast) 
#             return [item['name'] for item in cast_list[:3]] 
#         except: 
#             return [] 
    
#     movies['cast'] = movies['cast'].apply(get_top_cast) 
#     movies['overview'] = movies['overview'].fillna('') 
    
#     def combine_features(row): 
#         genres = ' '.join(row['genres']) if row['genres'] else '' 
#         keywords = ' '.join(row['keywords']) if row['keywords'] else '' 
#         cast = ' '.join(row['cast']) if row['cast'] else '' 
#         director = row['director'] if row['director'] else '' 
#         overview = row['overview'] if row['overview'] else '' 
        
#         return f"{genres} {keywords} {cast} {director} {overview}".strip() 
    
#     movies['combined_features'] = movies.apply(combine_features, axis=1) 
    
#     return movies 

# @st.cache_resource 
# def calculate_similarity(movies_data): 
#     tfidf = TfidfVectorizer(stop_words='english') 
#     tfidf_matrix = tfidf.fit_transform(movies_data['combined_features']) 
#     return cosine_similarity(tfidf_matrix, tfidf_matrix) 

# def get_recommendations(title, movies_data, cosine_sim): 
#     idx = movies_data[movies_data['title'] == title].index[0] 
#     sim_scores = list(enumerate(cosine_sim[idx])) 
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) 
#     sim_scores = sim_scores[1:11] 
#     movie_indices = [i[0] for i in sim_scores] 
    
#     recommendations = movies_data.iloc[movie_indices][['title', 'genres', 'vote_average', 'overview', 'cast', 'director']] 
#     similarity_scores = [i[1] for i in sim_scores] 
#     return recommendations, similarity_scores 

# st.set_page_config(page_title="Movie Recommender Pro", page_icon="🎬", layout="wide") 

# # Custom CSS for professional styling 
# st.markdown(""" 
#     <style> 
#     body { 
#         background-color: #121212; 
#         color: #ffffff; 
#         font-family: 'Arial', sans-serif; 
#     } 
#     .movie-card { 
#         padding: 20px; 
#         border-radius: 12px; 
#         margin-bottom: 20px; 
#         background: linear-gradient(135deg, #1E1E1E, #252525); 
#         box-shadow: 0px 10px 30px rgba(255, 255, 255, 0.1); 
#         transition: transform 0.3s ease-in-out; 
#     } 
#     .movie-card:hover { 
#         transform: scale(1.02); 
#     } 
#     .metric-container { 
#         display: flex; 
#         justify-content: space-between; 
#         font-size: 14px; 
#         color: #cccccc; 
#     } 
#     h3 { 
#         color: #FFD700; 
#     } 
#     button { 
#         background-color: #ff4500 !important; 
#         color: white !important; 
#         border-radius: 8px !important; 
#     } 
#     </style> 
# """, unsafe_allow_html=True) 

# st.title("🎬 Advanced Movie Recommendation System") 
# st.write("Using TMDB 5000 Movie Dataset") 

# try: 
#     with st.spinner("Loading movie database..."): 
#         movies_df = load_data() 
#         similarity_matrix = calculate_similarity(movies_df) 
    
#     selected_movie = st.selectbox("Choose a movie you like:", movies_df['title'].values, index=0) 
    
#     if st.button("Get Recommendations"): 
#         with st.spinner("Finding similar movies..."): 
#             recommendations, similarity_scores = get_recommendations(selected_movie, movies_df, similarity_matrix) 
            
#             st.subheader(f"Top Movie Recommendations Based on '{selected_movie}'") 
            
#             for idx, (_, movie) in enumerate(recommendations.iterrows()): 
#                 score = similarity_scores[idx] 
#                 genres = ', '.join(movie['genres']) if isinstance(movie['genres'], list) else str(movie['genres']) 
#                 cast = ', '.join(movie['cast']) if isinstance(movie['cast'], list) else str(movie['cast']) 
                
#                 st.markdown(f""" 
#                 <div class="movie-card"> 
#                     <h3>{movie['title']}</h3> 
#                     <div class="metric-container"> 
#                         <span>Similarity Score: {score:.2%}</span> 
#                         <span>Rating: {movie['vote_average']}/10</span> 
#                     </div> 
#                     <p><strong>Genres:</strong> {genres}</p> 
#                     <p><strong>Director:</strong> {movie['director']}</p> 
#                     <p><strong>Cast:</strong> {cast}</p> 
#                     <p><strong>Overview:</strong> {movie['overview']}</p> 
#                 </div> 
#                 """, unsafe_allow_html=True) 
    
#     with st.expander("ℹ️ About this Recommender System"): 
#         st.markdown(""" 
#         This advanced movie recommender uses the TMDB 5000 Movie Dataset and considers: 
#         - Movie genres 
#         - Keywords and themes 
#         - Cast and director 
#         - Plot overview 
#         - User ratings 
        
#         The system uses TF-IDF vectorization and cosine similarity to find movies that are most similar to your selection. 
        
#         Dataset source: [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata) 
#         """) 
# except FileNotFoundError: 
#     st.error("Dataset files not found! Ensure 'tmdb_5000_movies.csv' and 'tmdb_5000_credits.csv' are present.")


import streamlit as st 
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
import ast 

# [Previous data loading and processing functions remain the same]
@st.cache_data 
def load_data(): 
    # [Previous load_data code remains unchanged]
    movies = pd.read_csv('tmdb_5000_movies.csv') 
    credits = pd.read_csv('tmdb_5000_credits.csv') 
    
    movies = movies.merge(credits, on='title') 
    features = ['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew', 'vote_average', 'vote_count'] 
    movies = movies[features] 
    
    def convert_ast(obj): 
        try: 
            return [item['name'] for item in ast.literal_eval(obj)] 
        except: 
            return [] 
    
    movies['genres'] = movies['genres'].apply(convert_ast) 
    movies['keywords'] = movies['keywords'].apply(convert_ast) 
    
    def get_director(crew): 
        try: 
            directors = [item['name'] for item in ast.literal_eval(crew) if item['job'] == 'Director'] 
            return directors[0] if directors else '' 
        except: 
            return '' 
    
    movies['director'] = movies['crew'].apply(get_director) 
    
    def get_top_cast(cast): 
        try: 
            cast_list = ast.literal_eval(cast) 
            return [item['name'] for item in cast_list[:3]] 
        except: 
            return [] 
    
    movies['cast'] = movies['cast'].apply(get_top_cast) 
    movies['overview'] = movies['overview'].fillna('') 
    
    def combine_features(row): 
        return f"{' '.join(row['genres'])} {' '.join(row['keywords'])} {' '.join(row['cast'])} {row['director']} {row['overview']}".strip() 
    
    movies['combined_features'] = movies.apply(combine_features, axis=1) 
    return movies 

@st.cache_resource 
def calculate_similarity(movies_data): 
    tfidf = TfidfVectorizer(stop_words='english') 
    tfidf_matrix = tfidf.fit_transform(movies_data['combined_features']) 
    return cosine_similarity(tfidf_matrix, tfidf_matrix) 

def get_recommendations(title, movies_data, cosine_sim): 
    idx = movies_data[movies_data['title'] == title].index[0] 
    sim_scores = list(enumerate(cosine_sim[idx])) 
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) 
    sim_scores = sim_scores[1:11] 
    movie_indices = [i[0] for i in sim_scores] 
    recommendations = movies_data.iloc[movie_indices][['title', 'genres', 'vote_average', 'overview', 'cast', 'director']] 
    similarity_scores = [i[1] for i in sim_scores] 
    return recommendations, similarity_scores 

# Configure Streamlit page
st.set_page_config(
    page_title="Movie Recommender Pro",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Dark Theme CSS
st.markdown("""
    <style>
    /* Dark theme colors */
    :root {
        --bg-color: #121212;
        --card-bg: #1E1E1E;
        --card-hover: #252525;
        --primary: #BB86FC;
        --accent: #03DAC6;
        --error: #CF6679;
        --text-primary: #FFFFFF;
        --text-secondary: #B3B3B3;
    }

    /* Global styles */
    .stApp {
        background-color: var(--bg-color);
    }

    .stTextInput>div>div>input {
        background-color: var(--card-bg);
        color: var(--text-primary);
    }

    /* Header styling */
    .app-header {
        background: linear-gradient(180deg, rgba(187, 134, 252, 0.2) 0%, var(--bg-color) 100%);
        padding: 2rem;
        border-radius: 0 0 24px 24px;
        margin-bottom: 2rem;
        text-align: center;
    }

    .app-title {
        color: var(--primary);
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        font-family: 'SF Pro Display', system-ui, -apple-system;
    }

    /* Movie card styling */
    .movie-card {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        background: var(--card-hover);
        border-color: var(--primary);
    }

    .movie-title {
        color: var(--primary);
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .movie-meta {
        display: flex;
        gap: 1rem;
        color: var(--text-secondary);
        margin-bottom: 1rem;
        font-size: 0.9rem;
    }

    .similarity-bar {
        width: 100%;
        height: 4px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 2px;
        margin: 1rem 0;
        overflow: hidden;
    }

    .similarity-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--primary), var(--accent));
        border-radius: 2px;
        transition: width 0.5s ease;
    }

    .genre-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 1rem;
    }

    .genre-tag {
        background: rgba(187, 134, 252, 0.1);
        color: var(--primary);
        padding: 0.3rem 0.8rem;
        border-radius: 12px;
        font-size: 0.8rem;
        border: 1px solid rgba(187, 134, 252, 0.2);
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, var(--primary), var(--accent));
        color: black;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 25px;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(187, 134, 252, 0.3);
    }

    /* Selectbox styling */
    .stSelectbox>div>div {
        background-color: var(--card-bg);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: var(--text-primary);
    }

    /* Grid layout for recommendations */
    .recommendations-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 1.5rem;
        padding: 1rem;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .recommendations-grid {
            grid-template-columns: 1fr;
        }
        
        .app-title {
            font-size: 2rem;
        }
    }

    /* Loading animation */
    .stSpinner {
        border-color: var(--primary);
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("""
    <div class="app-header">
        <div class="app-title">🎬 Movie Recommender Pro</div>
        <p style="color: var(--text-secondary); font-size: 1.1rem;">
            Discover your next favorite movie using advanced AI
        </p>
    </div>
""", unsafe_allow_html=True)

# Main content
try:
    with st.spinner("Loading movie database..."): 
        movies_df = load_data() 
        similarity_matrix = calculate_similarity(movies_df) 
    
    # Search interface
    col1, col2 = st.columns([3, 1])
    with col1:
        selected_movie = st.selectbox(
            "Select a movie you enjoy:",
            movies_df['title'].values,
            index=0
        )
    with col2:
        search_button = st.button("🔍 Find Similar Movies")
    
    if search_button:
        with st.spinner("Finding perfect matches..."): 
            recommendations, similarity_scores = get_recommendations(selected_movie, movies_df, similarity_matrix) 
            
            st.markdown("""
                <div style="text-align: center; margin: 2rem 0;">
                    <h2 style="color: var(--text-primary);">Recommended Movies</h2>
                </div>
            """, unsafe_allow_html=True)
            
            # Create recommendation grid
            st.markdown('<div class="recommendations-grid">', unsafe_allow_html=True)
            
            for idx, (_, movie) in enumerate(recommendations.iterrows()): 
                score = similarity_scores[idx] 
                genres = movie['genres'] if isinstance(movie['genres'], list) else []
                cast = ', '.join(movie['cast']) if isinstance(movie['cast'], list) else str(movie['cast'])
                
                st.markdown(f"""
                    <div class="movie-card">
                        <div class="movie-title">{movie['title']}</div>
                        <div class="movie-meta">
                            <span>⭐ {movie['vote_average']:.1f}</span>
                            <span>🎬 {movie['director']}</span>
                        </div>
                        <div class="similarity-bar">
                            <div class="similarity-fill" style="width: {int(score * 100)}%"></div>
                        </div>
                        <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                            Match Score: {score:.0%}
                        </p>
                        <p style="color: var(--text-primary); margin-bottom: 1rem;">
                            {movie['overview'][:500]}...
                        </p>
                        <div class="genre-tags">
                            {' '.join([f'<span class="genre-tag">{genre}</span>' for genre in genres[:3]])}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # About section with dark theme styling
    with st.expander("ℹ️ About this Recommender"):
        st.markdown("""
            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
                <h3 style="color: var(--primary); margin-bottom: 1rem;">How it Works</h3>
                <p style="color: var(--text-secondary);">
                    This recommender uses advanced machine learning to analyze multiple aspects of movies:
                </p>
                <ul style="color: var(--text-secondary);">
                    <li>Genre patterns and themes</li>
                    <li>Cast and crew information</li>
                    <li>Plot elements and keywords</li>
                    <li>User ratings and popularity</li>
                </ul>
                <p style="color: var(--text-secondary); margin-top: 1rem;">
                    Data: TMDB 5000 Movie Dataset
                </p>
            </div>
        """, unsafe_allow_html=True)

except FileNotFoundError:
    st.error("⚠️ Dataset files not found! Please ensure the required CSV files are present.")