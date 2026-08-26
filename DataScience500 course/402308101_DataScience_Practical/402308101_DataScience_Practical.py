# #8.# DATA SCIENCE 500 PRACTICAL
#    # Student name: Shivaar
#    # Student number: 402308101
#
# #9.Import required libraries
# import pandas as pd
# import numpy as np
# # 10. import the csv file into a Panda DataFrame
# df = pd.read_csv("data_science_ch1_to_2_5_student_dataset.csv")
# # 11.  Displays the first 5 records using head function
# print(df.head())
# #12. Displays the last 5 records using tail function
# print(df.tail())
#
# # 13.Showing number of rows and columns
# print(df.shape)
#
# #All column names
# print(df.columns)
#
# #data types for every column
# print(df.dtypes)
#
# #The number of missing values in each  column
# print(df.isna().sum())
#
# #Student ID duplicate
# print(df.duplicated(subset = 'student_id').sum())
#
# #14.
# #  It is structured because it has a clear tabluar format
# #  The learning comment column is unstructured cause it doesn't follow a set format
# # programme is qualitative,study_mode is also qualitative and satisfaction_level is also qualitative
# # student_id,campus_temperature_c,study_hours_per_week,assessment_score,monthly_data_spend_zar,modules_registered are quantitative
# # Discrete quantitative varibales are student_id(despite it acting as an identifier,it is still numeric). Other one is modules_registered( you can't register for 3.5 modules).
# # The ffg can take any value within a range: campus_temperature_c,study_hours_per_week,assessment_score,monthly_data_spend_zar
#
# """
# 15.	Classify each of the following variables as nominal, ordinal, interval or ratio:
# Variable	Level of measurement
# student_id	nominal
# programme	nominal
# study_mode	nominal
# satisfaction_level	Ordinal
# campus_temperature_c	Interval
# study_hours_per_week	Ratio
# assessment_score	Ratio
# monthly_data_spend_zar	Ratio
# modules_registered	Ratio
#
# 16. Levels of measurement:
#  student_id - Nominal (identifier only)
#  programme - Nominal (categorical)
#  study_mode - Nominal (categorical)
#  satisfaction_level - Ordinal (ranked levels)
#  campus_temperature_c - Interval (equal intervals, no true zero)
#  study_hours_per_week - Ratio (true zero, measurable quantity)
#  assessment_score - Ratio (true zero, measurable quantity)
#  monthly_data_spend_zar - Ratio (true zero, measurable quantity)
#  modules_registered - Ratio (true zero, count data)
#
#
# """
#
# #17.Convert the assessment_score column into a NumPy array
# assessment_array = np.array(df["assessment_score"])
#
# #18.Calculate descriptive statistics for assessment_score
# mean_score = np.mean(assessment_array)
# median_score = np.median(assessment_array)
# min_score = np.min(assessment_array)
# max_score = np.max(assessment_array)
# range_score = max_score - min_score
# variance_score = np.var(assessment_array)
# std_dev_score = np.std(assessment_array)
#
# # Display results clearly
# print("Mean assessment score:", mean_score)
# print("Median assessment score:", median_score)
# print("Minimum assessment score:", min_score)
# print("Maximum assessment score:", max_score)
# print("Range of assessment scores:", range_score)
# print("Variance of assessment scores:", variance_score)
# print("Standard deviation of assessment scores:", std_dev_score)
#
#
# #19. Repeat descriptive statistics for study_hours_per_week
# study_hours_array = np.array(df["study_hours_per_week"])
# print("Mean study hours per week:", np.mean(study_hours_array))
# print("Median study hours per week:", np.median(study_hours_array))
# print("Minimum study hours per week:", np.min(study_hours_array))
# print("Maximum study hours per week:", np.max(study_hours_array))
# print("Range of study hours per week:", np.max(study_hours_array) - np.min(study_hours_array))
# print("Variance of study hours per week:", np.var(study_hours_array))
# print("Standard deviation of study hours per week:", np.std(study_hours_array))
#
# #20. Repeat descriptive statistics for monthly_data_spend_zar
# data_spend_array = np.array(df["monthly_data_spend_zar"])
# print("Mean monthly data spend (ZAR):", np.mean(data_spend_array))
# print("Median monthly data spend (ZAR):", np.median(data_spend_array))
# print("Minimum monthly data spend (ZAR):", np.min(data_spend_array))
# print("Maximum monthly data spend (ZAR):", np.max(data_spend_array))
# print("Range of monthly data spend (ZAR):", np.max(data_spend_array) - np.min(data_spend_array))
# print("Variance of monthly data spend (ZAR):", np.var(data_spend_array))
# print("Standard deviation of monthly data spend (ZAR):", np.std(data_spend_array))
#
# #21. Determine and display the mode of programme, study_mode, and satisfaction_level
# print("Mode of programme:", df["programme"].mode()[0])
# print("Mode of study mode:", df["study_mode"].mode()[0])
# print("Mode of satisfaction level:", df["satisfaction_level"].mode()[0])
#
# #22. Count and display how many students belong to each category
# print("Students per programme:\n", df["programme"].value_counts())
# print("Students per study mode:\n", df["study_mode"].value_counts())
# print("Students per satisfaction level:\n", df["satisfaction_level"].value_counts())
#
# #23. Sort the assessment scores from the lowest to the highest and display the result
# sorted_scores = np.sort(df["assessment_score"])
# print("Sorted assessment scores:\n", sorted_scores)
#
# #24. Use NumPy indexing or slicing to display subsets of assessment scores
# print("First five assessment scores:", sorted_scores[:5])
# print("Last five assessment scores:", sorted_scores[-5:])
# print("Assessment scores greater than or equal to 75:", sorted_scores[sorted_scores >= 75])
#
# #25. Identify and display specific score details
# highest_score = np.max(df["assessment_score"])
# lowest_score = np.min(df["assessment_score"])
# print("Student with highest assessment score:\n", df[df["assessment_score"] == highest_score])
# print("Student with lowest assessment score:\n", df[df["assessment_score"] == lowest_score])
# print("Number of students scoring 50 or higher:", np.sum(df["assessment_score"] >= 50))
# print("Number of students scoring below 50:", np.sum(df["assessment_score"] < 50))
#
# #26. Interpretation (100–150 words)
#
# #27 Ensure that the interpertation speaks about:
# #	The typical assessment performance
# #	How widely the assessment scores are spread
# #	The most common programme or study mode
# #	One additional observation from the dataset
#
# """
# 28. Interpretation:
# The dataset shows that the typical assessment performance is moderate, with most students scoring close to the mean.
# The spread of scores, indicated by the standard deviation, suggests some variation but not extreme differences.
# The most common programme and study mode highlight where most students are concentrated, showing dominant learning patterns.
# Students who study more hours per week tend to achieve higher assessment scores, suggesting consistent effort improves outcomes.
# Overall, the data reflects balanced performance across programmes, with a few standout achievers and some lower scores that may benefit from additional support.
# """
#
#

