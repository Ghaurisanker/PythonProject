def usingLenFunc(list):
    length = len(list)
    return length

def nativeApproach(list):
    count = 0
    for i in list:
        count = count + 1
    return count


list = [1,2,3,4,5,6,7]
ans = nativeApproach(list)
print("The length of the list is", ans)

# 1. First by using the len()
# 2. For native approach, we find the length of the list by using a counter, we increment the counter by 1 when we iterate through the list

# todo: explore other ways to find the length of the list