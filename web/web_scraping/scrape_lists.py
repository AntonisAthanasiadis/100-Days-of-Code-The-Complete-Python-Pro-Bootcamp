from bs4 import BeautifulSoup

with open("cats.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

items = soup.find_all("li")

print("Reasons people love cats:")

for i, item in enumerate(items, start=1):
    print(f"{i}. {item.text}")