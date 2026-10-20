# Week 3 – Functions and Modules – Programming Problems

## Task 1: Quiz
Suppose you want to develop a program to help a first grader practice addition, subtraction, multiplication, division, exponent or remainder. The user should have the option of choosing which mathematical operation they wish to practice. The program randomly generates two single-digit integers, number1 and number2, and of course the user will provide the answer to the question.

The program should include:
- A menu allowing the student to choose the operation they want to practice (ideally included in function names or main).
- Functions for each of the mathematical operations.
- A score calculating correct answers.
- Error messages for situations such as division by zero.
- Functionality to keep practicing until the user decides otherwise.

import random

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b


score = 0
play_again = "y"

while play_again == "y":
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Remainder")

    choice = input("Enter 1 to 6: ")

    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    if choice == "1":
        answer = add(number1, number2)
        symbol = "+"
    elif choice == "2":
        answer = subtract(number1, number2)
        symbol = "-"
    elif choice == "3":
        answer = multiply(number1, number2)
        symbol = "*"
    elif choice == "4":
        symbol = "/"
        if number2 == 0:
            print("You can't divide by zero. Try another question.")
            answer = None
        else:
            answer = divide(number1, number2)
    elif choice == "5":
        answer = power(number1, number2)
        symbol = "**"
    elif choice == "6":
        symbol = "%"
        if number2 == 0:
            print("You can't use zero for a remainder question. Try another.")
            answer = None
        else:
            answer = remainder(number1, number2)
    else:
        print("Please choose a number from 1 to 6.")
        answer = None

    if answer is not None:
        print(f"What is {number1} {symbol} {number2}?")
        user_answer = float(input("Your answer: "))

        if round(user_answer, 2) == round(answer, 2):
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. The answer is {answer}.")

    play_again = input("Practise again? Enter y or n: ").lower()

print(f"You got {score} questions correct.")

## Task 2: Scientific Calculator (Unit Conversion Chart)
Create a Scientific Calculator imitating the Unit Conversion Chart (Fig. 1).

Allow the user to choose between length, temperature, mass, volume, pressure, and energy. Create separate functions for each calculation within the types of unit. Allow the user to choose between units. For example, if the user chooses length, then the programme should allow the user to choose between conversions: m/ft, in/cm, or mi/km. The user should then enter the value to calculate. Finally, the system should do the conversion and print out the result.

![Unit Conversion Chart](Unit-Conversion-Chart.png)

def length():
    print("Choose a length conversion:")
    print("1. Metres to feet")
    print("2. Inches to centimetres")
    print("3. Miles to kilometres")

    choice = input("Enter 1, 2 or 3: ")
    value = float(input("Enter the value: "))

    if choice == "1":
        result = value * 3.3
        print(f"{value} metres = {result} feet")
    elif choice == "2":
        result = value * 2.43
        print(f"{value} inches = {result} centimetres")
    elif choice == "3":
        result = value * 1.61
        print(f"{value} miles = {result} kilometres")
    else:
        print("Invalid choice")


print("Choose a category:")
print("1. Length")

category = input("Enter 1: ")

if category == "1":
    length()
else:
    print("We haven't added that category yet.")

*Fig 1. Unit Conversion Chart*

## Task 3: Palindrome Checker
Write a function to check if a given string is a palindrome (reads the same backward as forward).

Some palindrome words are: civic, radar, level, rotor, kayak, madam, refer, rotator, deified, racecar and reviver.

The function should take one string, and return `True` if it is a palindrome, otherwise `False`.
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(is_palindrome("radar"))   # True
print(is_palindrome("python"))  # False
## Task 4: Text Compression
Write a Python function called `compress_string` that takes a string as input and returns a compressed version of the string. The compression should replace repeated characters with the character followed by the count of repetitions. If the compressed string is longer than the original string, return the original string.

```python
compressed = compress_string("aaabbbbcccddeee")
# The expected output is "a3b4c3d2e3" because 'a' is repeated 3 times, 'b' 4 times, 'c' 3 times, etc.
compressed = compress_string("Hello")
# The expected output is "Hello", because the compressed string in this case H1e1l2o1 is longer than the original string "Hello"
```
def compress_string(text):
    if text == "":
        return text

    compressed = ""
    count = 1

    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            count += 1
        else:
            compressed += text[index - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)

    if len(compressed) > len(text):
        return text
    else:
        return compressed


print(compress_string("aaabbbbcccddeee"))
print(compress_string("Hello"))


