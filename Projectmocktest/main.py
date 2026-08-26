# result=0
# elements=[1,2,3,5]
# for element in len(elements):
#     element+=1
#     result+=element
# print("The sum of all the elements in the list is:",result)

# Initialize a variable to store the sum of elements
result = 0

# Create a 1D list of elements
elements = [1, 2, 3, 5]

# Iterate through each element in the list
for element in elements:
    # Add the current element to the result
    result += element

# Print the sum of all elements in the list
print("The sum of all the elements in the list is:", result)

# # Initialize a variable to store the sum of elements
# total = 0
#
# # Create a 1D list of elements
# numbers = [1, 2, 3, 5]
#
# # Iterate through each element in the list
# for number in numbers:
#     # Add the current element to the result
#     total += numbers
#     avg=total/number
#
# # Print the sum of all elements in the list
# print("The avg of all the elements in the list is:", avg)

# Initialize a variable to store the sum of elements
total = 0

# Create a 1D list of elements
numbers = [1, 2, 3, 5]

# Iterate through each element in the list
for number in numbers:
    # Add the current element to the total
    total += number

# Calculate the average by dividing the total by the number of elements
avg = total / len(numbers)

# Print the average of all elements in the list
print("The average of all the elements in the list is:", avg)

# students={"Jake":59,"Billy":62,"Jerry":63}
# for student in students:

# Initialize a dictionary to store student information (name: score)
students = {"Jake": 59, "Billy": 62, "Jerry": 63}

# Function to add a new student with a score
def add_student(name, score):
    students[name] = score
    print(f"{name} has been added with a score of {score}.")

# Function to update a student's score
def update_score(name, new_score):
    if name in students:
        students[name] = new_score
        print(f"{name}'s score has been updated to {new_score}.")
    else:
        print(f"{name} is not in the list of students.")

# Function to find the student with the highest score
def find_highest_score_student():
    if not students:
        print("No students in the list.")
    else:
        highest_score_student = max(students, key=students.get)
        print(f"The student with the highest score is {highest_score_student} with a score of {students[highest_score_student]}.")

# Original 2D list
original = [
    [1, 2, 3],
    [4, 5, 6],
]

# Transpose the 2D list
transposed = [[row[i] for row in original] for i in range(len(original[0]))]

# Print the transposed list
for row in transposed:
    print(row)


# Example usage:
add_student("Alice", 95)
update_score("Jake", 75)
find_highest_score_student()

# Initialize an empty inventory dictionary
inventory = {}

# Function to add items to the inventory
def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"{quantity} {item_name}(s) added to inventory.")

# Function to update item quantities
def update_quantity(item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
        print(f"Updated quantity of {item_name} to {new_quantity}.")
    else:
        print(f"{item_name} is not in the inventory.")

# Function to display the current inventory
def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Example usage:
add_item("Apples", 50)
add_item("Bananas", 30)
update_quantity("Apples", 75)
display_inventory()



def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(original_list)
print(result_list)
