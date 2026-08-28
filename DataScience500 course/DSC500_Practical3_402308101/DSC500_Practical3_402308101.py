# DATA SCIENCE 500 - PRACTICAL 3
# Student: Shivaar
# Student number: 402308101

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker   # lets us format axis values as currency
import pandas as pd

# Load the retail dataset. This file must sit in the same folder as this
# script (or the path below needs to be updated) for pd.read_csv to find it.
df = pd.read_csv("Data_Science_500_Practical_3_Retail_Dataset.csv")


# ======================================================================
# QUESTION 1 - Line graph of sales_2026 across six months
# ======================================================================
# matplotlib.pyplot is already imported above as plt (that satisfies the
# "import using the alias plt" instruction).

months = ["January", "February", "March", "April", "May", "June"]
sales_2025 = [120000, 135000, 128000, 142000, 150000, 160000]
sales_2026 = [130000, 145000, 138000, 155000, 165000, 178000]

plt.figure(figsize=(8, 5))
# marker="o" -> circle markers, color="green" -> green line, as required
plt.plot(months, sales_2026, marker="o", color="green")
plt.title("2026 Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (R)")
plt.grid(True)              # gridlines
plt.tight_layout()
plt.show()


# ======================================================================
# QUESTION 2 - Bar chart of units sold per product
# ======================================================================
products = ["Laptops", "Smartphones", "Tablets", "Accessories"]
units_sold_by_product = [320, 450, 275, 510]
# One colour per bar, picked manually so every bar is visually distinct
bar_colours = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

plt.figure(figsize=(8, 5))
bars = plt.bar(products, units_sold_by_product, color=bar_colours)

# Loop through the Bar objects returned by plt.bar() so we can read each
# bar's height and place a text label just above it.
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # centre the label horizontally on the bar
        height + 5,                          # sit just above the top of the bar
        str(height),
        ha="center", va="bottom"
    )

plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()


# ======================================================================
# QUESTION 3 - Scatter plot: hours studied vs test scores
# ======================================================================
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [42, 50, 55, 60, 63, 70, 75, 78, 85, 90]

plt.figure(figsize=(8, 5))
plt.scatter(hours_studied, test_scores, marker="^")   # "^" = triangular markers
plt.title("Hours Studied vs Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.tight_layout()
plt.show()

print("Q3: The scatter plot shows a clear positive relationship - as the "
      "number of hours studied increases, test scores also increase in a "
      "fairly consistent, near-linear pattern.")


# ======================================================================
# QUESTION 4 - One figure, two subplots (2025 vs 2026)
# ======================================================================
# plt.subplots(1, 2, ...) creates one figure with a 1-row-by-2-column grid
# of axes, returned as (fig, (ax1, ax2)) so we can address each side
# separately.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(months, sales_2025, color="blue", marker="o")
ax1.set_title("2025 Sales")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales (R)")

ax2.plot(months, sales_2026, color="green", marker="o")
ax2.set_title("2026 Sales")
ax2.set_xlabel("Month")
ax2.set_ylabel("Sales (R)")

plt.tight_layout()   # stops the two subplot titles/labels overlapping
plt.show()


# ======================================================================
# QUESTION 5 - Single comparison line graph (2025 vs 2026)
# ======================================================================
plt.figure(figsize=(8, 5))
plt.plot(months, sales_2025, marker="o", color="blue", label="2025")
plt.plot(months, sales_2026, marker="o", color="green", label="2026")
plt.title("2025 vs 2026 Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (R)")
plt.legend()          # uses the label= values set above
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_comparison.png")   # exact filename required by the brief
plt.show()

total_2025 = sum(sales_2025)
total_2026 = sum(sales_2026)
print(f"Q5: Total 2025 sales: R{total_2025:,} | Total 2026 sales: R{total_2026:,}")
print("Q5: 2026 performed better overall, since total sales across the six "
      "months are higher than in 2025.")


# ======================================================================
# QUESTION 6 - Monthly revenue trend (real retail dataset)
# ======================================================================
# Group by both Month_Number and Month together: Month_Number lets us sort
# the months in calendar order (sorting "Month" alphabetically would put
# April before January, which is wrong), while Month gives us the readable
# label to plot on the x-axis.
monthly_revenue = (
    df.groupby(["Month_Number", "Month"])["Sales_Revenue"]
    .sum()
    .reset_index()
    .sort_values("Month_Number")
)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(monthly_revenue["Month"], monthly_revenue["Sales_Revenue"],
        marker="o", color="darkgreen", linestyle="-")

# Print the revenue value just above every point on the line
for x_val, y_val in zip(monthly_revenue["Month"], monthly_revenue["Sales_Revenue"]):
    ax.text(x_val, y_val + 60000, f"R{y_val:,.0f}", ha="center", fontsize=8)

# Find and highlight the month with the highest total revenue in red
max_row = monthly_revenue.loc[monthly_revenue["Sales_Revenue"].idxmax()]
ax.plot(max_row["Month"], max_row["Sales_Revenue"], marker="o", color="red",
        markersize=11, zorder=5)   # zorder=5 draws this marker on top of the line

# FuncFormatter lets us rewrite every y-axis tick as Rand currency
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, pos: f"R{v:,.0f}"))

