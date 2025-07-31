from flask import Flask, request, render_template
from recommend import recommend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('movie.html')

# @app.route('/list')
# def list():
#     return render_template('list.html')

@app.route('/recommend', methods=['POST'])
def recommend_route():
    movie = request.form['movie']
    results = recommend(movie)
    return render_template('list.html', movie=movie, recommendations=results)

if __name__ == '__main__':
    app.run(debug=True)

