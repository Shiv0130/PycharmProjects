import pandas as pd  # bring in pandas for tables

# load the csv - file must be in the same folder
df = pd.read_csv("practice_students.csv")

# show first 5 rows
print(df.head())
# show number of rows and columns
print(df.shape)
# show column types and non-null counts
print(df.info())
# show numeric summary (mean, min, max, etc)
print(df.describe())
# show missing values per column
print(df.isnull().sum())
# count how many students per city
print(df["City"].value_counts())

# Grade function - same idea as practical2 Performance column
def get_grade(m):
    # 80 or more = A
    if m >= 80:
        return "A"
    # 70 or more = B
    elif m >= 70:
        return "B"
    # everything else = C
    else:
        return "C"

# apply get_grade to every value in Marks
df["Grade"] = df["Marks"].apply(get_grade)

# only rows where Grade is A
print(df[df["Grade"] == "A"])
# sort whole table by Marks, highest first
print(df.sort_values("Marks", ascending=False))
# average Marks for each City
print(df.groupby("City")["Marks"].mean())
