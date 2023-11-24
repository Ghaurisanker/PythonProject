def multiply(list):
    product = 1
    for i in list:
        product = product * i  #todo: why we cannot give list[i]
    return product

list = [1,2,3]
ans = multiply(list)
print("The result:",ans)

# todo: explore other ways to multiply the items in the list