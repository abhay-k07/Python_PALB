#find the kth smallest element in the array.
arr = [7, 10, 4, 3, 20, 15]
min = arr[0] 
k = 3
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
print(f"{k}th smallest element is:", arr[k - 1]) 