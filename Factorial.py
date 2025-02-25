import math

def calculate_factorial(n):
    """Calculates the factorial of n"""
    return math.factorial(n)

def is_factorial(num):
    """Checks if a number is a factorial of some integer."""
    i = 1
    fact = 1
    while fact < num:
        i += 1
        fact *= i
    return fact == num

def main():
    # Taking input from the user
    try:
        number = int(input("Enter a number: "))
        
        # Checking if the input number is a factorial
        if is_factorial(number):
            print(f"{number} is a factorial number.")
        else:
            print(f"{number} is not a factorial number.")
        
        # Calculating the factorial of the number if it is a valid input
        if number >= 0:
            print(f"The factorial of {number} is: {calculate_factorial(number)}")
        else:
            print("Factorial is not defined for negative numbers.")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()