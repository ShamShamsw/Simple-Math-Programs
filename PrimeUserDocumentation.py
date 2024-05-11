# The goal of the function below is to check if the number is prime or not.
# To start the number should be greater than 1 because 1 is not a prime number and 0 is not a prime number.
# The function will check if the number is divisible by any number between 2 and the number itself.
# The for loop will iterate through the numbers between 2 and the number itself.
# It does this by checking if the number is divisible by any number between 2 and the number itself.
# If the number is divisible by any number between 2 and the number itself, the function will return False.
# If the number is not divisible by any number between 2 and the number itself, the function will return True.
# The function will then check if the number is prime or not.
# The function will print the prime numbers between 2 and the number itself.
# The function will then call the main function.
# The main function will take the input from the user.
# The main function will then call the prime function.
# The main function will then print the prime numbers between 2 and the number itself.

#def prime(n):
#    if n < 2:
#        return False
#    for i in range(2, n):
#        if n % i == 0:
#            return False
#    return True

#def main():
#    n = int(input("Enter a number: "))
#    for i in range(2, n):
#        if prime(i):
#            print(i)

#if __name__ == "__main__":
#    main()