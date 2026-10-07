# Coding-Based Questions – Chapter 3 (Regression)
# Done with study notes + trying the code myself

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score

# ============================================================
# 1. Linear Regression + interpret coefficients
# ============================================================
print("=" * 55)
print("1. Linear Regression – coefficients")
print("=" * 55)

housing = fetch_california_housing()
X = housing.data
y = housing.target
feature_names = housing.feature_names

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# scale so coefficients are comparable
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

lin = LinearRegression()
lin.fit(X_train_s, y_train)

print("Intercept:", round(lin.intercept_, 4))
print("\nCoefficients (scaled features):")
for name, coef in zip(feature_names, lin.coef_):
    print(f"  {name:15s}: {coef:8.4f}")

# Interpretation (own words):
# Positive coef → higher feature value pushes predicted house price up.
# Negative coef → higher feature value pushes predicted price down.
# Biggest absolute coef means that feature has the strongest effect
# after scaling (so we are not just seeing large-range features win).

y_pred_lin = lin.predict(X_test_s)
print(f"\nLinear  R²  : {r2_score(y_test, y_pred_lin):.4f}")
print(f"Linear  MAE : {mean_absolute_error(y_test, y_pred_lin):.4f}")


# ============================================================
# 2. Compare Linear vs Polynomial vs Decision Tree
# ============================================================
print("\n" + "=" * 55)
print("2. Model comparison (same train/test split)")
print("=" * 55)

# Polynomial degree 2
poly = Pipeline([
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("lin", LinearRegression())
])
poly.fit(X_train_s, y_train)
y_pred_poly = poly.predict(X_test_s)

# Decision Tree (limit depth so it doesn’t just memorise)
tree = DecisionTreeRegressor(max_depth=5, random_state=42)
tree.fit(X_train_s, y_train)
y_pred_tree = tree.predict(X_test_s)

results = [
    ("Linear",      y_pred_lin),
    ("Polynomial",  y_pred_poly),
    ("Decision Tree", y_pred_tree)
]

print(f"{'Model':15s} {'R²':>8s} {'MAE':>8s}")
print("-" * 35)
for name, pred in results:
    r2 = r2_score(y_test, pred)
    mae = mean_absolute_error(y_test, pred)
    print(f"{name:15s} {r2:8.4f} {mae:8.4f}")


# ============================================================
# 3. Visualise regression curves (1 feature so we can plot)
# ============================================================
print("\n" + "=" * 55)
print("3. Regression curves (using MedInc only for plot)")
print("=" * 55)

# Use only median income so the curve is 2-D and easy to see
X_1d = X[:, 0].reshape(-1, 1)   # MedInc
X_tr, X_te, y_tr, y_te = train_test_split(X_1d, y, test_size=0.2, random_state=42)

# sort for smooth lines
order = np.argsort(X_te.ravel())
X_plot = X_te[order]
y_true_plot = y_te[order]

lin_1d = LinearRegression().fit(X_tr, y_tr)
poly_1d = Pipeline([
    ("poly", PolynomialFeatures(degree=3, include_bias=False)),
    ("lin", LinearRegression())
]).fit(X_tr, y_tr)
tree_1d = DecisionTreeRegressor(max_depth=4, random_state=42).fit(X_tr, y_tr)

plt.figure(figsize=(8, 5))
plt.scatter(X_plot, y_true_plot, alpha=0.3, s=12, label="Actual")
plt.plot(X_plot, lin_1d.predict(X_plot), color="red", linewidth=2, label="Linear")
plt.plot(X_plot, poly_1d.predict(X_plot), color="green", linewidth=2, label="Polynomial (deg 3)")
plt.plot(X_plot, tree_1d.predict(X_plot), color="purple", linewidth=2, label="Decision Tree")
plt.xlabel("Median Income (MedInc)")
plt.ylabel("House price (target)")
plt.title("Regression curves on one feature")
plt.legend()
plt.tight_layout()
plt.show()

# Quick note on what you see:
# Linear = straight line (assumes straight relationship).
# Polynomial = can bend, captures mild curves, but high degree can overfit.
# Decision Tree = step-like jumps (splits), very flexible but can overfit if deep.