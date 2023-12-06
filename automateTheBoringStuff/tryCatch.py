def div42By(num):
    try:
        return 42 / num # normal execution
    except ZeroDivisionError as e:
        print("Error: You tried to divide by zero")
        print("Exception details", e)


print(div42By(2))
print(div42By(0))


   
print("How many cats do you have?")
numCats = input()
try:
    numCats = int(numCats)
    if numCats < 0:
        raise ValueError("The number of cats cannot be negative")
    elif numCats >= 4:
        print("That's a lot of cats")
    else:
        print("That's not that many cats")
except ValueError as e:
    print("Invalid input. Please enter a number.")