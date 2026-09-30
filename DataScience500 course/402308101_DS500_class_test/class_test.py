# DSC500 Test 1 - full answers (your style + fixes)
# Use for revision under lockdown: write these patterns by hand

# ========== SECTION A (theory - write in words) ==========
# 1.1 Nominal: categories, no order (eye colour)
#     Ordinal: ranked, unequal gaps (1st/2nd/3rd)
#     Interval: equal gaps, no true zero (Celsius)
#     Ratio: true zero (weight kg)
# 1.2 Structured: rows/columns (bank table, CSV)
#     Unstructured: no fixed schema (email, audio)
# 1.3 EDA: summarise + find issues before modelling
#     Look for: missing values, outliers, relationships

# ========== SECTION B ==========
import numpy as np

test_scores = np.array([
    56, 79, 63, 51, 59, 61, 43, 74, 84, 86,
    91, 82, 60, 89, 57, 73, 85, 78, 72, 64
])

# 2.1 a) mean
print(np.mean(test_scores))

# 2.1 b) standard deviation
print(np.std(test_scores))

# 2.1 c) distinctions 75-100
print(test_scores[(test_scores >= 75) & (test_scores <= 100)])

# 2.1 d) homogeneous = every element has the same data type

# 2.2 a) As study hours increase, test scores increase (positive relationship)

# 2.2 b) line plot
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_Scores = [65, 70, 75, 83, 85, 86, 91, 93, 95]

plt.figure(figsize=(8, 5))
plt.plot(study_hours, test_Scores, marker="o", linestyle="-", color="blue")
plt.title("Test Scores vs. Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Test Scores")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# ========== SECTION C Q3 ==========
import pandas as pd

# columns must be same length
customer_tips = {
    "total_bill": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88],
    "tip":        [1.01, 1.66, 3.50, 3.31, 4.71, 2.00, 1.96, 3.12],
    "sex":  ["Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male"],
    "day":  ["Sun"] * 8,
    "time": ["Dinner"] * 8,
    "size": [2, 3, 3, 2, 4, 4, 2, 4],
}

df = pd.DataFrame(customer_tips)  # NOT DataFrane
print(df.describe())              # NOT customer_tips.describe()

# 3.b classifications:
# total_bill - Quantitative continuous, Ratio
# tip        - Quantitative continuous, Ratio
# sex        - Qualitative, Nominal
# day        - Qualitative, Nominal
# time       - Qualitative, Nominal
# size       - Quantitative discrete, Ratio

# 3.d scatter: positive tip vs bill; both sexes across range;
#     tip tracks bill; outlier = high tip on low bill

# ========== SECTION C Q4 ==========
# n=1000; cancer=200; no cancer=800
# TP=160; FP=120; FN=40; TN=680
#
# a) P(cancer) = 200/1000 = 0.20
# b) Sensitivity = TP/(TP+FN) = 160/200 = 0.80
# c) Specificity = TN/(TN+FP) = 680/800 = 0.85
# d) PPV = TP/(TP+FP) = 160/280 ≈ 0.57
# e) P(C|Pos) = (0.80*0.20)/0.28 ≈ 0.57
# f) Confusion matrix:
#              Pred+   Pred-
# Actual+       160     40
# Actual-       120    680
