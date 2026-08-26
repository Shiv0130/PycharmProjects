file=open("secrets.txt","w")
file.write("I am Iron Man:)\n")
file.close()

file=open("secrets.txt","r")
contents=file.read()
print(contents)
file.close()

with open("secrets.txt",'a') as file:
    file.write("It's beliveable right?")
with open("secrets.txt",'r') as file:
    text=file.read()
    print(text)
    file.close()

file=open("calculations.txt","w")
file.write(str(2)+"\n")
file.write(str(1)+"\n")
file.write(str(4)+"\n")

file=open("calculations.txt",'r')
sum=0

for line in file:

    line=float(line.rstrip("\n"))
    sum+=line
print("The sum of  the numbers in this file is:",sum)

file.close()

with open("zoomcall.txt","r") as file:
    contents=file.readline()
print(contents)

