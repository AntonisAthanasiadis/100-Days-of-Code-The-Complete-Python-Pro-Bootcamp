from bs4 import BeautifulSoup

with open("cats.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

for link in soup.find_all("a"):
    print("Text:", link.text)
    print("URL:", link["href"])