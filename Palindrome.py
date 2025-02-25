def is_palindrome(s):
    """Check if the given string is a palindrome."""
    # Remove spaces and convert to lowercase to ensure the check is case-insensitive
    cleaned_str = ''.join(s.split()).lower()
    
    # Compare the string with its reverse
    return cleaned_str == cleaned_str[::-1]

def main():
    # Get user input
    user_input = input("Enter a string: ")

    # Check if it's a palindrome
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()