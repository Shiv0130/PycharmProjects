import pandas as pd  # tables
import numpy as np   # arrays

# load the csv
df = pd.read_csv("practice_students.csv")

# turn columns into NumPy arrays
marks = df["Marks"].to_numpy()
hours = df["StudyHours"].to_numpy()

# class means
mean_mark = np.mean(marks)
mean_hour = np.mean(hours)
print(mean_mark, mean_hour)
# marks above the class mean
print(marks[marks > mean_mark])

# True/False column: above mean?
df["AboveMean"] = marks > mean_mark
# standard deviation of marks
std_dev = np.std(marks)
# z-score = (value - mean) / std
df["Z_Marks"] = (marks - mean_mark) / std_dev

# show new columns
print(df[["Student", "Marks", "AboveMean", "Z_Marks"]].head())

# both conditions must be True
print(df[(df["StudyHours"] > 10) & (df["Marks"] >= 80)])
