#largest element of the array
arr = [7, 10, 4, 3, 20, 15]
max = arr[0] 
for i in arr:  
    if i > max: 
        max = i
print("Largest element is:", max)