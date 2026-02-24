### Python Quiz

---

- **Q01-01**

**Print the sum of the values from 1 to 5. The code that prints the sum of the values from 1 to 3 using the `print()` function is `print(1+2+3)`. With reference to this code, print the sum of the values from 1 to 5.**

  ```python
  print("The sum of 1 to 5 is:", 1+2+3+4+5)
  ```

- **Q02-01**

**Find the sum of odd numbers between 1 and 100. The figure below is a flowchart of a program that finds the sum of odd numbers among integers between 1 and 100 and prints the sum. Fill in the blanks.**

```Python
N = -1
S = 0

while True:
    N = N + 2
    S = S + N

    if N >= 100:
        break

print(S)
```
- **Q02-02**

**We will write a program that receives a positive integer from the user and tells whether it is an odd or even number.Complete the appropriate pseudo code for the underlined part.**

```Python
print('Enter an integer:')
n = input()

if int(n) % 2 == 0:
    print('n is even')
else:
    print('n is odd')
```
- **Q03-01**

**Write a code to print the following decorative output. In the first line, use only one '*' character with the operator * and number. In the second line, use only one '#' character and one space with the operator * and number.Coding guideline: In the case of the first line, print in the same way as '*' * number n. The second line also uses the * operator.**
```Python
print('*' * 10)
print(('# ' * 5).rstrip())
```

- **Q04-01**

**Write and save the following name and address in the name and address variables, respectively. Write a code that prints them to the screen.name = "David Doe"**
```python
name = "David Doe"
address = "1600 Wilshire Blvd #205, Los Angeles CA 90017"
print(name)
print(address)
```
- **Q05-01**

**Expect the output of the following code and write it down**
```python
x =1
y = 0
print(x and y)
print(x or y)
print(not x)
print(not y)
```
**output:**
```0
1
False
True
```
- **Q06-01**

**Write a program that takes two random integers as input and lists them from smallest to largest. (Condition: Two integers are not the same number.) Coding guideline: Receive the user's input with the input function and convert it to an integer using the int function.Next, use an if statement to compare and print the two values**
```python
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

if num1 < num2:
    print(num1, num2)
else:
    print(num2, num1)
```
- **Q07-01**

**Write a program that performs the following using a compound conditional expression of an if statement. Coding guideline: Write a code that performs differently depending on whether the answer to the first question is 0 or 1, as shown below.**
```python
adult = int(input("Are you an adult? (1 if you are an adult, 0 if you are minor):"))
married = int(input("Are you married? (1 if you are married, 0 if you are single):"))

if adult == 1 and married == 1:
    print("You are an adult who is married.")
```
- **Q08-01**

**Among the positive natural numbers other than 1, a number that is not prime is called a composite number. Print the prime and composite numbers from 2 to 12 as follows. Coding guideline: Use the for statement to solve this problem. When using a nested for statement, an expression for determining a prime number must be entered in the inner for statement.**
```python
for i in range(2, 13):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{i}: Prime number")
    else:
        print(f"{i}: Composite number")
```
- **Q09-01**

**An Armstrong number is a three-digit integer that is equal to the sum of the cubes of each digit. Find all Armstrong numbers among three-digit integers and print them as follows. Coding guideline: All numbers from 100 to 999 should be searched using the for statement.**
```python
print("Three-digit Armstrong numbers:", end=" ")
for i in range(100, 1000):
    hundreds = i // 100
    tens = (i % 100) // 10
    units = i % 10

    if (hundreds**3 + tens**3 + units**3) == i:
        print(i, end=" ")
```
- **Q10-01**

**If there are two lists l1 and l2 with the following strings, use the combination of l1 and l2 to print as follows. Coding guideline: Use nested loops to print it out.**
```python
l1 = ['I like', 'I love']
l2 = ['pancake.', 'kiwi juice.', 'espresso.']

for phrase in l1:
    for food in l2:
        print(f"{phrase} {food}")
```
- **Q11-01**

**The person dictionary is defined as follows. Add a new item to this person dictionary with the key 'Father' and the value 'John Doe'. And then print the person dictionary. Coding guideline: After defining the person dictionary, write a code to add new items.**
```python
person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82, 'Job': 'Data scientist' }
person['Father'] = 'John Doe'
print(person)
```
- **Q12-01**

**With tuple data, the values of two variables can be swapped without using a temporary variable. Using this swapping method, write a program that moves the largest value in the given list to the last. Coding guideline: Use a for loop. When swapping values in a list, additional variables such as temp should not be used.**
```python
lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]
for i in range(len(lst) - 1):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)
```
- **Q13-01**

**The two-dimensional array a contains the values [[1, 2], [3, 4], [5, 6]]. Change this two-dimensional array to a onedimensional array like [1, 2, 3, 4, 5, 6], and print it out. Coding guideline: Use a for loop. Define a new array and put the elements of a into this array.**
```python
a = [[1, 2], [3, 4], [5, 6]]
flat_array = []

for sub_array in a:
    for element in sub_array:
        flat_array.append(element)

print(flat_array)
```
- **Q14-01**

**There is a dictionary variable maria as follows. In this dictionary variable, courses such as ‘korean' and ‘english' and their scores are stored as key:value. Print the average score of 89.25 for maria's subject scores. Coding guideline: Use a dictionary method such as values() and len() function.**
```python
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)
```
- **Q15-01**

**Declare a nested dictionary school as follows. Next, use the deepcopy() function of the copy module to write a program that 'copy' to another variable, school2. (Check that school and school2 are different variables through the is operator.) Coding guideline: Print so that the result of school is school2 is false.**
```python
import copy
school = {'kim': {'age': 16, 'hei': 170, 'grade': 3}, 
          'lee': {'age': 15, 'hei': 168, 'grade': 2}, 
          'choi': {'age': 14, 'hei': 173, 'grade': 1}}

school2 = copy.deepcopy(school)
print(school is school2)
```
- **Q16-01**

**There is a scores tuple as follows. This tuple contains information about four students, including each student's name and English, math, and science grades. For example, ‘Hyun’ has an English score of 88, a math score of 95, and a science score of 90. Extract only math scores by unpacking the scores tuple. Write a code that calculates the average of these extracted math scores. Coding guideline: Use the zip function to solve the problem.**
```python
scores = (('Hyun', 88, 95, 90), ('Kang', 85, 90, 95), ('Park', 70, 90, 80), ('Hong', 90, 90, 95))
names, english, math, science = zip(*scores)

math_average = sum(math) / len(math)
print(math_average)
```
