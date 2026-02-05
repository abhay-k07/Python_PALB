#rotating the array clockwise by one position
arr=[1, 2, 3, 4, 5]
a = arr.pop()
arr.insert(0, a)
print(arr)