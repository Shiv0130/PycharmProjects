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

#Part B: NumPy

# Q7
scores = np.array(student_data["Test_Score"])
attendance = np.array(student_data["Attendance_Percentage"])
study_hours = np.array(student_data["Study_Hours"])
print(scores, scores.dtype)
print(attendance, attendance.dtype)
print(study_hours, study_hours.dtype)

# Q8
mean_score = np.mean(scores)
median_score = np.median(scores)
print(round(mean_score, 2), round(median_score, 2))

# Q9
min_score = np.min(scores)
max_score = np.max(scores)
range_score = max_score - min_score
print(min_score, max_score, range_score)

# Q10
std_score = np.std(scores)
print(round(std_score, 2))

# Q11
above_mean = scores[scores > mean_score]
print(above_mean, len(above_mean))

# Q12
print(attendance[:4])
print(study_hours[-3:])

# Q13
adjusted_scores = np.clip(scores + 5, None, 100)
print(scores)
print(adjusted_scores)

#Part C: Pandas

# Q14
df = pd.DataFrame(student_data)
print(df)

# Q15
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

# Q16
print(df[["Student_ID", "Programme", "Test_Score"]])
print(df.iloc[3])

# Q17
filtered = df[(df["Test_Score"] >= 70) & (df["Attendance_Percentage"] >= 80)]
print(filtered[["Student_ID", "Programme", "Test_Score", "Attendance_Percentage"]])

# Q18
grouped = df.groupby("Programme")["Test_Score"].mean().round(2)
print(grouped)

# Q19
df["Performance"] = np.where(df["Test_Score"] >= 50, "Pass", "Fail")
print(df[["Student_ID", "Test_Score", "Performance"]])

# Q20
df.to_csv("practical2_results.csv", index=False)