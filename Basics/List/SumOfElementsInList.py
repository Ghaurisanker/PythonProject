def sumofList(list):
    sum = 0
    for i in list:
        sum = sum + list[i]
    return sum

list = [1,1,1,1,1]
ans = sumofList(list)
print("The sum elements in list: ", ans)

# todo: other ways to find sum of elements in a list