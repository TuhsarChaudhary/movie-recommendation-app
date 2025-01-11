import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for local development

with open('movies.json') as f:
    movie_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_movie():
    data = request.json
    genre = data.get('genre')
    duration = data.get('duration')
    mood = data.get('mood')
    
    movie_recommendation = generate_recommendation(genre, duration, mood)
    
    return jsonify({"recommendation": movie_recommendation})

def generate_recommendation(genre, duration, mood):
    for movie in movie_data['movies']:
        if movie['genre'] == genre and movie['duration'] == duration and movie['mood'] == mood:
            return f"""
            <div style="text-align: center;">
                <img src="{movie['poster']}" alt="{movie['title']} Poster" style="width: 200px; height: auto; border-radius: 8px;">
                <h2 style="color: #ff4d4d;">{movie['title']}</h2>
                <p>Year: {movie['year']} | Director: {movie['director']} | IMDb Rating: {movie['rating']}</p>
                <p>{movie['description']}</p>
                <p>{movie['extra']}</p>
            </div>
            """
    return "<p>No recommendation found</p>"

if __name__ == '__main__':
    app.run(debug=True)
