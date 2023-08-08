from bs4 import BeautifulSoup
import requests
import pprint

response = requests.get("https://news.ycombinator.com/")

articles_data = {}

soup = BeautifulSoup(response.text, 'html.parser')

# Get all of the news
all_news = soup.find_all(name="tr", class_="athing")


for news in all_news:
    # Find the id
    news_id = news.get("id")
    
    # Find the title and link
    title = news.find_all(name="td")[2]
    link = title.find(name="a").get("href")
    title = title.find(name="a").text

    # Find the score
    score = soup.find(name="span", id=f"score_{news_id}")

    # Add to the Dictionary
    if score:
        score = score.getText().split()[0]
        articles_data[title] = [news_id, link, int(score)]

print(articles_data)

