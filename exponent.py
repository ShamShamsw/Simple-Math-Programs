def exponent(n):
    for i in range(n+1):
        i = i**2
        print(i)
        i+=1
    
n = int(input("Enter a number: "))
print(exponent(n))

#sudo code
#1. Define a function exponent that takes an integer input n.
#2. Initialize a loop that iterates from 0 to n.
#3. Within the loop, calculate the square of the current iteration value and store it in a variable.
#4. Print the squared value.
#5. add 1 to the variable and end the iteratation.
#5. Call the exponent function with n as the argument and print the result.
#6. End.
