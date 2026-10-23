# Data Science 500 - Book Market Analytics
# Lab 2: Data Cleaning (pandas style like practical2 / Lab A)
# Run after 01_scrape.py (or use existing books_raw.csv)

import pandas as pd

raw = pd.read_csv("books_raw.csv")
print("Shape (rows, columns):", raw.shape)
print(raw.isnull().sum())

books = raw.copy()
print("Rows before cleaning:", len(books))

# drop rows missing category or stock text
books = books.dropna(subset=["category", "stock_text"])
print("Rows after dropna:", len(books))

# price text "£51.77" -> float
books["price_gbp"] = books["price"].str.replace("£", "", regex=False).astype(float)

# rating word -> number (One..Five)
rating_numbers = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
books["rating_num"] = books["rating"].map(rating_numbers)
print("Ratings not converted:", books["rating_num"].isnull().sum())


def get_quantity(stock_text):
    # "In stock (22 available)" -> 22
    if isinstance(stock_text, str) and "(" in stock_text:
        return int(stock_text.split("(")[1].split(" ")[0])
    return 0


books["stock_qty"] = books["stock_text"].apply(get_quantity)

# tidy categories
books["category"] = books["category"].str.strip()
books["category"] = books["category"].replace({
    "Default": "Uncategorised",
    "Add a comment": "Uncategorised",
})

# title / description features
books["title"] = books["title"].str.strip()
books["description"] = books["description"].fillna("")
books["description_clean"] = books["description"].str.lower().str.strip()
books["title_length"] = books["title"].str.len()
books["title_words"] = books["title"].str.split().str.len()
books["description_length"] = books["description_clean"].str.len()
books["description_words"] = books["description_clean"].str.split().str.len()

# checks for the cleaning section of the rubric
print("No missing values:", books.isnull().sum().sum() == 0)
print("Prices > 0:", (books["price_gbp"] > 0).all())
print("Ratings 1-5:", books["rating_num"].between(1, 5).all())
print("Stock >= 0:", (books["stock_qty"] >= 0).all())
print("Enough books (>=200):", len(books) >= 200)

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
