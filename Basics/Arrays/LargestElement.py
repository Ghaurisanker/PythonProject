def largest(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
            
    return max

arr = [1,2,3,4,433,22]
n = len(arr)
ans = largest(arr, n)
print("The Largest element of array is: ", ans)


# 1. first we declare the first element of array as max value
# 2. Then we traverse through the arry
# 3. Then we comapare the first element with the array elements
# 4. If it is greater then we update the max value
# 5. finally we retrun the max value