def reverseList(list):
    new_list = list[::-1]
    return new_list

list = [1,2,3,4,5]
ans = reverseList(list)
print("The result:", ans)

# todo: other ways to reverse a list
# Using the slicing technique
# Reversing list by swapping present and last numbers at a time
# Using the reversed() and reverse() built-in function
# Using a two-pointer approach
# Using the insert() function
# Using list comprehension
# Reversing a list using Numpy