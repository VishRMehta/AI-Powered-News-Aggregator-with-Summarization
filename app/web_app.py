from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

def load_summarized_articles():
    with open('summarized_articles.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    articles = load_summarized_articles()
    return render_template('index.html', articles=articles)

@app.route('/api/articles')
def api_articles():
    articles = load_summarized_articles()
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
