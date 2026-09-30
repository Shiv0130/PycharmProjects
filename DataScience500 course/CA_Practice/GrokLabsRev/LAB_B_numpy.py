import numpy as np  # bring in NumPy for arrays

# make an array of the 20 marks
marks = np.array(
    [85, 67, 92, 74, 58, 79, 88, 71, 95, 63,
     81, 76, 69, 90, 54, 83, 77, 89, 61, 84]
)

# data type of the array (should be one type)
print(marks.dtype)
# mean, median, standard deviation
print(np.mean(marks), np.median(marks), np.std(marks))
# lowest and highest mark
print(marks.min(), marks.max())

# keep only marks that are 75 or more (distinction)
print(marks[marks >= 75])
# how many distinctions
print(len(marks[marks >= 75]))

# 89th percentile VALUE (the score at that percentile)
print(np.percentile(marks, 89))
# percentile RANK of score 89 (% of scores <= 89)
print((marks <= 89).sum() / len(marks) * 100)

# index of the highest mark, and the value
print(np.argmax(marks), marks.max())
