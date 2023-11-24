def find(list, element):
    for i in list:
        if i == element:
            return True
    return False

def find1(list, element):
    for i, value in enumerate(list):
        if value == element:
            return f"The element {element} is present at index {i}."
    return f"The element {element} is not present in the list."


list = ["hello",1,3,4,5,6]
element = 7
ans = find1(list, element)
print("The result:", ans)


# enumerate() function to iterate over both the values and their indices in the list. If the element is found, it returns a message with the element and its index.
# If the element is not found, it returns a message indicating that the element is not present in the list.

# todo: explore other ways
# Using “in” Statement
# Using a loop
# Using any() function
# Using count() function
# Using sort with bisect_left and set()
# Using find() method
# Using Counter() function
# Using try-except block