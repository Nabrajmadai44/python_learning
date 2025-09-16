'''
🟢 Beginner Level
Great for understanding syntax, loops, conditionals, and basic data structures.

1. Even or Odd
Write a program that takes an integer as input and prints whether it is even or odd.
num = int(input('Enter an integer: '))
if num % 2:
    print(f'{num} is odd number')
else:
    print(f'{num} is even number')

2. Sum of a List
Create a list of numbers and write a function that returns the sum of all the elements.
num_list = [1,2,3,4,5,6,7,8,9]
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_of_list(num_list))

3. Factorial Calculation
Write a function to compute the factorial of a given number.
# using loop
def fac(n):
    if n < 0:
        print("Factorial is not defined for negative numbers    ")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

number = int(input("Enter a number to calculate it s factorial: "))
print(fac(number))



4. Palindrome Checker
Check whether a given string is a palindrome (reads the same backward).
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

word = input("Enter a word: ")

if is_palindrome(word):
    print("It's a palindrome word")
else:
    print("It's not a palindrome word")



5. Fibonacci Series
Print the first n numbers in the Fibonacci sequence.

def fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b , a + b

num = int(input("Enter a number: "))
fibo(num)

'''