import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example of extracting the article content
        content = soup.find('article') or soup.find('body')
        
        if content and content.text.strip():
            return content.text.strip()
        else:
            raise ValueError("No article content found")
            
    except Exception as e:
        print(f"Error scraping article: {e}")
        return None
