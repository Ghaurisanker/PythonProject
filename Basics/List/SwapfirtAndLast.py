def swap(list):
    n = len(list)

    temp = list[0]
    list[0] = list[n-1]
    list[n-1] = temp

    return list

list = [1,2,3,44,'Hi']
ans = swap(list)
print("The swapped values of the list", ans)

# 1. Create a empty list
# 2. Find the first and last element of the list
# 3. store the first element in temp, last element to first then temp to last element
