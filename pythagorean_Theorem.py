# Tik Tok: Part 1

# def pythag(a, b):
#    return (a**2 + b**2)**0.5

#a = int(input("Enter the value of a: "))
#b = int(input("Enter the value of b: "))
#print("The value c is: ", pythag(a, b))

#sudo code
#1. Define a function called pythag that takes two inputs, a and b
#2. The function should return the square root of a squared plus b squared
#3. Take an integer input a and b from the user.
#4. Call the function "pythag" and print the result
#5. End

#Tik Tok: Part 2

a = int(input("If their is no side A put 0 \n Enter the value of a (): "))
b = int(input("If their is no side B put 0 \n Enter the value of b (): "))
C = int(input("If their is no side C put 0 \n Enter the value of c (): "))

def LegA(c, b):
    return (c**2 - b**2)**0.5

def LegB(c, a):
    return (c**2 - a**2)**0.5

def LegC(a, b):
    return (a**2 + b**2)**0.5

if a == 0:
    print("The value of a is: ", LegA(c, b))
elif b == 0:
    print("The value of b is: ", LegB(c, a))
else:
    print("The value of c is: ", LegC(a, b))

#sudo code
#1. Take an integer input a, b, and c from the user.
#2. Define a function called LegA that takes two inputs, c and b
#3. The function should return the square root of c squared minus b squared
#4. Define a function called LegB that takes two inputs, c and a
#5. The function should return the square root of c squared minus a squared
#6. Define a function called LegC that takes two inputs, a and b
#7. The function should return the square root of a squared plus b squared
#8. If a is 0, call the function LegA and print the result
#9. If b is 0, call the function LegB and print the result
#10. If c is 0, call the function LegC and print the result
#11. End
