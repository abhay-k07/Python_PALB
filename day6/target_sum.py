#return indices of the two numbers such that they add up to target
arr = [2, 7, 11, 15]
target = 17
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print([i, j])
            break