# DATA SCIENCE 500 - Book Market Analytics
# Student: 402308101
# Part 4: Predictive Modelling - Linear Regression
# Assignment: estimate book price from listing features
# Style: MLAssignment600 main.py (PART blocks, train_test_split)
# Study guide: supervised learning - predictors + response

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# load clean data
books = pd.read_csv("books_clean.csv")
print("Shape (rows, columns):", books.shape)

os.makedirs("charts", exist_ok=True)


def save_fig(name):
    plt.tight_layout()
    plt.savefig("charts/" + name + ".png", dpi=150, bbox_inches="tight")
    plt.show()


print("=" * 60)
print("PART A - Features and target")
print("=" * 60)

# predictors (X) and response (y)
feature_cols = ["rating_num", "stock_qty", "title_length", "description_length"]
X = books[feature_cols]
y = books["price_gbp"]

print("Predictors:", feature_cols)
print("Response: price_gbp")

print("=" * 60)
print("PART B - Train / test split (80/20)")
print("=" * 60)

# same pattern as MLAssignment600
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print("Train shape:", X_train.shape)
print("Test shape :", X_test.shape)

print("=" * 60)
print("PART C - Fit Linear Regression")
print("=" * 60)

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

print("=" * 60)
print("PART D - Evaluation (MAE vs mean baseline)")
print("=" * 60)

guess = y_train.mean()
print("Simple guess (train mean): £" + str(round(guess, 2)))

train_mae_guess = (y_train - guess).abs().mean()
test_mae_guess = (y_test - guess).abs().mean()
train_mae_model = train_residuals.abs().mean()
test_mae_model = test_residuals.abs().mean()

results = pd.DataFrame({
    "Average error on training books (£)": [train_mae_guess, train_mae_model],
    "Average error on test books (£)": [test_mae_guess, test_mae_model],
}, index=["Always guess the average", "Linear regression"])
print(results.round(2))

model_squared = (test_residuals ** 2).sum()
guess_squared = ((y_test - guess) ** 2).sum()
print(
    "Model squared errors as a share of the guess:",
    str(round(model_squared / guess_squared * 100, 1)) + "%",
)

print("=" * 60)
print("PART E - Charts")
print("=" * 60)

plt.figure(figsize=(8, 7))
plt.scatter(test_predictions, y_test, alpha=0.5, s=30, color="steelblue")
plt.plot([10, 60], [10, 60], "--", color="black", linewidth=1.5)
plt.xlim(10, 60)
plt.ylim(10, 60)
plt.xlabel("Predicted price (£)")
plt.ylabel("Real price (£)")
plt.title("Predicted prices barely move, real prices do")
plt.grid(alpha=0.3, linestyle="--")
save_fig("7_actual_vs_predicted")

names = ["Always guess\nthe average", "Linear\nregression"]
errors = [test_mae_guess, test_mae_model]
plt.figure(figsize=(8, 5))
bars = plt.bar(names, errors, color=["lightgrey", "steelblue"], width=0.5)
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.3,
        "£" + str(round(bar.get_height(), 2)),
        ha="center",
    )
plt.ylim(0, 16)
plt.ylabel("Average error on test books (£)")
plt.title("The model is no more accurate than guessing")
plt.grid(axis="y", alpha=0.3, linestyle="--")
save_fig("8_error_comparison")

print("=" * 60)
print("PART F - Example prediction")
print("=" * 60)

new_books = pd.DataFrame({
    "rating_num": [1, 5],
    "stock_qty": [10, 10],
    "title_length": [30, 30],
    "description_length": [1400, 1400],
})
predicted_prices = linreg.predict(new_books)
print("1-star book: £" + str(round(predicted_prices[0], 2)))
print("5-star book: £" + str(round(predicted_prices[1], 2)))
print("Difference:  £" + str(round(predicted_prices[1] - predicted_prices[0], 2)))
print("\nLimitation: listing features barely explain price on this sandbox site.")
print("Done.")
