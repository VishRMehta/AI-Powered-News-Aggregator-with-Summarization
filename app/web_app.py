from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
import re
import csv
from fetch_articles import fetch_articles

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

# Regex for basic URL validation
URL_REGEX = re.compile(r'^(http|https)://')

def load_valid_domains():
    valid_domains = []
    with open('valid_domains.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            valid_domains.append(row[0].strip())  # Add each domain to the set
    return valid_domains


def load_summarized_articles():
    with open('summarized_articles.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    articles = load_summarized_articles()
    valid_domains = load_valid_domains() 
    return render_template('index.html', articles=articles, valid_domains=json.dumps(valid_domains))

@app.route('/scrape-articles', methods=['POST'])
def scrape_articles():
    # Get URLs from the form
    urls_input = request.form.get('urls', '')
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]
    
    # Validate URLs
    valid_urls = [url for url in urls if re.match(URL_REGEX, url)]
    
    if not valid_urls:
        # If no valid URLs are provided, use the default set
        # valid_urls = ['https://cnn.com', 'https://bbc.com', 'https://techcrunch.com', 'https://www.bloomberg.com/uk', 'https://www.cnbc.com/world/?region=worldpyt']
        return redirect(url_for('index'))
    
    # Fetch articles from the URLs
    articles = fetch_articles(valid_urls)

    # Save the articles to a JSON file
    with open('articles.json', 'w') as f:
        json.dump(articles, f, indent=4)
    
    # Categorize and summarize the articles
    from categorize_articles import categorize_articles
    from summarize_articles import summarize_articles
    
    categorized_articles = categorize_articles(articles)
    summarized_articles = summarize_articles(categorized_articles)
    
    with open('summarized_articles.json', 'w') as f:
        json.dump(summarized_articles, f, indent=4)
    
    # Redirect back to the homepage to display the new articles
    return redirect(url_for('index'))

@app.route('/api/articles')
def api_articles():
    articles = load_summarized_articles()
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
