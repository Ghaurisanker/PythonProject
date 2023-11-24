def countEvenNumbers(list):
    count = 0
    for i in list:
        if i%2 == 0:
            count = count + 1
    return count

def printEvenNumbers(list):
    new_list = []
    for i in list:
        if i%2 == 0:
            new_list.append(i)
    return new_list

def printEvenNumbersInRange(start, end):
    new_list = []
    for i in range(start, end+1):
        if i%2 == 0:
            new_list.append(i)
    return new_list


list = [1,2,32,3,6,8,11,10]
ans = countEvenNumbers(list)
print("count of Even numbers in a list:", ans)

ans = printEvenNumbers(list)
print("Even numbers in a list:", ans)

ans = printEvenNumbersInRange(1,5)
print("Even numbers from list for a given range:", ans)  #todo: for a given list in a given range

# todo: explore other ways