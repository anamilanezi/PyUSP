from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article_tag = soup.find(name="a", class_="titlelink")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()

# print(article_text)
# print(article_link)
# print(article_upvote)

articles = soup.find_all(name="a", class_="titlelink")

article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

# Getting only the number of votes and turning into int
# article_upvotes = [int(upvotes.getText().split()[0]) for upvotes in soup.find_all(name="span", class_="score")]

# This will not work if there are no upvotes (a new article was just posted for example).
# So, you need to go to the higher level and pull a bigger section then test for the "score" field in that section.
article_upvotes = []
upvotes = soup.find_all(name="td", class_="subtext")
for article in upvotes:
    has_votes = article.find(name="span", class_="score")
    if has_votes is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(has_votes.string.split()[0]))

print(article_texts)
print(article_links)
print(article_upvotes)

# Checking if the list are equal:
print(len(article_texts))
print(len(article_links))
print(len(article_upvotes))

# This works if all lists are equal:
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

