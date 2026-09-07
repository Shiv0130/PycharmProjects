# Section A:

# 1.1 Data levels of measurement determine how variables are recorded and dictate which statistical analyses can be used.
# Nominal Level
# Description: Data at this level consists of categories, labels, or names with no inherent order, ranking, or numerical value. You can only count frequencies or calculate percentages.
# Example: Eye color (e.g., Blue, Brown, Green, Hazel). One color is not higher or better than another; they are simply distinct categories.
# Ordinal Level
# Description: Data can be categorized and placed in a meaningful order or rank. However, the mathematical distance between the ranks is unknown, unequal, or cannot be measured.
# Example: Finishing positions in a race (e.g., 1st place, 2nd place, 3rd place). You know who won and who came in second, but the time gap between 1st and 2nd might be 1 second, while the gap between 2nd and 3rd might be 10 seconds.
# Interval Level
# Description: Data can be categorized and ranked, and there are equal, measurable distances between values. However, it lacks a true zero point; zero does not mean the complete absence of the variable. Because there is no true zero, you cannot make multiplication or ratio statements (e.g., you cannot say one value is "twice as much" as another).
# Example: Temperature in Celsius or Fahrenheit. The difference between 10°C and 20°C is the exact same as the difference between 20°C and 30°C (10 degrees). However, 0°C does not mean "no temperature"—it simply represents the freezing point of water. Consequently, 20°C is not "twice as hot" as 10°C.
#  Ratio Level
# Description: This is the most complex level of measurement. It possesses all the characteristics of interval data, but features a true zero point, meaning zero represents a complete absence of the property being measured. This allows you to construct meaningful ratios (multiplication and division).
# Example: Weight (e.g., 0 kg, 50 kg, 100 kg). A weight of 0 kg means an object has absolutely no weight. Because of this true zero, an object that weighs 100 kg is precisely twice as heavy as an object that weighs 50 kg.
# 1.2. Structured Data: Quantitative information organized into neat tables, relational databases, or spreadsheets. Example: A bank's customer table containing columns for account numbers, names, and balances. You can explore more details on IBM.
# Unstructured Data: Qualitative information that does not fit into standard rows and columns. Example: An email message or an audio recording of a customer service call. You can see further comparisons on AltexSoft.
#
# 1.3. The purpose of exploratory data analysis (EDA) is to summarize the main characteristics of a dataset, uncover hidden patterns, and detect data quality issues before building formal models or making assumptions. The three things a Data Scientist Looks for during an EDA is:
#  Missing Values and Data Quality Errors: Checking for null, blank, or duplicate entries and deciding how to fix them.
#  Outliers and Anomalies: Spotting extreme or unusual data points that could skew statistical results or machine learning models.
# Relationships and Correlations: Investigating how different variables interact with one another using scatter plots or correlation matrices


# Section B
# 2.1.a)
import numpy as np
test_scores = np.array([56, 79, 63, 51, 59, 61, 43, 74, 84, 86, 91, 82, 60, 89, 57, 73, 85,
 78, 72, 64])

mean = np.mean(test_scores)
print(mean)
#     b)
std_dev = np.std(test_scores)
print(std_dev)

#     c)
distinctions =[]
for score in test_scores:
    if score >=75 and score<=100:
        distinctions.append(score)
print(distinctions)

#     d) NumPy arrays are homogeneous,
#        it means that every single element inside the array must be of the exact same data type.

# 2.2 a) As the number of hours student's marks increases the test scores of students increases.
#     b)
import plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_Scores = [65, 70, 75, 83, 85, 86, 91, 93, 95]
plt.figure(figsize=(8, 5))
plt.plot(study_hours,test_Scores,marker='o',linestyle='-',color='blue')
plt.title('Test Scores vs. Study Hours')
plt.xlabel('Study Hours')
plt.ylabel('Test Scores')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# Section C:
# 3.a)
import pandas as pd
customer_tips = {'total_bill':[16.99,10.34,21.01,23.68,24.59,25.29,8.77,26.88],'tip':[1.01,1.66,3.50,3.31,4.71,2.00,3.12],'sex':['Female','Male','Male','Male','Female','Male','Male','Male'],'day':['Sun','Sun','Sun','Sun','Sun','Sun','Sun','Sun'], 'time':['Dinner','Dinner','Dinner','Dinner','Dinner','Dinner','Dinner','Dinner'],'size':[2,3,3,2,4,4,2,4] }
df = pd.DataFrane(customer_tips)

#   b)
# total_bill is Quantitative(continous),Ratio
# tip is quantitative (continous),Ratio
# sex is qualitative,Nominal
# day is Qualitative,Nominal
# time is Qualitative,Nominal
#size is Quantitative(discrete),Ratio

#   c)
customer_tips_summary = customer_tips.describe()
#   d)
# Nature of relationship:As total bill rises,tip generally rises with it,roughly linear
# Gender distribution: Both sexes appear across the full bill range
# General conclusion: Customers tip roughly according to their bill regardless of their sex
# Outliers: The point around a R7 bill with round about a R5 tip stands out

#4.a) P(cancer) = 200/1000 = 0.20
# .b) Sensitivity = TP(TP+FN) = 160/200 =0.80
# .c) Specificity = TN =(TN+FP) = 680/800 =0.85
# .d) PPV = TP/(TP+FP) = 160/280 = 0.57
# .e) P(Cancer|Positive) = [P(Positive|Cancer).P(Cancer)]/P(Positive) = (0.80*0.20)/0.28 = 0.57
# .f) Confusion matrix is the table above

