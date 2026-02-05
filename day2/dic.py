dict = {}

name = input(("Enter the name:"))
lang = input(("Enter the language:"))
dict.update({name : lang})
name = input(("Enter the name:"))
lang = input(("Enter the language:"))
dict.update({name : lang})
name = input(("Enter the name:"))
lang = input(("Enter the language:"))
dict.update({name : lang})
name = input(("Enter the name:"))
lang = input(("Enter the language:"))
dict.update({name : lang})
#remove
dict.pop(name)
#add
dict.update({"Amit" : "Java"})
print(dict)