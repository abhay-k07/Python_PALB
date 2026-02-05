#Create a leader array from a given array
def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[n-1]
    leaders.append(max_from_right)

    for i in range(n-2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)

    leaders.reverse()
    return leaders

arr = [16, 17, 4, 3, 5, 2]
print("Leaders in the array:", find_leaders(arr))