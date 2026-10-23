# ============================================================
# DATA SCIENCE 500 - Book Market Analytics (Books to Scrape)
# Student number: 402308101
# PyCharm project - single pipeline (lecturer confirmed .py is fine)
#
# Rubric order:
#   PART A  Data Acquisition (BeautifulSoup)
#   PART B  Data Cleaning & Preparation
#   PART C  Data Visualisation & Exploration
#   PART D  Predictive Modelling (Linear Regression)
#
# Style: short comments like practical / CA labs
#        PART blocks like MLAssignment600 (same lecturer)
# ============================================================

import os
import time
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# working folder = this script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("charts", exist_ok=True)

# ------------------------------------------------------------
# Shared settings
# ------------------------------------------------------------
BASE_URL = "https://books.toscrape.com/"
HEADERS = {"User-Agent": "Student project for Data Science 500"}
DELAY = 0.5
TOTAL_PAGES = 50   # full catalogue = 50 pages x 20 books


def save_fig(name):
    # save chart then show it
    plt.tight_layout()
    plt.savefig("charts/" + name + ".png", dpi=150, bbox_inches="tight")
    plt.show()


# ============================================================
# PART A - Data Acquisition (Web Scraping)
# Assignment: BeautifulSoup, title, price, rating word, stock
#             at least ~100 books (we take the full catalogue)
# ============================================================
print("=" * 60)
print("PART A - Data Acquisition")
print("=" * 60)


def get_soup(url):
    # download a page and parse HTML
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        response.encoding = "utf-8"
        return BeautifulSoup(response.text, "lxml")
    except requests.RequestException as error:
        print("Could not get", url, "-", error)
        return None


def parse_listing_page(soup, page_url):
    # one catalogue page: title, price, star word, stock, link
    books = []
    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]  # One..Five
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
    # detail page: genre, full stock text, description, UPC
    crumbs = soup.find("ul", class_="breadcrumb").find_all("li")
    category = crumbs[2].text.strip()
    stock_text = soup.find("p", class_="instock").text.strip()

    description_heading = soup.find("div", id="product_description")
    if description_heading is not None:
        description = description_heading.find_next_sibling("p").text.strip()
    else:
        description = None

    upc = None
    table = soup.find("table", class_="table-striped")
    if table is not None:
        for row in table.find_all("tr"):
            if row.th is not None and row.th.text == "UPC":
                upc = row.td.text

    return {
        "category": category,
        "stock_text": stock_text,
        "description": description,
        "upc": upc,
    }


# Use existing books_raw.csv if present (faster for marking)
if os.path.exists("books_raw.csv"):
    print("books_raw.csv found - loading saved scrape (skip live scrape)")
    raw = pd.read_csv("books_raw.csv")
else:
    print("No books_raw.csv - scraping full catalogue (about 10-15 min)")
    all_books = []

    for page_number in range(1, TOTAL_PAGES + 1):
        if page_number == 1:
            page_url = BASE_URL + "index.html"
        else:
            page_url = BASE_URL + "catalogue/page-" + str(page_number) + ".html"

        soup = get_soup(page_url)
        if soup is not None:
            all_books.extend(parse_listing_page(soup, page_url))

        print("Page", page_number, "done - total books so far:", len(all_books))
        time.sleep(DELAY)

    for number, book in enumerate(all_books, start=1):
        soup = get_soup(book["url"])
        if soup is not None:
            book.update(parse_book_page(soup))
        if number % 100 == 0:
            print(number, "of", len(all_books), "detail pages done")
        time.sleep(DELAY)

    raw = pd.DataFrame(all_books)
    raw.to_csv("books_raw.csv", index=False)
    print("Saved books_raw.csv")

print("Shape (rows, columns):", raw.shape)
print("Books collected:", len(raw))
print("Enough for assignment (>=100):", len(raw) >= 100)
print("Missing values per column:")
print(raw.isnull().sum())
print("\nRating counts:")
print(raw["rating"].value_counts())
if "category" in raw.columns:
    print("Number of genres:", raw["category"].nunique())


# ============================================================
# PART B - Data Cleaning & Preparation
# ============================================================
print("\n" + "=" * 60)
print("PART B - Data Cleaning & Preparation")
print("=" * 60)

books = raw.copy()
print("Rows before cleaning:", len(books))

# drop rows missing category or stock text from detail page
books = books.dropna(subset=["category", "stock_text"])
print("Rows after dropna:", len(books))

# price text "£51.77" -> float
books["price_gbp"] = books["price"].str.replace("£", "", regex=False).astype(float)

# rating word -> number 1-5
rating_numbers = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
books["rating_num"] = books["rating"].map(rating_numbers)
print("Ratings not converted:", books["rating_num"].isnull().sum())


def get_quantity(stock_text):
    # "In stock (22 available)" -> 22
    if isinstance(stock_text, str) and "(" in stock_text:
        return int(stock_text.split("(")[1].split(" ")[0])
    return 0


books["stock_qty"] = books["stock_text"].apply(get_quantity)

