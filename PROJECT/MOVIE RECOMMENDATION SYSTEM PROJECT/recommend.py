import requests
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV
movies = pd.read_csv('datamodel/movies.csv')

# Fill missing values
features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in features:
    movies[feature] = movies[feature].fillna('')

# Combine features into one string
movies['combine'] = movies['genres'] + ' ' + movies['keywords'] + ' ' + movies['tagline'] + ' ' + movies['cast'] + ' ' + movies['director']

# Generate TF-IDF vectors and similarity matrix
cv = TfidfVectorizer()
vectors = cv.fit_transform(movies['combine'])
similarity = cosine_similarity(vectors)

# Replace with your actual OMDb API key
OMDB_API_KEY = ''


def fetch_omdb_data(title):
    """Fetch poster and rating from OMDb API."""
    url = f'http://www.omdbapi.com/?t={requests.utils.quote(title)}&apikey={OMDB_API_KEY}'
    try:
        response = requests.get(url)
        data = response.json()
        poster = data.get('Poster') if data.get('Poster') and data.get('Poster') != 'N/A' else '/static/default_poster.jpg'
        rating = data.get('imdbRating') if data.get('imdbRating') and data.get('imdbRating') != 'N/A' else 'Not Rated'
        return poster, rating
    except Exception as e:
        print(f"Error fetching OMDb data for {title}: {e}")
        return '/static/default_poster.jpg', 'Not Rated'

def recommend(movie_name):
    titles = movies['title'].tolist()
    matches = difflib.get_close_matches(movie_name, titles)

    if not matches:
        return [{
            'name': "No match found",
            'overview': "N/A",
            'cast': "N/A",
            'poster': '/static/default_poster.jpg',
            'rating': 'N/A'
        }]

    match = matches[0]
    index = movies[movies['title'] == match].index[0]
    similarity_scores = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in similarity_scores[1:10]:  # Top 9 matches (excluding itself)
        movie_data = movies.iloc[i[0]]
        poster, rating = fetch_omdb_data(movie_data['title'])
        recommendations.append({
            'name': movie_data['title'],
            'overview': movie_data['overview'],
            'cast': movie_data['cast'],
            'poster': poster,
            'rating': rating
        })

    return recommendations
