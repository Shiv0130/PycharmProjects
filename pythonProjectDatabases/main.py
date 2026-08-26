# Import the sqlite3 module to work with SQLite databases
import sqlite3

# Connect to the SQLite database 'users.db' or create it if it doesn't exist
connection = sqlite3.connect("users.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table named 'user' if it doesn't exist with three columns: name, password, and age
cursor.execute("CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, age INTEGER)")

# Add users to the 'user' table
cursor.execute("INSERT INTO user VALUES ('John', 'password-john50', 50)")
cursor.execute("INSERT INTO user VALUES ('George', 'password-George45', 45)")
cursor.execute("INSERT INTO user VALUES ('Jeff', 'password-jeff25', 25)")

# Retrieve data from the 'user' table
cursor.execute("SELECT * FROM user")

# Fetch all the rows from the result set
results = cursor.fetchall()

# Iterate through the results and print name and age
for row in results:
    print('Name:', row[0])
    print('Password:', row[2])

# Commit the changes to the database
connection.commit()

# Close the database connection
connection.close()



# my way
# import sqlite3
#
# conn=sqlite3.connect("chocolates.db")
#
# cursor=conn.cursor()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS chocolates(Choc_ID INTEGER PRIMARY KEY NOT NULL, Choc_flavor TEXT, Choc_brand TEXT)")
#
# cursor.execute("INSERT INTO chocolates VALUES(1,'milk','KitKat')")
# cursor.execute("INSERT INTO chocolates VALUES(2,'dark','Cadbury')")
# cursor.execute("INSERT INTO chocolates VALUES(3,'Vanila','TVbar')")
#
# cursor.execute("SELECT * FROM chocolates")
#
# results = cursor.fetchall()
#
# for record in results:
#     print("Choc_ID:",record[0])
#     print("Choc_flavor:",record[1])
#     print("Choc_brand:",record[2])
# conn.commit()
# conn.close()


# # correct way with some altercations
# import sqlite3
#
# conn = sqlite3.connect("chocolates.db")
# cursor = conn.cursor()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS chocolates (Choc_ID INTEGER PRIMARY KEY NOT NULL, Choc_flavor TEXT, Choc_brand TEXT)")
#
# cursor.execute("INSERT INTO chocolates VALUES(24,'milk','KitKat')")
# cursor.execute("INSERT INTO chocolates VALUES(25,'dark','Cadbury')")
# cursor.execute("INSERT INTO chocolates VALUES(26,'Vanilla','TVbar')")
#
#
# cursor.execute("SELECT * FROM chocolates")
# cursor.execute("SELECT * FROM chocolates ORDER BY Choc_ID Desc")
# # cursor.execute("Update chocolates SET Choc_flavour =dark where Choc_brand=""KitKat and Choc_ID=21" )
# cursor.execute("UPDATE chocolates SET Choc_flavor = 'dark' WHERE Choc_brand = 'KitKat' AND Choc_ID = 21")
#
#
# results = cursor.fetchall()
#
# for record in results:
#     print("Choc_ID:", record[0])
#     print("Choc_flavor:", record[1])
#     print("Choc_brand:", record[2])
#
# conn.commit()
# conn.close()
#
#
# import sqlite3
#
# conn = sqlite3.connect("chocolates.db")
# cursor = conn.cursor()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS chocolates (Choc_ID INTEGER PRIMARY KEY NOT NULL, Choc_flavor TEXT, Choc_brand TEXT)")
#
# # Insert data with unique Choc_ID values
# cursor.execute("INSERT INTO chocolates VALUES(21, 'milk', 'KitKat')")
# cursor.execute("INSERT INTO chocolates VALUES(22, 'dark', 'Cadbury')")
# cursor.execute("INSERT INTO chocolates VALUES(23, 'Vanilla', 'TVbar')")
#
# # Update an existing record
# cursor.execute("UPDATE chocolates SET Choc_flavor = 'dark' WHERE Choc_brand = 'KitKat' AND Choc_ID = 21")
#
# cursor.execute("SELECT * FROM chocolates")
#
# results = cursor.fetchall()
#
# for record in results:
#     print("Choc_ID:", record[0])
#     print("Choc_flavor:", record[1])
#     print("Choc_brand:", record[2])
#
# conn.commit()
# conn.close()



# Creating a table
# import sqlite3
#
# connection=sqlite3.connect('contacts.db')
# cursor=connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS contacts(Name TEXT ,PhoneNumber TEXT)")
# connection.commit()
# connection.close()

# import sqlite3
#
# def main():
#     connection = sqlite3.connect("inventory.db")
#     cursor = connection.cursor()
#
#     cursor.execute("CREATE TABLE IF NOT EXISTS inventory (ItemName TEXT, Price REAL)")
#
#     again = 'yes'
#     while again == 'yes':
#         item_name = input("Item Name: ")
#         price = float(input('Price: '))
#         cursor.execute("INSERT INTO inventory (ItemName, Price) VALUES (?, ?)", (item_name, price))
#         again = input("Add another item? (yes/no): ")
#
#     connection.commit()
#     connection.close()
#
# if __name__ == '__main__':
#     main()


# Correct code
# import sqlite3
#
# def main():
#     connection = sqlite3.connect("inventory.db")
#     cursor = connection.cursor()
#
#     cursor.execute("CREATE TABLE IF NOT EXISTS inventory (ItemName TEXT, Price REAL)")
#
#     while True:
#         item_name = input("Item Name: ")
#         price = float(input('Price: '))
#         cursor.execute("INSERT INTO inventory (ItemName, Price) VALUES (?, ?)", (item_name, price))
#         again = input("Add another item? (yes/no): ")
#         if again.lower() != 'yes':
#             break
#
#     connection.commit()
#     connection.close()
#
# if __name__ == '__main__':
#     main()



# SQL SELECT statements

# import sqlite3
#
# def main():
#     conn = sqlite3.connect("chocolate.db")
#     cursor = conn.cursor()
#
#     cursor.execute("CREATE TABLE IF NOT EXISTS chocolate (Description TEXT, RetailPrice REAL, Products TEXT)")
#
#     cursor.execute("INSERT INTO chocolate (PRODUCTID INTEGER PRIMARY KEY NOT NULL,Description, RetailPrice, Products) VALUES ('Product is amazing', 6.99, 'KitKat')")
#
#     description = "Product is amazing"
#     retail = float(input("Enter a price:"))
#     product = input("Product name:")
#
#     cursor.execute("INSERT INTO chocolate (Description, RetailPrice, Products) VALUES (?, ?, ?)", (description, retail, product))
#
#     cursor.execute("SELECT Description, RetailPrice, Products FROM chocolate")
#     results = cursor.fetchall()
#
#     for row in results:
#         print("Description:", row[0])
#         print("RetailPrice:", row[1])
#         print("Products:", row[2])
#
#     conn.commit()
#     conn.close()
#
# if __name__ == '__main__':
#     main()


# import sqlite3
#
# def main():
#     conn = sqlite3.connect("chocolates.db")  # Use the correct database name
#     cursor = conn.cursor()
#     pID = input("Enter a Product ID:")
#
#     cursor.execute("SELECT Description, RetailPrice FROM Products WHERE ProductID = ?", (pID,))  # Corrected the SELECT statement
#     results = cursor.fetchone()  # Use fetchone() to get a single result
#
#     if results is not None:  # Check if a record was found
#         print(f"The current price for {results[0]} is ${results[1]:.2f}")
#         new_price = float(input("Enter new price: "))
#
#         cursor.execute("UPDATE Products SET RetailPrice = ? WHERE ProductID = ?", (new_price, pID))
#         conn.commit()
#         conn.close()
#     else:
#         print(f"No product found with ProductID {pID}")
#
# if __name__ == '__main__':
#     main()
