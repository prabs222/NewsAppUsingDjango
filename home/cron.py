from .models import Article
from .utils import get_articles_from_api

def fetch_articles():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=7eccae8242104011931a11270ce896b9'    
    get_articles_from_api(url)
    
    