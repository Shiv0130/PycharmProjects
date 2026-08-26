#Q1
#a.Given the list = [1,2,3,1,4,1,5,1,6] find the number of occurences for 1:

# Initialize a variable to store the count of occurrences of the number 1.
count=0

# Given list of numbers.
nums=[1,2,3,1,4,1,5,1,6]

# Count the number of occurrences of the value 1 in the list.

count=nums.count(1)

# Print the result indicating the number of occurrences of 1.
print("The number of occurences for 1 is:",count)

#b.sort the list and return the sorted list

#
# # Bubble sort implementation using a for loop
# for i in range(len(nums)):
#     # Inner loop iterates through the unsorted portion of the list
#     # In each iteration, the largest element 'bubbles up' to its correct position
#     for j in range(0, len(nums) - i - 1):
#         # Compare adjacent elements
#         if nums[j] > nums[j + 1]:
#             # Swap the elements if they are out of order
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#
# # Print the sorted list
# print("The sorted list is:", nums)

# Sort the given list in ascending order and store the sorted list in 'list'.
# Note: Avoid using variable names like 'list' since it's a built-in type name.
list=sorted(nums)
print("The list sorted out displays:",list)



#Q2
#with the 2 lists given below, find the common elements and print them
#list1=[10,20,50,75,80,92,100]
#list2=[10,50,75]

list1=[10,20,50,75,80,92,100]
list2=[10,50,75]
#
# for i in list1:
#     for j in list2:
#         if list1[i]==list[j]:

#How to have done the above method correctly:

common_elements = []

# Nested loop approach to compare elements
# Given two lists.
list1 = [10, 20, 50, 75, 80, 92, 100]
list2 = [10, 50, 75]

# # Initialize an empty list to store the common elements.
# common_elements = []
#
# # Nested loop approach to compare elements
# # Iterate through the indices of list1.
# for i in range(len(list1)):
#     # Nested loop: Iterate through the indices of list2 for every index in list1.
#     for j in range(len(list2)):
#         # Check if the element in list1 at index i is the same as the element in list2 at index j.
#         if list1[i] == list2[j]:
#             # If they are the same, add the common element to the common_elements list.
#             common_elements.append(list1[i])
#
# # Print the list of common elements found between the two lists.
# print("The common elements between the two lists are:", common_elements)



# Initialize an empty list to store the common elements.
common_elements = []

# Iterate through the elements in the first list.
for element in list1:
    # Check if the current element exists in the second list.
    if element in list2:
        # If it does, add it to the common_elements list.
        common_elements.append(element)

# Print the list of common elements found between the two lists.
print("The common elements between the two lists are:", common_elements)


#Q3
#Multiply all the elements in the list
#numbers=[20,40,80,90]
result=1
numbers=[20,40,80,90]
for i in numbers:
    result*=i
print("The multiplication of numbers in elements is",result)
