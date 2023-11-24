# arr = [1,2,2,3]

def sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i

    return sum

arr = [11,22,33]
ans = sum(arr)
print("The Largest element of array is: ", ans)

# 1. initialise the sum
# 2. iterate through array
# 3. the add the items and update the sum value