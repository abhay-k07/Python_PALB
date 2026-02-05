#return index of target value or where it would be if not in array
arr = [1, 3, 5, 6]
target = 5
while arr:
    mid = len(arr) // 2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        arr = arr[mid + 1:]
    else:
        arr = arr[:mid]
else:
    print(len(arr))