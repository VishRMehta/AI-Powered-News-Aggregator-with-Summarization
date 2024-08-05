import newspaper
import json
import concurrent.futures
import requests
from fake_useragent import UserAgent

ua = UserAgent()

def fetch_articles_from_source(url, max_articles=10):
    config = newspaper.Config()
    config.browser_user_agent = ua.random  # Set a random user agent for each request
    config.memoize_articles = False
    paper = newspaper.build(url, config=config)
    articles = []
    for i, article in enumerate(paper.articles):
        if i >= max_articles:
            break
        try:
            article.download()
            article.parse()
            articles.append({
                'title': article.title,
                'text': article.text,
                'url': article.url
            })
        except Exception as e:
            print(f"Error fetching article from {url}: {e}")
    return articles

def fetch_articles(sources, max_articles_per_source=10):
    all_articles = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(fetch_articles_from_source, url, max_articles_per_source): url for url in sources}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                articles = future.result()
                all_articles.extend(articles)
                print(f"Fetched {len(articles)} articles from {url}")
            except Exception as e:
                print(f"Error fetching articles from {url}: {e}")
    return all_articles

if __name__ == "__main__":
    sources = ['https://cnn.com', 'https://bbc.com', 'https://techcrunch.com']
    all_articles = fetch_articles(sources)
    with open('articles.json', 'w') as f:
        json.dump(all_articles, f, indent=4)
    print(f"Total articles fetched: {len(all_articles)}")
