from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import numpy as np
import json

nltk.download('punkt')

def summarize(text, n=3):
    sentences = sent_tokenize(text)
    if len(sentences) <= n:
        return text
    
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(sentences)
    scores = X.sum(axis=1).A1
    
    ranked_sentences = [sentences[i] for i in np.argsort(scores)[-n:]]
    return ' '.join(ranked_sentences)

def summarize_articles(articles):
    for article in articles:
        article['summary'] = summarize(article['text'])
    return articles

if __name__ == "__main__":
    with open('categorized_articles.json', 'r') as f:
        articles = json.load(f)
    summarized_articles = summarize_articles(articles)
    with open('summarized_articles.json', 'w') as f:
        json.dump(summarized_articles, f, indent=4)
