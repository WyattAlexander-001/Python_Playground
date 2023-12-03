def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("Sequential Search: ")
arr = [4, 2, 88, 1, 45, 7]
print(sequential_search(arr, 3)) # -1
print(sequential_search(arr, 88)) # 2
print(sequential_search(arr, 4)) # 0


'''

This one is easy to understand, but it is not efficient.
The time complexity is O(n) "linear".
We basically iterate through the array and check if the target is in the array.
If it is, we return the index of the target.
If it is not, we return -1.

'''

