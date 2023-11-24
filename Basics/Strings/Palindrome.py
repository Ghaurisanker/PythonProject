def palindrome(s):
    reverse = s[::-1]
    if s == reverse:
        print("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")

palindrome("Hello")
palindrome("malayalam")