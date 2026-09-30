import pandas as pd  # tables
import numpy as np   # arrays
import matplotlib.pyplot as plt  # plots

# load the csv
df = pd.read_csv("practice_students.csv")
# first 5 rows
print(df.head())

# Grade function
def get_grade(m):
    if m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    else:
        return "C"

# apply Grade to Marks
df["Grade"] = df["Marks"].apply(get_grade)

# arrays
marks = df["Marks"].to_numpy()
hours = df["StudyHours"].to_numpy()
# mean and how many distinctions
print(round(np.mean(marks), 2), int((marks >= 75).sum()))

# scatter + trend line
plt.figure(figsize=(10, 6))
plt.scatter(hours, marks, marker="^", color="purple", label="Students")
# fit a straight line through the points
m, c = np.polyfit(hours, marks, 1)
plt.plot(hours, m * hours + c, "--", color="orange", label="Trend")
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.title("Study hours vs marks")
plt.legend()
plt.show()

# mean Marks by City, sorted low to high
city_means = df.groupby("City")["Marks"].mean().sort_values()
# horizontal bars
plt.barh(city_means.index, city_means.values)
plt.xlabel("Average marks")
plt.title("Average marks by city")
plt.show()

# histogram of marks
plt.hist(marks, bins=8, color="navy")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.title("Distribution of marks")
plt.show()
