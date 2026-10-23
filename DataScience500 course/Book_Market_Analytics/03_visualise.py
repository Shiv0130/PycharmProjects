# Data Science 500 - Book Market Analytics
# Lab 3: Visualisation (Matplotlib only - study guide Ch 4)
# Run after 02_clean.py

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

books = pd.read_csv("books_clean.csv")
print("Shape (rows, columns):", books.shape)
print(books[["price_gbp", "rating_num", "stock_qty"]].describe())

os.makedirs("charts", exist_ok=True)

# ---- 1. price distribution ----
prices = books["price_gbp"]
average_price = prices.mean()

plt.figure(figsize=(10, 5))
plt.hist(prices, bins=10, color="steelblue", edgecolor="white")
plt.axvline(average_price, color="black", linestyle="--")
plt.xlabel("Price (GBP)")
plt.ylabel("Number of books")
plt.title("Book prices from 10 to 60 GBP")
plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("charts/1_price_distribution.png", dpi=150)
plt.show()

# ---- 2. rating count and mean price ----
by_rating = books.groupby("rating_num")["price_gbp"].agg(["count", "mean"])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(by_rating.index, by_rating["count"], color="steelblue")
ax1.set_xlabel("Star rating")
ax1.set_ylabel("Number of books")
ax1.set_title("Books per star rating")
ax1.grid(True, axis="y", linestyle="--", alpha=0.5)

ax2.bar(by_rating.index, by_rating["mean"], color="steelblue")
ax2.set_xlabel("Star rating")
ax2.set_ylabel("Average price (GBP)")
ax2.set_title("Average price by star rating")
ax2.grid(True, axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/2_rating.png", dpi=150)
plt.show()

# ---- 3. average price by genre (genres with 20+ books) ----
genre_stats = books.groupby("category")["price_gbp"].agg(["count", "mean"])
genre_stats = genre_stats[genre_stats["count"] >= 20].sort_values("mean")

plt.figure(figsize=(10, 7))
plt.barh(genre_stats.index, genre_stats["mean"], color="steelblue")
plt.xlabel("Average price (GBP)")
plt.title("Average price by genre (20+ books)")
plt.grid(True, axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("charts/3_genres.png", dpi=150)
plt.show()

# ---- 4. stock levels ----
stock_counts = books["stock_qty"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(stock_counts.index, stock_counts.values, color="steelblue")
plt.xlabel("Copies in stock")
plt.ylabel("Number of books")
plt.title("Stock levels")
plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("charts/4_stock.png", dpi=150)
plt.show()

# ---- 5. scatter: price vs each feature (Matplotlib only) ----
features = ["rating_num", "stock_qty", "title_length", "description_length"]
labels = ["Star rating", "Copies in stock", "Title length", "Description length"]

fig, axes = plt.subplots(1, 4, figsize=(14, 4))
for i in range(4):
    axes[i].scatter(books[features[i]], books["price_gbp"], alpha=0.3, color="steelblue", s=15)
    axes[i].set_xlabel(labels[i])
    axes[i].set_ylabel("Price (GBP)")
    axes[i].grid(True, linestyle="--", alpha=0.4)
fig.suptitle("Price against each feature")
plt.tight_layout()
plt.savefig("charts/5_scatter.png", dpi=150)
plt.show()

# ---- 6. correlation with price ----
number_columns = [
    "price_gbp", "rating_num", "stock_qty",
    "title_length", "description_length",
]
correlations = books[number_columns].corr()
print(correlations.round(2))

price_links = correlations["price_gbp"].drop("price_gbp")
names = ["Star rating", "Copies in stock", "Title length", "Description length"]

plt.figure(figsize=(10, 5))
plt.barh(names, price_links.values, color="steelblue")
plt.axvline(0, color="black", linewidth=1)
plt.xlim(-1, 1)
plt.xlabel("Correlation with price (-1 to 1)")
plt.title("Correlation of features with price")
plt.grid(True, axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("charts/6_correlation.png", dpi=150)
plt.show()

print("Charts saved in charts/")
