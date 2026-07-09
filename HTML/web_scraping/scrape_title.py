from bs4 import BeautifulSoup

with open("cats.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

title = soup.find("title")
heading = soup.find("h1")

print("Page title:", title.text)
print("Main heading:", heading.text)