import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability", "Rating"])

    for page in range(1, 51):
        url = base_url.format(page)
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()
            rating = book.find("p")["class"][1]
            writer.writerow([title, price, availability, rating])

print("Done. All book data saved to books.csv")
