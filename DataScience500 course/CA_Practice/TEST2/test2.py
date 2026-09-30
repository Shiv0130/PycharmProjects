#My original code
# import pandas as pd
# import numpy as np
# data = {
#     'Student': ['Lerato','Aisha','Thabo'],
#     'Marks': [85,67,92,74],
#     'Subject':['Math','Science','Math','English']
#
# }
#
# df = pd.DataFrame(data)
#
# #a)
# head = df.head() #Displays the first 5 rows
# print(head)
# #b)
# types= df.dtypes() # Diplays the data type
# print(types)
#
# summary = df.describe() #numeric summary
# print(summary)
#
# #c)
# marks = data['Marks']
# ArrMarks = np.array(marks)
#
# avgMarks = np.mean(ArrMarks)
#
# print(avgMarks)
#
# #d)
# if marks>=80:
#     print("A")
#     else if(marks >=70 && marks<80):
#         print("B")
#         else(marks<70):
#         print("C")
#
# #e)
# if(marks)>=80:
#     print(data['Student'])
#
# #f)
# df.sort_values(marks,ascending=False)


import pandas as pd
import numpy as np

#fixed: Kabelo was missing - lists must be the same length
data = {
    "Student":["Lerato","Kabelo","Aisha","Thabo"],
    "Marks": [85,67,92,74],
    "Subject": ["Math","Science","Math","English"]
}

df = pd.DataFrame()

#a) first five rows
print(df.head())

#b) data types AND summary info-> dtypes has no ()  and info() covers  both
print(df.dtypes)
print(df.info)

#c) average marks - use DataFrame column, not the raw dict
marks_array = np.array(df["Marks"])
avg_marks = np.mean(marks_array)
print(avg_marks)

#d) Grade column - nested np where instead of  if/elif on a whole column
df['Grade'] = np.where(df["Marks"] >= 80,"A",
                       np.where(df["Marks"] >=70,"B","C"))
print(df)

#e) Only Grade A students
print(df[df["Grade"]== "A"])

# f) story by Marks,descending
df_sorted = df.sort_values("Marks",ascending=False)
print(df_sorted)