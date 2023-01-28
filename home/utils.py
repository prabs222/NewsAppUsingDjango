import requests
from .models import *
def get_articles_from_api(url):
    try:
        print("test cron")
        data = requests.get(url)
        data = data.json()
        if data.get('articles'):
            for article in data.get('articles'):
                print (article)
                source = article.get('source').get('name')
                author = article.get('author')
                title = article.get('title')
                description = article.get('description')
                url = article.get('url')
                image_url = article.get('urlToImage')
                content = article.get('content')
                created_at = article.get('publishedAt')
                if Article.objects.filter(source = source, author = author, title = title, description = description, url = url, image_url = image_url,content = content, created_at = created_at):
                    continue
                Article.objects.create(source = source, author = author, title = title, description = description, url = url, image_url = image_url,content = content, created_at = created_at)
    except Exception as e:
        print(e)