myList = ['cat', 'bat', 'rat', 'elephant', 'dog']

print("Indexing a list:")
print(myList[0])  # cat
print(myList[1])  # bat
print(myList[-1])  # dog
print(myList[-2])  # elephant

print("=====================================")
print("Iterating through a list:")
for i in range(len(myList)):
    print(myList[i])

print('elephant' in myList) # True

print("=====================================")
print("Slicing a list:") # Makes a new list
newList = myList[0:2]
print(newList)  # ['cat', 'bat'] goes up to but not including index 2
print(myList[0])  # cat

del newList[0]
print(newList)