ax.set_title("Total Monthly Sales Revenue (All Branches)")
ax.set_xlabel("Month")
ax.set_ylabel("Total Sales Revenue")
ax.grid(True)
plt.xticks(rotation=45)   # angle the month labels so they don't overlap
plt.tight_layout()
plt.show()

print(f"Q6: Highest revenue month: {max_row['Month']} (R{max_row['Sales_Revenue']:,.0f})")
print("Q6: Overall, monthly revenue shows a steady upward trend across the "
      "year, rising from January through to a peak in December.")


# ======================================================================
# QUESTION 7 - Branch revenue and expenses comparison
# ======================================================================
branch_summary = df.groupby("Branch")[["Sales_Revenue", "Operating_Expenses"]].sum()
# Profit is a new column we calculate ourselves from the two totals above
branch_summary["Profit"] = branch_summary["Sales_Revenue"] - branch_summary["Operating_Expenses"]
print("Q7 branch summary:\n", branch_summary)

branches = branch_summary.index.tolist()
x_positions = range(len(branches))
bar_width = 0.35   # width of each individual bar in the grouped pair

fig, ax = plt.subplots(figsize=(10, 6))
# Shift the revenue bars left and the expense bars right so each branch
# gets a side-by-side pair instead of the bars overlapping.
revenue_bars = ax.bar([i - bar_width / 2 for i in x_positions],
                       branch_summary["Sales_Revenue"], width=bar_width,
                       color="#4C72B0", label="Sales Revenue")
expense_bars = ax.bar([i + bar_width / 2 for i in x_positions],
                       branch_summary["Operating_Expenses"], width=bar_width,
                       color="#C44E52", label="Operating Expenses")

# Value labels above every bar (both revenue and expense bars)
for bar_group in (revenue_bars, expense_bars):
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f"R{height:,.0f}",
                ha="center", va="bottom", fontsize=8, rotation=90)

ax.set_xticks(list(x_positions))
ax.set_xticklabels(branches)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, pos: f"R{v:,.0f}"))
ax.set_title("Branch Revenue vs Operating Expenses")
ax.set_xlabel("Branch")
ax.set_ylabel("Amount (R)")
ax.legend()
plt.tight_layout()
plt.show()

top_profit_branch = branch_summary["Profit"].idxmax()
print(f"Q7: Branch with the highest total profit: {top_profit_branch} "
      f"(R{branch_summary['Profit'].max():,.0f})")


# ======================================================================
# QUESTION 8 - Customer satisfaction vs product returns
# ======================================================================
fig, ax = plt.subplots(figsize=(10, 6))   # custom figure size, as required

# A fixed colour per branch, defined once as a dictionary so Q8 and Q9 stay
# visually consistent with each other.
branch_colours = {
    "Durban": "#4C72B0",
    "Johannesburg": "#DD8452",
    "Cape Town": "#55A868",
    "Online": "#C44E52",
}