# DATA SCIENCE 500 PRACTICAL
# Student name: Shivaar
# Student number: 402308101

# 1. Importing libraries
#8. Import required libraries
import pandas as pd
import numpy as np

# 2. Importing the CSV file
#9. Import the CSV file into a Pandas DataFrame
df = pd.read_csv("data_science_ch1_to_2_5_student_dataset.csv")

# 3. Initial dataset exploration
#10. Display the first 5 records using head() function
print(df.head())
#11. Display the last 5 records using tail() function
print(df.tail())

#12. Showing number of rows and columns
print(df.shape)

#13. All column names
print(df.columns)

# Data types for every column
print(df.dtypes)

# The number of missing values in each column
print(df.isna().sum())

# Student ID duplicates
print(df.duplicated(subset='student_id').sum())

# 4. Data-type classification
#14. It is structured because it has a clear tabular format.
# The 'learning_comment' column is unstructured because it doesn't follow a set format.
# programme is qualitative, study_mode is qualitative, and satisfaction_level is qualitative.
# student_id, campus_temperature_c, study_hours_per_week, assessment_score, monthly_data_spend_zar, modules_registered are quantitative.
# Discrete quantitative variables: student_id (numeric identifier) and modules_registered (cannot register for fractional modules).
# Continuous quantitative variables: campus_temperature_c, study_hours_per_week, assessment_score, monthly_data_spend_zar.

# 5. Levels of measurement
"""
15. Classify each of the following variables as nominal, ordinal, interval or ratio:
Variable    Level of measurement
student_id          Nominal
programme           Nominal
study_mode          Nominal
satisfaction_level  Ordinal
campus_temperature_c    Interval
study_hours_per_week    Ratio
assessment_score        Ratio
monthly_data_spend_zar  Ratio
modules_registered      Ratio

16. Levels of measurement:
 student_id - Nominal (identifier only)
 programme - Nominal (categorical)
 study_mode - Nominal (categorical)
 satisfaction_level - Ordinal (ranked levels)
 campus_temperature_c - Interval (equal intervals, no true zero)
 study_hours_per_week - Ratio (true zero, measurable quantity)
 assessment_score - Ratio (true zero, measurable quantity)
 monthly_data_spend_zar - Ratio (true zero, measurable quantity)
 modules_registered - Ratio (true zero, count data)
"""