## Task 5: Lambda Rewrite
Rewrite the quiz or the scientific converter including mainly lambda functions.

import random

operations = {
    "1": ("+", lambda a, b: a + b),
    "2": ("-", lambda a, b: a - b),
    "3": ("*", lambda a, b: a * b),
    "4": ("/", lambda a, b: a / b),
    "5": ("**", lambda a, b: a ** b),
    "6": ("%", lambda a, b: a % b)
}

score = 0
play_again = "y"

while play_again == "y":
    print("1. Addition  2. Subtraction  3. Multiplication")
    print("4. Division  5. Exponent  6. Remainder")

    choice = input("Choose an operation: ")

    if choice not in operations:
        print("Invalid choice")
    else:
        number1 = random.randint(0, 9)
        number2 = random.randint(0, 9)
        symbol, operation = operations[choice]

        if choice in ("4", "6") and number2 == 0:
            print("You can't divide by zero.")
        else:
            answer = float(input(f"What is {number1} {symbol} {number2}? "))
            correct_answer = operation(number1, number2)

            if round(answer, 2) == round(correct_answer, 2):
                print("Correct!")
                score += 1
            else:
                print(f"Not quite. The answer is {correct_answer}.")

    play_again = input("Practise again? (y/n): ").lower()

print(f"You got {score} correct.")

## Task 6: Cyber: Timestamped Auth Event
Ask for a username and action (e.g., `LOGIN` or `LOGOUT`) and print a timestamped event line.

**Example Output:**
```
[2025-09-17 14:20:15] LOGIN user=alice
```
*Optional hint:* `from datetime import datetime; datetime.now().strftime(...)`

from datetime import datetime

username = input("Enter username: ")
action = input("Enter action, such as LOGIN or LOGOUT: ")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"[{timestamp}] {action} user={username}")

## Task 7: Pure Python EDA: Mini Statistics Report
Ask for five numeric values (space-separated). Print the values, total, mean, median, and sample standard deviation.

**Example Output:**
```
Values: 80, 90, 70, 85, 75
Total = 400.00
Mean = 80.00
Median = 80.00
Std Dev = 7.91
```
*Optional hint:* `import statistics as stats`

import statistics as stats

values = input("Enter five numbers separated by spaces: ").split()
values = [float(value) for value in values]

print("Values:", ", ".join(str(value) for value in values))
print(f"Total = {sum(values):.2f}")
print(f"Mean = {stats.mean(values):.2f}")
print(f"Median = {stats.median(values):.2f}")
print(f"Std Dev = {stats.stdev(values):.2f}")

## Task 8: IT: Path Decomposition Report
Ask for a file or directory path and print its absolute path, parent, name, stem, and suffix.

**Example Output:**
```
Absolute path: /home/user/project/service.log
Parent: /home/user/project
Name: service.log
Stem: service
Suffix: .log
```
*Optional hint:* `from pathlib import Path`

from pathlib import Path

path = Path(input("Enter a file or directory path: "))

print("Absolute path:", path.absolute())
print("Parent:", path.parent)
print("Name:", path.name)
print("Stem:", path.stem)
print("Suffix:", path.suffix)

## Task 9: System Info Banner
Ask for a hostname and print OS and Python version as a simple banner (one value per line).

**Example Output:**
```
Host: server01
OS: Linux
Python: 3.11.5
```
*Optional hint:* `import platform; platform.system(); platform.python_version()`

import platform

hostname = input("Enter hostname: ")

print("Host:", hostname)
print("OS:", platform.system())
print("Python:", platform.python_version())

## Task 10: Pentagon Area
Ask for the side length `s` and compute the area: `area = 5*s**2 / (4*tan(pi/5))`. Print to 2 d.p.

**Example Output:**
```
Area = 172.05
```
*Optional hint:* `from math import tan, pi`

from math import tan, pi

side = float(input("Enter the pentagon side length: "))
area = 5 * side ** 2 / (4 * tan(pi / 5))

print(f"Area = {area:.2f}")

## Task 11: Square Root Table
Use the `math.sqrt` function. Write a program that prints the following table using the `sqrt` function in the `math` module.

```
Number      Square root
0   	 	0.00
2    		1.41
4    		2.00
6    		2.45
8    		2.83
10    		3.16
12    		3.46
14    		3.74
16    		4.00
18    		4.24
```

import math

print(f"{'Number':<12}Square root")

for number in range(0, 20, 2):
    print(f"{number:<12}{math.sqrt(number):.2f}")