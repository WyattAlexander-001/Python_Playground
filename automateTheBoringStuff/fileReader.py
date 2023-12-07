# Overwrite the file
basicFile = open("automateTheBoringStuff/sample.txt", "w") # relative path
basicFile.write("This is a test\n")
basicFile.write("This is another test\n")
basicFile.write("This is a third test\n")
basicFile.close() # close the file

# Read the file
basicFile = open("automateTheBoringStuff/sample.txt", "r") # relative path
print("====================================")
print(basicFile.read())
print("====================================")

# Append to the file
basicFile = open("automateTheBoringStuff/sample.txt", "a") # relative path
basicFile.write("Append1\n")
basicFile.write("Append2\n")
basicFile.write("Append3\n")
basicFile.close() # close the file

# Read the file
basicFile = open("automateTheBoringStuff/sample.txt", "r") # relative path
print(basicFile.read())

