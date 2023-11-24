def countOddNumbers(list):
    count = 0
    for i in list:
        if i%2 != 0:
            count = count + 1
    return count

def printOddNumbers(list):
    new_list = []
    for i in list:
        if i%2 != 0:
            new_list.append(i)
    return new_list

def printOddNumbersInRange(start, end):
    new_list = []
    for i in range(start, end+1):
        if i%2 != 0:
            new_list.append(i)
    return new_list

list = [1,2,3,4,5,6]
ans = countOddNumbers(list)
print("Count of odd numbers in a list:", ans)


ans = printOddNumbers(list)
print("Count of odd numbers in a list:", ans)

ans = printOddNumbersInRange(0,4)
print("Count of odd numbers in a list:", ans)   #todo: print odd numbers in a given range for given list 

# todo: explore other ways