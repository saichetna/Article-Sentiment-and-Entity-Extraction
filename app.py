from flask import Flask, render_template, request
from scraping import scrape_article
from entity_extraction import extract_entities
from sentiment_analysis import analyze_sentiment
from db import store_article_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        
        # Scrape the article content
        content = scrape_article(url)
        if not content:
            return render_template('error.html', message="Error scraping article. Please check the URL and try again.")

        # Extract entities
        entities = extract_entities(content)

        # Analyze sentiment
        sentiment = analyze_sentiment(content)

        # Store the result in the database
        store_article_data(url, content, entities, sentiment)

        return render_template('result.html', url=url, sentiment=sentiment, entities=entities)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
