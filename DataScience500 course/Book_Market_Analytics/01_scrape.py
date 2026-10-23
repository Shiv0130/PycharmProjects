# Data Science 500 - Book Market Analytics
# Lab 1: Web scraping with BeautifulSoup (study guide Chapter 7)
# Run in PyCharm: right-click -> Run
# Output: books_raw.csv
# NOTE: books_raw.csv is already in this folder (1000 books).
#       Only re-run if you need a fresh scrape (about 10-15 minutes).

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
HEADERS = {"User-Agent": "Student project for Data Science 500"}
DELAY = 0.5
TOTAL_PAGES = 50


def get_soup(url):
    # download page HTML and parse it
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        response.encoding = "utf-8"
        return BeautifulSoup(response.text, "lxml")
    except requests.RequestException as error:
        print("Could not get", url, "-", error)
        return None


def parse_listing_page(soup, page_url):
    # each product card on the listing page
    books = []
    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        in_stock = book.find("p", class_="instock").text.strip()
        link = urljoin(page_url, book.h3.a["href"])
        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": in_stock,
            "url": link,
        })
    return books


def parse_book_page(soup):
    # detail page: genre, stock text, description, UPC
    crumbs = soup.find("ul", class_="breadcrumb").find_all("li")
    category = crumbs[2].text.strip()
    stock_text = soup.find("p", class_="instock").text.strip()

    description_heading = soup.find("div", id="product_description")
    if description_heading is not None:
        description = description_heading.find_next_sibling("p").text.strip()
    else:
        description = None

    upc = None
    for row in soup.find("table", class_="table-striped").find_all("tr"):
        if row.th.text == "UPC":
            upc = row.td.text

    return {
        "category": category,
        "stock_text": stock_text,
        "description": description,
        "upc": upc,
    }


def main():
    all_books = []

    # listing pages
    for page_number in range(1, TOTAL_PAGES + 1):
        if page_number == 1:
            page_url = BASE_URL + "index.html"
        else:
            page_url = BASE_URL + "catalogue/page-" + str(page_number) + ".html"

        soup = get_soup(page_url)
        if soup is not None:
            all_books.extend(parse_listing_page(soup, page_url))

        print("Page", page_number, "done - total books:", len(all_books))
        time.sleep(DELAY)

    # each book page
    for number, book in enumerate(all_books, start=1):
        soup = get_soup(book["url"])
        if soup is not None:
            book.update(parse_book_page(soup))
        if number % 100 == 0:
            print(number, "of", len(all_books), "book pages done")
        time.sleep(DELAY)

    # save
    raw_books = pd.DataFrame(all_books)
    raw_books.to_csv("books_raw.csv", index=False)

    print("Shape:", raw_books.shape)
    print("Books collected:", len(raw_books))
    print("Enough for assignment (>=200):", len(raw_books) >= 200)
    print(raw_books.isnull().sum())
    print("Saved books_raw.csv")


if __name__ == "__main__":
    main()
