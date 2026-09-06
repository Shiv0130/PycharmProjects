# import numpy as np
# from numpy.ma.extras import median
#
# test_scores = [85, 92, 78, 65, 88, 95, 74, 89, 70, 85]
# #a.
# arr_test_scores = np.array(test_scores)
#
# mean = np.mean(test_scores)
# print(f"a.Mean is:{mean}")
#
# median = np.median(test_scores)
# print(f" Median is: {median}")
#
# std_dev = np.std(test_scores)
# print(f"Std deviation is:{std_dev:.1f}")
#
# count = 0
# for i in range(len(arr_test_scores)):
#     if(arr_test_scores[i]>80):
#         count+=1
# print(f"The amount of scores above 80 is:{count}")
#
# #percentile rank
# percentile = np.percentile(test_scores,89)
# print(f"The percentile rank of 89 is: {percentile}")

import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = np.array([12000, 13500, 15000, 14200, 16000, 17500,
                   18200, 17000, 19500, 21000, 22500, 25000])

# a. months with sales above the yearly average
yearly_average = np.mean(sales)
above_average_mask = sales > yearly_average
above_average_months = np.array(months)[above_average_mask]

print(f"a. Yearly average sales: {yearly_average:.2f}")
print(f"   Months above average: {above_average_months.tolist()}")

# b. quarter-over-quarter growth rate
quarterly_sales = sales.reshape(4, 3).sum(axis=1)
growth_rate = (quarterly_sales[1:] - quarterly_sales[:-1]) / quarterly_sales[:-1] * 100

print(f"\nb. Quarterly totals: {quarterly_sales}")
print(f"   Quarter-over-quarter growth rate (%): {np.round(growth_rate, 2)}")

# c. peak sales month and its value
peak_index = np.argmax(sales)
peak_month = months[peak_index]
peak_value = sales[peak_index]

print(f"\nc. Peak sales month: {peak_month} (R{peak_value})")