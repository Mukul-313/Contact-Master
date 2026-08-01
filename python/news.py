import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-10&sortBy=publishedAt&apiKey=c66e16cddb4d4d3c8b6e70d3b9d22619"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")