def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter a number: "))
print(fibonacci(n))

#summary
# This program takes an integer input n and returns the nth Fibonacci number using a recursive definition.
# The recursive definition for the Fibonacci sequence is as follows:
# - The first two Fibonacci numbers are 0 and 1.
# - Any Fibonacci number greater than 1 is the sum of the two Fibonacci numbers before it.
# The program defines a function fibonacci that takes an integer input n and returns the nth Fibonacci number.
# If n is less than or equal to 1, the function returns n.
# Otherwise, it returns the sum of the (n-1)th and (n-2)th Fibonacci numbers.

#sudo code
#1. Define a function fibonacci that takes an integer input n.
#2. If n is less than or equal to 1, return n.
#3. Otherwise, return the sum of the (n-1)th and (n-2)th Fibonacci numbers.
#4. Take an integer input n from the user.
#5. Call the fibonacci function with n as the argument and print the result.
#6. End.