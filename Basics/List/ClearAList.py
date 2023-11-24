def clearList(list):
    list.clear()
    return f"There is no items in the list {list}"

list = [1,2,3,4]
ans = clearList(list)
print("The result:", ans)

# other ways: todo
# Using clear()
# Reinitializing the list
# Using “*= 0”
# Using del
# Using pop() method
# Using slicing