# Plot one branch at a time so each gets its own colour and legend entry
for branch_name, colour in branch_colours.items():
    branch_data = df[df["Branch"] == branch_name]
    ax.scatter(branch_data["Satisfaction_Score"], branch_data["Returns"],
               color=colour, label=branch_name)

# Find and annotate the single row with the highest number of returns
max_returns_row = df.loc[df["Returns"].idxmax()]
ax.annotate(
    f"{max_returns_row['Branch']} ({max_returns_row['Month']})\n"
    f"Highest returns: {max_returns_row['Returns']}",
    xy=(max_returns_row["Satisfaction_Score"], max_returns_row["Returns"]),   # point being labelled
    xytext=(max_returns_row["Satisfaction_Score"] - 0.3, max_returns_row["Returns"] + 2),  # label position
    arrowprops=dict(arrowstyle="->", color="black"),
)

ax.set_title("Customer Satisfaction vs Product Returns")
ax.set_xlabel("Satisfaction Score")
ax.set_ylabel("Returns")
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()

correlation = df["Satisfaction_Score"].corr(df["Returns"])
print(f"Q8: Correlation between Satisfaction_Score and Returns: {correlation:.2f}")
print("Q8: Yes - higher satisfaction scores are associated with fewer "
      "returns. The scatter plot slopes downward, and the correlation "
      "coefficient is negative, confirming that as satisfaction increases, "
      "returns tend to decrease.")


# ======================================================================
# QUESTION 9 - Branch performance dashboard (2x2 subplot grid)
# ======================================================================
branch_order = ["Durban", "Johannesburg", "Cape Town", "Online"]
branch_line_colours = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()   # turns the 2x2 array of axes into a simple flat list of 4

# Work out one shared upper y-limit up front so all four subplots use the
# same scale, making them directly comparable at a glance.
shared_max = df.groupby(["Branch", "Month_Number"])["Sales_Revenue"].sum().max()

for ax, branch_name, colour in zip(axes, branch_order, branch_line_colours):
    branch_monthly = (
        df[df["Branch"] == branch_name]
        .groupby(["Month_Number", "Month"])["Sales_Revenue"]
        .sum()
        .reset_index()
        .sort_values("Month_Number")   # keep months in calendar order
    )
    ax.plot(branch_monthly["Month"], branch_monthly["Sales_Revenue"],
            marker="o", color=colour)
    ax.set_title(branch_name)
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales Revenue (R)")
    ax.set_ylim(0, shared_max * 1.1)   # same y-axis scale on every subplot
    ax.grid(True)
    ax.tick_params(axis="x", rotation=45)

fig.suptitle("Branch Performance Dashboard - Monthly Sales Revenue")
plt.tight_layout()   # prevents the subplot titles/labels from overlapping
plt.show()


# ======================================================================
# QUESTION 10 - Product-category performance report
# ======================================================================
category_summary = df.groupby("Product_Category")[["Units_Sold", "Sales_Revenue", "Returns"]].sum()
print("Q10 category summary:\n", category_summary)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left subplot: bar chart of total revenue by category
ax1.bar(category_summary.index, category_summary["Sales_Revenue"], color="#4C72B0")
ax1.set_title("Total Sales Revenue by Product Category")
ax1.set_xlabel("Product Category")
ax1.set_ylabel("Sales Revenue (R)")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, pos: f"R{v:,.0f}"))
ax1.grid(True, axis="y")

# Right subplot: line graph comparing units sold and returns by category
ax2.plot(category_summary.index, category_summary["Units_Sold"],
         marker="o", color="green", label="Units Sold")
ax2.plot(category_summary.index, category_summary["Returns"],
         marker="s", color="red", label="Returns")
ax2.set_title("Units Sold vs Returns by Product Category")
ax2.set_xlabel("Product Category")
ax2.set_ylabel("Count")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("product_performance_report.png")   # exact filename required by the brief
plt.show()

print("Q10: Highest revenue category:", category_summary["Sales_Revenue"].idxmax())
print("Q10: Highest units sold category:", category_summary["Units_Sold"].idxmax())
print("Q10: Highest returns category:", category_summary["Returns"].idxmax())
