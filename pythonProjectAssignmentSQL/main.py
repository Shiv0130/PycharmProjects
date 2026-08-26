import sqlite3

# Function to create the database and table
def create_database():

    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()

    # Create the Cities table with the specified columns
    cursor.execute("CREATE TABLE IF NOT EXISTS Cities (CityName TEXT PRIMARY KEY, CityID INTEGER, Population REAL)")
    cursor.execute("INSERT INTO Cities (CityName, CityID, Population) VALUES ('New York', 512, 5000000.21)")
    cursor.execute("INSERT INTO Cities (CityName, CityID, Population) VALUES ('Durban', 511, 4000000.12)")
    cursor.execute("INSERT INTO Cities (CityName, CityID, Population) VALUES ('China', 513, 3000000000.03)")

    connection.commit()
    connection.close()


# Function to display a list of cities sorted by population in ascending order
def display_cities_ascending():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()

    # Retrieve cities sorted by population in ascending order
    cursor.execute("SELECT * FROM Cities ORDER BY Population ASC")
    cities = cursor.fetchall()

    # Print the sorted cities
    for city in cities:
        print(f"City: {city[0]}, Population: {city[2]}")

    connection.close()


# Function to display a list of cities sorted by population in descending order
def display_cities_descending():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()

    # Retrieve cities sorted by population in descending order
    cursor.execute("SELECT * FROM Cities ORDER BY Population DESC")
    cities = cursor.fetchall()

    # Print the sorted cities
    for city in cities:
        print(f"City: {city[0]}, Population: {city[2]}")

    connection.close()


# Function to display a list of cities sorted by name
def display_cities_by_name():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()

    # Retrieve cities sorted by name
    cursor.execute("SELECT * FROM Cities ORDER BY CityName")
    cities = cursor.fetchall()

    # Print the sorted cities
    for city in cities:
        print(f"City: {city[0]}, Population: {city[2]}")

    connection.close()


# Function to display the total population of all cities
def display_total_population():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()

    # Calculate the total population
    cursor.execute("SELECT SUM(Population) FROM Cities")
    total_population = cursor.fetchone()[0]

    print(f"Total Population: {total_population}")

    connection.close()


# Function to display the average population of all cities
def display_average_population():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()

    # Calculate the average population
    cursor.execute("SELECT AVG(Population) FROM Cities")
    average_population = cursor.fetchone()[0]

    print(f"Average Population: {average_population}")

    connection.close()


# Function to display the city with the highest population
def display_highest_population():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()

    # Retrieve the city with the highest population
    cursor.execute("SELECT * FROM Cities ORDER BY Population DESC LIMIT 1")
    city = cursor.fetchone()

    print(f"City with Highest Population: {city[0]}, Population: {city[2]}")

    connection.close()


# Function to display the city with the lowest population
def display_lowest_population():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()

    # Retrieve the city with the lowest population
    cursor.execute("SELECT * FROM Cities ORDER BY Population ASC LIMIT 1")
    city = cursor.fetchone()

    print(f"City with Lowest Population: {city[0]}, Population: {city[2]}")

    connection.close()


# Main program
if __name__ == "__main__":
    create_database()

    while True:
        print("\nOptions:")
        print("1. Display cities sorted by population (ascending)")
        print("2. Display cities sorted by population (descending)")
        print("3. Display cities sorted by name")
        print("4. Display total population of all cities")
        print("5. Display average population of all cities")
        print("6. Display city with the highest population")
        print("7. Display city with the lowest population")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_cities_ascending()
        elif choice == "2":
            display_cities_descending()
        elif choice == "3":
            display_cities_by_name()
        elif choice == "4":
            display_total_population()
        elif choice == "5":
            display_average_population()
        elif choice == "6":
            display_highest_population()
        elif choice == "7":
            display_lowest_population()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")