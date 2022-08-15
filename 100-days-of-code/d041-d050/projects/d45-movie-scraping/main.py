from bs4 import BeautifulSoup
import requests

# response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
# print(soup.prettify())

# all_info = [text.getText() for text in soup.find_all(name="h3")]

ranking = [rank.getText().split()[0] for rank in soup.find_all(name="h3")]
titles = [title.getText().split()[1:] for title in soup.find_all(name="h3")]

ranking = [int(rank.replace(")", "").replace(":", "")) for rank in ranking]
titles = [" ".join(title) for title in titles]

print(ranking)
print(titles)

ranking.reverse()
titles.reverse()

print(ranking)
print(titles)

with open("movies.txt", mode='a', encoding="utf-8") as file:
    for i in range(len(ranking)):
        file.write(f"{ranking[i]}) {titles[i]}\n")