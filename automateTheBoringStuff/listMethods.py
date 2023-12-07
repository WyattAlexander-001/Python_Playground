spam = ["hello", "hello" ,"hi", "howdy", "heyas"]
print(spam.index("hello"))
# print(spam.index("byebye")) # ValueError: 'byebye' is not in list

spam.append("Jim")
print(spam[-1])
spam.pop()
print(spam[-1])

spam.remove("hello") # removes first instance of "hello"
print(spam)

spam.sort()
print(spam)