# tidy category labels
books["category"] = books["category"].str.strip()
books["category"] = books["category"].replace({
    "Default": "Uncategorised",
    "Add a comment": "Uncategorised",
})

# title / description features for the model
books["title"] = books["title"].str.strip()
books["description"] = books["description"].fillna("")
books["description_clean"] = books["description"].str.lower().str.strip()
books["title_length"] = books["title"].str.len()
books["title_words"] = books["title"].str.split().str.len()
books["description_length"] = books["description_clean"].str.len()
books["description_words"] = books["description_clean"].str.split().str.len()

# cleaning checks (rubric)
print("No missing values:", books.isnull().sum().sum() == 0)
print("Prices > 0:", (books["price_gbp"] > 0).all())
print("Ratings 1-5:", books["rating_num"].between(1, 5).all())
print("Stock >= 0:", (books["stock_qty"] >= 0).all())
print("Enough books (>=100):", len(books) >= 100)

final_columns = [
    "title", "category", "price_gbp", "rating", "rating_num",
    "stock_qty", "title_length", "title_words",
    "description_length", "description_words",
    "description_clean", "upc", "url",
]
books_clean = books[final_columns].reset_index(drop=True)
books_clean.to_csv("books_clean.csv", index=False)

print("Final shape:", books_clean.shape)
print(books_clean.head())
print("Saved books_clean.csv")
print("\nNumeric summary:")
print(books_clean[["price_gbp", "rating_num", "stock_qty",
                   "title_length", "description_length"]].describe())


# ============================================================
# PART C - Data Visualisation & Exploration
# Study guide Ch 4: hist, bar, scatter, labels, grid
# ============================================================
print("\n" + "=" * 60)
print("PART C - Data Visualisation & Exploration")
print("=" * 60)

# C1 - price distribution
prices = books_clean["price_gbp"]
average_price = prices.mean()
plt.figure(figsize=(10, 5))
plt.hist(prices, bins=10, color="steelblue", edgecolor="black")
plt.axvline(average_price, color="red", linestyle="--", linewidth=1.5)
plt.xlabel("Price (GBP)")
plt.ylabel("Number of books")
plt.title("Book prices from about 10 to 60 GBP")
plt.grid(True, axis="y", linestyle="--", alpha=0.4)
save_fig("1_price_distribution")
print("Insight: prices spread fairly evenly; average is about GBP", round(average_price, 2))

# C2 - rating vs count and mean price
by_rating = books_clean.groupby("rating_num")["price_gbp"].agg(["count", "mean"])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(by_rating.index, by_rating["count"], color="steelblue")
ax1.set_xlabel("Star rating")
ax1.set_ylabel("Number of books")
ax1.set_title("Books per star rating")
ax1.grid(True, axis="y", linestyle="--", alpha=0.4)
ax2.bar(by_rating.index, by_rating["mean"], color="steelblue")
ax2.set_xlabel("Star rating")
ax2.set_ylabel("Average price (GBP)")
ax2.set_title("Average price barely changes by rating")
ax2.grid(True, axis="y", linestyle="--", alpha=0.4)
save_fig("2_rating")
print("Insight: star rating does not clearly go with price")

# C3 - genre average price (genres with at least 20 books)
genre_stats = books_clean.groupby("category")["price_gbp"].agg(["count", "mean"])
genre_stats = genre_stats[genre_stats["count"] >= 20].sort_values("mean")
plt.figure(figsize=(10, 7))
plt.barh(genre_stats.index, genre_stats["mean"], color="steelblue")
plt.xlabel("Average price (GBP)")
plt.title("Average price by genre (genres with 20+ books)")
plt.grid(True, axis="x", linestyle="--", alpha=0.4)
save_fig("3_genres")
print("Insight: genre shows the biggest average difference, but it is still small")

# C4 - stock levels
stock_counts = books_clean["stock_qty"].value_counts().sort_index()
plt.figure(figsize=(10, 5))
plt.bar(stock_counts.index, stock_counts.values, color="steelblue")
plt.xlabel("Copies in stock")
plt.ylabel("Number of books")
plt.title("Stock levels bunch at certain numbers")
plt.grid(True, axis="y", linestyle="--", alpha=0.4)
save_fig("4_stock")

# C5 - scatter price vs each numeric feature
features = ["rating_num", "stock_qty", "title_length", "description_length"]
labels = ["Star rating", "Copies in stock", "Title length", "Description length"]
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, col, label in zip(axes, features, labels):
    ax.scatter(books_clean[col], books_clean["price_gbp"],
               alpha=0.3, s=18, color="steelblue")
    coef = np.polyfit(books_clean[col], books_clean["price_gbp"], 1)
    x_line = np.linspace(books_clean[col].min(), books_clean[col].max(), 50)
    ax.plot(x_line, coef[0] * x_line + coef[1], "--", color="orange")
    ax.set_xlabel(label)
    ax.set_ylabel("Price (GBP)")
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
fig.suptitle("Price against each feature")
save_fig("5_scatter")
print("Insight: scatter plots are almost flat - weak links to price")

