#Calculating factorial of a number using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

#Calculating factorial of a number using iteration
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#representing calculated factorial as an array of its digits
def factorial_to_array(n):
    fact = factorial_iterative(n)
    fact_str = str(fact)
    factorial = []
    for i in range(len(fact_str)):
        factorial.append(int(fact_str[i]))
    return factorial

n = 5
print(f"The factorial of {n} is {factorial_recursive(n)}")
print(f"The factorial of {n} using iteration is {factorial_iterative(n)}")
print(f"The factorial of {n} as an array of digits is {factorial_to_array(n)}")