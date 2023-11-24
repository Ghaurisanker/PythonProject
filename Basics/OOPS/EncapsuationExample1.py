# Write Python code here
class sampleclass:
    count = 0	 # class attribute
    print("Count value of class attribute",count)

    def increase(self):
        sampleclass.count += 1
        print("Count value of instance attribute",sampleclass.count)


# Calling increase() on an object
s1 = sampleclass()
s1.increase()
print(s1.count)
print()

# Calling increase on one more
# object
s2 = sampleclass()
s2.increase()
print(s2.count)

print(sampleclass.count)