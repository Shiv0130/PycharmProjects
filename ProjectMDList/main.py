# multi diementional and list
# 1) Create an empty list
# 2) for loop = rows
# 3)nest the loop = cols
# 4)deal with the first row with their cols
# 5) print main list

# Define a function named create_list that takes two parameters: rows and cols
def create_list(rows,cols):
    # Initialize an empty list to store the final multi-dimensional list
    list = []
    # Loop through the rows using the range function
    for rows in range(rows):
        # Initialize an empty list for each row
        list_row = []
        # Loop through the columns using the range function
        for cols in range(cols):
            # Prompt the user to enter a number and store it in the content variable
            content = input("please enter the number for the row{} and cols}:").format(rows, cols)
            # Append the entered content to the row_list
            list_row.append(content)
            # After looping through the columns, append the row_list to the main_list
        list.append(list_row)
        # Return the main_list, which now holds the complete multi-dimensional list
    return list

# Prompt the user to enter the number of rows and columns
rowss = int(input("please enter the nember of rows:"))
colss = int(input("please enter the nember of cols: "))

# Call the create_list function and store the result in the create_list variable
create_list = create_list(rowss,colss)
# Print the elements in the resulting multi-dimensional list
print("The elements in the list:",create_list)