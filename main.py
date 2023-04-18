from flask import Flask, request, jsonify
import csv

all_movies = []

with open('movies.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watched_movies = []

app = Flask(__name__)
@app.route('/get-movie')

def get_movie():
    return jsonify({
        'data' : all_movies[0],
        'status' : 'success'
    })

@app.route('/liked-movie', methods=['POST'])

def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movie.append(movie)
    return jsonify({
        'status' : 'success'
    })

@app.route('/not-liked-movie', methods=['POST'])

def not_liked_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movies)
    return jsonify({
        'status' : 'success'
    })

@app.route('/did-not-watched-movie', methods=['POST'])

def did_not_watched_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watched_movies.append(movies)
    return jsonify({
        'status' : 'success'
    })

if __name__ == '__main__':
    app.run()