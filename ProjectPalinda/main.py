# #Check if a string is a palindrome
#
# string1=input("Enter string:")
# string2=input("Enter string:")
# iLen1=len(string1)
# iLen2=len(string2)
# for i in range(1,iLen1):
#     for j in range (iLen2,-1):
#         if string1==string2:
#             print("This is a Palindrome")
#         else:
#             print("Isn't a palindrome")
string = input("Enter string:")
is_palindrome = True

for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")


