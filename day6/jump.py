#find the minimum number of jumps to reach the end of the array
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
jumps = 0
current_end = 0
far = 0
for i in range(len(arr) - 1):
    far = max(far, i + arr[i])
    if i == current_end:
        jumps += 1
        current_end = far
print(jumps)