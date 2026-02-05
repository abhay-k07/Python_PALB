#find minimum and maximum element of an array.
arr = [23,45,43,56,1,9]

max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print (max, min)
