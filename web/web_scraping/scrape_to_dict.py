from bs4 import BeautifulSoup

with open("cats.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

data = {
    "title": soup.title.text,
    "heading": soup.h1.text,
    "description": soup.find("p").text,
    "reasons": [li.text for li in soup.find_all("li")]
}

print(data)