# Creating a set
phonebook = {'Chris': '555-1111', 'Katie':'555-2222','Joanne':'555-3333'}
# Adding a key and value
phonebook["Kathryn"] = "555-1203"
print(phonebook)
# displaying values
print(phonebook["Chris"])
print(phonebook["Katie"])
print(phonebook["Joanne"])
print(phonebook["Kathryn"])


# delete function
del phonebook["Joanne"]

# Checking what is in and what is not in
if "Joanne" not in phonebook:
    print("Joanne wasn't found")

if "Chris" in phonebook:
    print(phonebook["Chris"])

# Using loops
for key in phonebook:
    print(key)
test_scores = { "Kayla":[88,92,100],"Luis":[95,74,81],"Sophie":[72,88,91],"Ethan":[70,75,78]}
print(test_scores)

kalya_scores = test_scores["Kayla"]
print(kalya_scores)


# myset= set('abc')
# print(myset)

# myset=set()
# myset.add(1)
# myset.add(2)
# myset.add(3)
# # appended to previous set
# myset.update([4,5,6])
# # remove
# # myset.remove()
# print(myset)
#
# # clear method
# myset.clear()
# print(myset)

# in or not in
# myset=set([1,2,3])
# # if 99 not in myset:
# #     print("99 is not in set")
# if 1 in myset:
#     print("1 is in set")









