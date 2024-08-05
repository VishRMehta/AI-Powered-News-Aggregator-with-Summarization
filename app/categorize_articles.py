from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import json

def load_articles():
    with open('articles.json', 'r') as f:
        return json.load(f)

def categorize_articles(articles, num_clusters=5):
    texts = [article['text'] for article in articles]
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(X)
    
    categories = kmeans.labels_
    for i, article in enumerate(articles):
        article['category'] = int(categories[i])
    return articles

if __name__ == "__main__":
    articles = load_articles()
    categorized_articles = categorize_articles(articles)
    with open('categorized_articles.json', 'w') as f:
        json.dump(categorized_articles, f, indent=4)
    print(f"Categorized {len(categorized_articles)} articles")