# 6. Descriptive statistics
#17. Convert the assessment_score column into a NumPy array
assessment_array = np.array(df["assessment_score"])

#18. Calculate descriptive statistics for assessment_score
mean_score = np.mean(assessment_array)
median_score = np.median(assessment_array)
min_score = np.min(assessment_array)
max_score = np.max(assessment_array)
range_score = max_score - min_score
variance_score = np.var(assessment_array)
std_dev_score = np.std(assessment_array)

# Display results clearly
print("Mean assessment score:", mean_score)
print("Median assessment score:", median_score)
print("Minimum assessment score:", min_score)
print("Maximum assessment score:", max_score)
print("Range of assessment scores:", range_score)
print("Variance of assessment scores:", variance_score)
print("Standard deviation of assessment scores:", std_dev_score)

#19. Repeat descriptive statistics for study_hours_per_week
study_hours_array = np.array(df["study_hours_per_week"])
print("Mean study hours per week:", np.mean(study_hours_array))
print("Median study hours per week:", np.median(study_hours_array))
print("Minimum study hours per week:", np.min(study_hours_array))
print("Maximum study hours per week:", np.max(study_hours_array))
print("Range of study hours per week:", np.max(study_hours_array) - np.min(study_hours_array))
print("Variance of study hours per week:", np.var(study_hours_array))
print("Standard deviation of study hours per week:", np.std(study_hours_array))

#20. Repeat descriptive statistics for monthly_data_spend_zar
data_spend_array = np.array(df["monthly_data_spend_zar"])
print("Mean monthly data spend (ZAR):", np.mean(data_spend_array))
print("Median monthly data spend (ZAR):", np.median(data_spend_array))
print("Minimum monthly data spend (ZAR):", np.min(data_spend_array))
print("Maximum monthly data spend (ZAR):", np.max(data_spend_array))
print("Range of monthly data spend (ZAR):", np.max(data_spend_array) - np.min(data_spend_array))
print("Variance of monthly data spend (ZAR):", np.var(data_spend_array))
print("Standard deviation of monthly data spend (ZAR):", np.std(data_spend_array))

# 7. Category and score analysis
#21. Determine and display the mode of programme, study_mode, and satisfaction_level
print("Mode of programme:", df["programme"].mode()[0])
print("Mode of study mode:", df["study_mode"].mode()[0])
print("Mode of satisfaction level:", df["satisfaction_level"].mode()[0])

#22. Count and display how many students belong to each category
print("Students per programme:\n", df["programme"].value_counts())
print("Students per study mode:\n", df["study_mode"].value_counts())
print("Students per satisfaction level:\n", df["satisfaction_level"].value_counts())

#23. Sort the assessment scores from the lowest to the highest and display the result
sorted_scores = np.sort(df["assessment_score"])
print("Sorted assessment scores:\n", sorted_scores)

#24. Use NumPy indexing or slicing to display subsets of assessment scores
print("First five assessment scores:", sorted_scores[:5])
print("Last five assessment scores:", sorted_scores[-5:])
print("Assessment scores greater than or equal to 75:", sorted_scores[sorted_scores >= 75])

#25. Identify and display specific score details
highest_score = np.max(df["assessment_score"])
lowest_score = np.min(df["assessment_score"])
print("Student with highest assessment score:\n", df[df["assessment_score"] == highest_score])
print("Student with lowest assessment score:\n", df[df["assessment_score"] == lowest_score])
print("Number of students scoring 50 or higher:", np.sum(df["assessment_score"] >= 50))
print("Number of students scoring below 50:", np.sum(df["assessment_score"] < 50))

# 8. Interpretation and conclusion
#26. Interpretation (100–150 words)
#27. Ensure that the interpretation discusses:
#   The typical assessment performance
#   How widely the assessment scores are spread
#   The most common programme or study mode
#   One additional observation from the dataset

"""
28. Interpretation:
The dataset shows that the typical assessment performance is moderate, with most students scoring close to the mean. 
The spread of scores, indicated by the standard deviation, suggests some variation but not extreme differences. 
The most common programme and study mode highlight where most students are concentrated, showing dominant learning patterns. 
Students who study more hours per week tend to achieve higher assessment scores, suggesting consistent effort improves outcomes. 
Overall, the data reflects balanced performance across programmes, with a few standout achievers and some lower scores that may benefit from additional support.
"""
