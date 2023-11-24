def postive(start, end):
    list = []
    for i in range(start, end+1):
        if i > 0:
            list.append(i)
    return list

def negative(start, end):
    list = []
    for i in range(start, end+1):
        if i < 0:
            list.append(i)
    return list


ans = postive(-5,8)
print("Result", ans)

ans = negative(-5,8)
print("Result", ans)