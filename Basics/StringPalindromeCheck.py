'''
Create a Python function to check if a given string is a palindrome
'''

def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase to make it case-insensitive
    s = ''.join(filter(str.isalnum, s))  # Remove non-alphanumeric characters
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))    # True
print(is_palindrome("hello"))      # False
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