# C6 - correlation with price
number_columns = [
    "price_gbp", "rating_num", "stock_qty", "title_length",
    "title_words", "description_length", "description_words",
]
correlations = books_clean[number_columns].corr()
print("\nCorrelation matrix:")
print(correlations.round(2))

price_links = correlations["price_gbp"].drop("price_gbp")
names = [
    "Star rating", "Copies in stock", "Title length", "Title words",
    "Description length", "Description words",
]
plt.figure(figsize=(10, 5))
plt.barh(names, price_links.values, color="steelblue", height=0.5)
plt.axvline(0, color="black", linewidth=1)
plt.xlim(-1, 1)
plt.xlabel("Correlation with price (-1 to 1)")
plt.title("Every feature is almost uncorrelated with price")
plt.grid(True, axis="x", linestyle="--", alpha=0.4)
save_fig("6_correlation")
print("Insight: strongest |correlation| with price is near 0 - features do not explain price")


# ============================================================
# PART D - Predictive Modelling (Linear Regression)
# Predict price_gbp from listing features
# ============================================================
print("\n" + "=" * 60)
print("PART D - Predictive Modelling (Linear Regression)")
print("=" * 60)

# D1 - features (justified: only numeric listing fields we scraped)
feature_cols = ["rating_num", "stock_qty", "title_length", "description_length"]
X = books_clean[feature_cols]
y = books_clean["price_gbp"]

print("Predictors (X):", feature_cols)
print("Response (y): price_gbp")

# D2 - 80/20 train-test split (same pattern as ML600)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print("Train shape:", X_train.shape)
print("Test shape :", X_test.shape)

# D3 - fit linear regression
linreg = LinearRegression()
linreg.fit(X_train, y_train)

print("Intercept (Beta 0):", round(linreg.intercept_, 2))
coefficients = pd.DataFrame({
    "feature": feature_cols,
    "coefficient": linreg.coef_.round(4),
})
print(coefficients)

train_predictions = linreg.predict(X_train)
test_predictions = linreg.predict(X_test)
train_residuals = y_train - train_predictions
test_residuals = y_test - test_predictions

# D4 - evaluation: MAE vs always guessing the mean
guess = y_train.mean()
print("Simple guess (train mean): GBP", round(guess, 2))

train_mae_guess = (y_train - guess).abs().mean()
test_mae_guess = (y_test - guess).abs().mean()
train_mae_model = train_residuals.abs().mean()
test_mae_model = test_residuals.abs().mean()

results = pd.DataFrame({
    "Average error on training books (GBP)": [train_mae_guess, train_mae_model],
    "Average error on test books (GBP)": [test_mae_guess, test_mae_model],
}, index=["Always guess the average", "Linear regression"])
print(results.round(2))

model_squared = (test_residuals ** 2).sum()
guess_squared = ((y_test - guess) ** 2).sum()
print(
    "Model squared errors as a share of the guess:",
    str(round(model_squared / guess_squared * 100, 1)) + "%",
)

# D5 - actual vs predicted chart
plt.figure(figsize=(8, 7))
plt.scatter(test_predictions, y_test, alpha=0.5, s=30, color="steelblue")
plt.plot([10, 60], [10, 60], "--", color="black", linewidth=1.5)
plt.xlim(10, 60)
plt.ylim(10, 60)
plt.xlabel("Predicted price (GBP)")
plt.ylabel("Real price (GBP)")
plt.title("Predicted prices barely move, real prices do")
plt.grid(True, linestyle="--", alpha=0.4)
save_fig("7_actual_vs_predicted")

# D6 - error comparison chart
names_err = ["Always guess\nthe average", "Linear\nregression"]
errors = [test_mae_guess, test_mae_model]
plt.figure(figsize=(8, 5))
bars = plt.bar(names_err, errors, color=["lightgrey", "steelblue"], width=0.5)
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.3,
        "GBP " + str(round(bar.get_height(), 2)),
        ha="center",
    )
plt.ylim(0, 16)
plt.ylabel("Average error on test books (GBP)")
plt.title("The model is no more accurate than guessing")
plt.grid(True, axis="y", linestyle="--", alpha=0.4)
save_fig("8_error_comparison")

# D7 - example prediction
new_books = pd.DataFrame({
    "rating_num": [1, 5],
    "stock_qty": [10, 10],
    "title_length": [30, 30],
    "description_length": [1400, 1400],
})
predicted_prices = linreg.predict(new_books)
print("1-star book predicted: GBP", round(predicted_prices[0], 2))
print("5-star book predicted: GBP", round(predicted_prices[1], 2))
print("Difference: GBP", round(predicted_prices[1] - predicted_prices[0], 2))

print("\nLimitation: listing features barely explain price on this sandbox site.")
print("Recommendation: do not set real prices from rating/stock/title length alone.")
print("\nDone. Pipeline complete.")
print("Submit: this main.py + books_clean.csv + report PDF")
