import matplotlib.pyplot as plt  # plotting library

# categories and their averages
subjects = ["Math", "Science", "English"]
avg_marks = [82.1, 75.4, 73.0]

# make a figure (canvas) size 8 by 5
fig, ax = plt.subplots(figsize=(8, 5))
# vertical bars
ax.bar(subjects, avg_marks, color="teal")
# axis labels and title
ax.set_xlabel("Subject")
ax.set_ylabel("Average marks")
ax.set_title("Average marks by subject")
# light grid on y axis
ax.grid(True, axis="y", linestyle="--", alpha=0.6)
# show the bar chart
plt.show()

# sample hours and scores for scatter
hours = [12, 6, 14, 8, 4, 10, 11, 7, 16, 5]
scores = [85, 67, 92, 74, 58, 79, 88, 71, 95, 63]

# new figure size 10 by 6
plt.figure(figsize=(10, 6))
# scatter with triangle markers
plt.scatter(hours, scores, marker="^", color="purple")
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.title("Study hours vs marks")
plt.grid(True, linestyle="--", alpha=0.6)
# show the scatter
plt.show()
