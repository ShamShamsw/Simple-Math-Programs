def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter a number: "))
    for i in range(2, n):
        if prime(i):
            print(i)

if __name__ == "__main__":
    main()

#Sudo code
#1. Define a function is_prime that takes a number n as a parameter
#2. If n is less than 2, return False
#3. Loop through the numbers from 2 to n
#4. If n is divisible by any number other than 1 and itself, return False
#5. Otherwise, return True
#6. Define a main function
#7. Prompt the user to enter a number
#8. Loop through the numbers from 2 to n
#9. If the number is prime, print it
#10. Call the main function if the script is run as the main program
#11. End

# Next Steps
# Generate a random array of numbers and check if they are prime