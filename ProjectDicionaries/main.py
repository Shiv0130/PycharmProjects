people={"name":"Raymond","name1":"Sally","name2":"Mark",
        "surname":"Jones","surname1":"Khumalo","surname2":"Jones",
        "ID":"411123111",
        "cellphone":"071311413"}

people["address"]="47JonesAve"
# check this one out
people["cellphone"]="063124125"

print(people)

x=people.keys()
print(x)

y=people.values()
print(y)

#If you had to add another employees information in the same dictionary:the company has hired two more people
# "Sally" "Mark"  "Khumalo" "Jones" and other values can be anything

#Search if there is a person called Mark Jones in the dictionary.
for key, value in people.items():
    if "Mark" in value and "Jones" in value:
        print("Mark Jones found.")
        break
else:
    print("Mark Jones not found.")

# change address to 45 Wentworth Road
for key, value in people.items():
    if "Mark" in value and "Jones" in value:
        people[key.replace("name", "address")] = "45 Wentworth Road"
        break




