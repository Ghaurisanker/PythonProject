def secondLargestElementInList(list):
    element = sorted(list)  #list.sort() method sorts the list in-place and returns None, so you can't use it to assign to element
    secondLargestElement = element[len(element) - 2]
    return secondLargestElement

list = [1,3,4,5,2,3,13,18,1,2,4,5,67]
ans =  secondLargestElementInList(list)
print("The result", ans)

#todo: Explore other ways tooo