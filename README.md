# Automated News Summarization and Categorization Tool

This project is a comprehensive solution for summarizing and categorizing news articles from various online sources. It employs advanced NLP and machine learning techniques to streamline news content, making it more accessible and easier to analyze.

![SS1](https://github.com/VishRMehta/AI-Powered-News-Aggregator-with-Summarization/blob/master/Project_Thumbnail.png)

---

## Features

**Article Extraction:** Fetches articles from major news websites.

**Text Summarization:** Provides concise summaries using TF-IDF.

**Article Categorization:** Groups articles into topics using KMeans clustering.

**Concurrent Processing:** Handles multiple news sources efficiently.

## Technologies

**Python**: Programming language used.

**Newspaper3k**: Library for extracting and parsing news articles.

**scikit-learn**: For TF-IDF vectorization and KMeans clustering.

**NLTK**: For sentence tokenization.

**JSON**: For data storage and interchange.


## Installation
---
**Clone the Repository:**

```bash
git clone https://github.com/yourusername/news-summarization.git
cd news-summarization
```

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

##Usage

**Run the Article Fetcher:**

```bash
python fetch_articles.py
```

**Summarize and Categorize Articles:**

```bash
python categorize_articles.py
python summarize_articles.py
```

**View Results:**

```bash
python web_app.py
```

Summarized articles will be saved in summarized_articles.json.
Categorized articles will be available in categorized_articles.json.

---

## How It Works

### Fetching Articles:

Uses Newspaper3k to extract articles from specified news sources.
Handles basic anti-scraping mechanisms by using varied user agents.

### Summarization:

Splits text into sentences.
Calculates TF-IDF scores to rank sentences.
Selects top n sentences to create a summary.

### Categorization:

Transforms text data into TF-IDF vectors.
Applies KMeans clustering to categorize articles into topics.

### Handling Paywalls:

The tool uses a rotating user-agent strategy to bypass basic paywalls. It simulates different browser requests to avoid detection and scraping restrictions.
