# DATA SCIENCE 500 - PRACTICAL EXERCISE 2
# Student: Shivaar
# Student number: 402308101

import numpy as np
import pandas as pd

student_data = {
    "Student_ID": ["S001", "S002", "S003", "S004", "S005", "S006",
                   "S007", "S008", "S009", "S010", "S011", "S012"],
    "Programme": ["IT", "IT", "Business", "IT", "Business", "IT",
                  "Business", "IT", "Business", "IT", "Business", "IT"],
    "Study_Hours": [6, 10, 4, 12, 7, 9, 5, 11, 8, 3, 6, 10],
    "Sleep_Hours": [7.0, 6.0, 8.0, 5.5, 7.5, 6.5, 8.0, 6.0, 7.0, 8.5, 7.5, 6.5],
    "Satisfaction_Level": [4, 3, 5, 2, 4, 4, 5, 3, 4, 2, 5, 4],
    "Attendance_Percentage": [88, 92, 76, 95, 84, 89, 73, 94, 86, 68, 81, 90],
    "Test_Score": [72, 85, 64, 91, 75, 82, 60, 88, 79, 55, 70, 84]
}

# Part B: NumPy

# Question 7 - create arrays from the dataset and confirm their dtype
scores = np.array(student_data["Test_Score"])
attendance = np.array(student_data["Attendance_Percentage"])
study_hours = np.array(student_data["Study_Hours"])
print(scores, scores.dtype)
print(attendance, attendance.dtype)
print(study_hours, study_hours.dtype)

# Question 8 - mean and median test score, rounded to 2 decimal places
mean_score = np.mean(scores)
median_score = np.median(scores)
print(round(mean_score, 2), round(median_score, 2))

# Question 9 - min, max and range of test scores
min_score = np.min(scores)
max_score = np.max(scores)
range_score = max_score - min_score
print(min_score, max_score, range_score)
# The range (36) shows the total spread between the lowest and highest test score in the class.

# Question 10 - population standard deviation of test scores
std_score = np.std(scores)
print(round(std_score, 2))
# A standard deviation of about 11 marks shows a moderate spread of scores around the mean,
# rather than everyone scoring close to the class average.

# Question 11 - scores above the class mean, using a Boolean condition
above_mean = scores[scores > mean_score]
print(above_mean, len(above_mean))

# Question 12 - indexing and slicing
print(attendance[:4])      # first four attendance values
print(study_hours[-3:])    # last three study-hour values

# Question 13 - broadcasting: add 5 bonus marks, capped at 100
adjusted_scores = np.clip(scores + 5, None, 100)
print(scores)
print(adjusted_scores)

# Part C: Pandas

# Question 14 - build the DataFrame
df = pd.DataFrame(student_data)
print(df)

# Question 15 - inspect structure
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

# Question 16 - select specific columns, then the full 4th-row record with iloc
print(df[["Student_ID", "Programme", "Test_Score"]])
print(df.iloc[3])

# Question 17 - filter: Test_Score >= 70 and Attendance_Percentage >= 80
filtered = df[(df["Test_Score"] >= 70) & (df["Attendance_Percentage"] >= 80)]
print(filtered[["Student_ID", "Programme", "Test_Score", "Attendance_Percentage"]])

# Question 18 - mean Test_Score grouped by Programme, rounded to 2 decimal places
grouped = df.groupby("Programme")["Test_Score"].mean().round(2)
print(grouped)

# Question 19 - Pass/Fail column based on Test_Score
df["Performance"] = np.where(df["Test_Score"] >= 50, "Pass", "Fail")
print(df[["Student_ID", "Test_Score", "Performance"]])

# Question 20 - export final DataFrame to CSV without the index
df.to_csv("practical2_results.csv", index=False)
