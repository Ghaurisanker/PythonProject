def largestElement(list):
    max = list[0]
    n = len(list)
    for i in range(1,n):
        if list[i] > max:
            max = list[i]
    return max

list = [12,3,4,5,56,6,7]
ans = largestElement(list)
print("The result: ",ans)

# todo: explore other ways to find the largest Element in a list