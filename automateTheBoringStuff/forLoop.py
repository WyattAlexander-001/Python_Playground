print("This is just like GDScript")
for i in range(5):
    print("Round # " + str(i))

print("=====================================")

for i in range(5):
    print("Round # " + str(i+1))
    

total = 0

for num in range(101): # 0 to 100 Gaussian Summation
    print(str(total) + " + " + str(num))
    total += num
    print("Total: " + str(total))
print(total)