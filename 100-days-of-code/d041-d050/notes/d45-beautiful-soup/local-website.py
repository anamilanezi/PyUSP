from bs4 import BeautifulSoup

with open(file="website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
# print(soup.prettify())

# Using a tag that occurs more than once will return the first occurance
print(soup.p)

# Getting all occurances
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

form_tag = soup.find("input")
max_length = form_tag.get("maxlength")

# Getting a tag using id/class
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.text)

# Using CSS selectors:
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)

