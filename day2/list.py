lst = []

f1 = int(input("Enter Marks:"))
lst.append(f1)
f2 = int(input("Enter Marks:"))
lst.append(f2)
f3 = int(input("Enter Marks:"))
lst.append(f3)
f4 = int(input("Enter Marks:"))
lst.append(f4)
f5 = int(input("Enter Marks:"))
lst.append(f5)
f6 = int(input("Enter Marks:"))
lst.append(f6)
#remove
lst.remove(f4)
#insert
lst.insert(2, 95)
#sort
lst.sort()
print(lst)