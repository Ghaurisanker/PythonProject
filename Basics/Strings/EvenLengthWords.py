def findEvenLenghtWords():
    string = input("Enter a String:")
    new_string = []
    s = string.split()
    for i in s:
        if len(i)%2 == 0:
             new_string.append(i)
    print("The Result", new_string)

findEvenLenghtWords()