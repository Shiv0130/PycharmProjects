# tuples
my_tuple=(1,2,3,4)
print(my_tuple)

# Iteration using tuples
names=("Bob","Mary","Smith")
for n in names:
    print(n)

# Converting between lists and tuples
# tuples to list
number_tuple = (1, 2, 3)
number_list = list(number_tuple)
print(number_list)
# [list] to (tuples)
str_list = ['one', 'two', 'three']
str_tuple = tuple(str_list)
print(str_tuple)

fruits =("apple","banana","cherry","Pomegranete")
green,yellow,*red = fruits
print(green)
print(yellow)
print(red)







