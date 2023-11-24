def smallestElement(list):
    min = list[0]
    n = len(list)
    for i in range(1,n):
        if min < list[i]:
            min = list[i]
    return min

list = [1,2,3,43,5,5,3]
ans = smallestElement(list)
print("The result",ans)

# todo: explore other ways to find minimum value in a list