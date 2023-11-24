def swapTwoElements(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = [1,2,3,4,5,6,7]
pos1 = 1
pos2 = len(list) - 2

ans = swapTwoElements(list, pos1, pos2)
print("The final list after swapping two elements", ans)


# 1. Take the list ans positions to swap
# 2. Then reassign the positions
# 3. retrun the list
