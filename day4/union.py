#union of two arrays
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]
c = [0] * (len(a) + len(b))
i =0
while i < len(a):
    c[i] = a[i]
    i += 1
j = 0
while j < len(b):
    c[i] = b[j]
    i += 1
    j += 1
print("Union of two arrays is:", c)