# Week 2 – Decisions and Loops – Programming Problems

## Task 1: Password Strength Checker
**Scenario:** You are a junior security analyst at a company. Employees often choose weak passwords, so you need to create a simple program to check password strength. Since you only know the basics of programming, your program will use simple rules.

**Requirements:**
1. Ask the user to enter a password.
2. If the password has fewer than 8 characters, print "Weak".
3. If the password has 8 or more characters, print "Moderate".
4. If the password has 12 or more characters, print "Strong".

password = input("Enter a password: ")

if len(password) >= 12:
    print("Strong")
elif len(password) >= 8:
    print("Moderate")
else:
    print("Weak")   

## Task 2: Multiplication Quiz
Suppose you want to develop a program to help a first-grader practice multiplication. The program randomly generates two single-digit integers, number1 and number2, and displays to the student a question such as: What is 1 * 7. After the student types the answer, the program displays a message to indicate whether it is true or false.



To generate a random number, you can use the `randint(a, b)` function in the `random` module. This function returns a random integer i between a and b, inclusively. To obtain a random integer between 0 and 9, use `randint(0, 9)`.

The program may be set up to work as follows:
- Step 1: Randomly generate two single-digit integers for number1 (e.g., 4) and number2 (e.g., 5)
- Step 2: Prompt the student to answer, "What is 4 * 5?" (user input)
- Step 3: Check whether the student's answer is correct.

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
answer = int(input(f"What is {number1} * {number2}? "))

if answer == number1 * number2:
    print("True")
else:
    print("False")

## Task 3: Even or Odd
Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

## Task 4: Body Mass Index (BMI)
BMI is a measure of health and weight. It can be calculated by taking your weight in kilograms and dividing it by the square of your height in meters. The interpretation of BMI for people 20 years or older is as follows:

| BMI | Interpretation |
|-----|----------------|
| BMI < 18.5 | Underweight |
| 18.5 ≤ BMI < 25.0 | Normal |
| 25.0 ≤ BMI < 30.0 | Overweight |
| 30.0 ≤ BMI | Obese |

Write a program that prompts the user to enter weight in pounds and height in inches and display the BMI. Note that one pound is 0.45359237 kilograms, and one inch is 0.0254 meters.

weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))

weight_kg = weight_pounds * 0.45359237
height_m = height_inches * 0.0254
bmi = weight_kg / (height_m ** 2)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

## Task 5: Negative Numbers
Display numbers from `-10` to `-1` using a for loop.

```
Expected output:
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
```

for number in range(-10, 0):
    print(number)

## Task 6: Number Pattern
Write a program to print the following number pattern using a loop.

```
Expected output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()

## Task 7: Sum of Numbers from 1 to n
Write a program to accept a number `n` from a user and calculate the sum of all numbers from 1 to a given number n.

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10).

```
Expected output
Enter the value n: 10
The sum of all numbers until 10 is 55


n = int(input("Enter the value n: "))
total = 0

for number in range(1, n + 1):
    total += number

print(f"The sum of all numbers until {n} is {total}")
```

## Task 8: Multiplication Table of a Number
Write a program to print the multiplication table of a given number.

For example, `num = 2`:

```
Expected output:

0 x 2 = 0
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
4 x 2 = 8
5 x 2 = 10
6 x 2 = 12
7 x 2 = 14
8 x 2 = 16
9 x 2 = 18
```

num = int(input("Enter a number: "))

for number in range(10):
    print(f"{number} x {num} = {number * num}")

## Task 9: Multiplication Table Grid
Display the following multiplication table. Consider the spacing between digits.

```
Expected output:

0   0   0   0   0   0   0   0   0   0 
0   1   2   3   4   5   6   7   8   9 
0   2   4   6   8  10  12  14  16  18 
0   3   6   9  12  15  18  21  24  27 
0   4   8  12  16  20  24  28  32  36 
0   5  10  15  20  25  30  35  40  45 
0   6  12  18  24  30  36  42  48  54 
0   7  14  21  28  35  42  49  56  63 
0   8  16  24  32  40  48  56  64  72 
0   9  18  27  36  45  54  63  72  81 
```

for row in range(10):
    for column in range(10):
        print(f"{row * column:3}", end=" ")
    print()

## Task 10: Dog Years
It is commonly said that one human year is equivalent to 7 dog years. However, this simple conversion fails to recognise that dogs reach adulthood in approximately two years. As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.

Write a program that implements the conversion from human years to dog years described in the previous paragraph. Ensure that your program works correctly for conversions of less than two or more human years. Your program should display an appropriate error message if the user enters a negative number.

human_years = float(input("Enter human years: "))

if human_years < 0:
    print("Please enter a number that is not negative.")
elif human_years <= 2:
    dog_years = human_years * 10.5
    print(f"Dog years: {dog_years}")
else:
    dog_years = 21 + (human_years - 2) * 4
    print(f"Dog years: {dog_years}")

## Task 11: Vowel or Consonant
In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.

letter = input("Enter one letter: ").lower()

if letter in "aeiou":
    print("Vowel")
elif letter == "y":
    print("Sometimes y is a vowel, and sometimes it is a consonant.")
else:
    print("Consonant")

## Task 12: Reverse Number Pattern
Write a program that uses a for loop to print the following reverse number pattern.

```
Expected output:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
```

for row in range(5, 0, -1):
    for number in range(row, 0, -1):
        print(number, end=" ")
    print()

## Task 13: Find the Highest Score
Write a program that prompts the user to enter the number of students and each student's name and score and displays the student name and highest score.

student_count = int(input("How many students? "))
highest_score = None
highest_name = ""

for _ in range(student_count):
    name = input("Student name: ")
    score = float(input("Student score: "))

    if highest_score is None or score > highest_score:
        highest_score = score
        highest_name = name

print(f"Highest score: {highest_name} with {highest_score}")

## Task 14: Guessing Game
Write a guessing game in Python where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed.

import random

secret_number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    tries += 1

    if guess < secret_number:
        print("Too small")
    elif guess > secret_number:
        print("Too large")
    else:
        print(f"Correct! It took you {tries} tries.")
        break

## Task 15: Lottery (Two-Digit)
Suppose you want to develop a program to play a lottery.

The program randomly generates a two-digit number, prompts the user to enter a two-digit number, and determines whether the user wins according to the following rules:
1. If the user's input matches the lottery in the exact order, the award is £10,000.
2. If all the digits in the user's input match all the digits in the lottery number, the award is £3,000.
3. If one digit in the user's input matches a digit in the lottery number, the award is £1,000.

import random

lottery = str(random.randint(10, 99))
guess = input("Enter a two-digit number: ")

if guess == lottery:
    print("You win £10,000")
elif len(guess) == 2 and sorted(guess) == sorted(lottery):
    print("You win £3,000")
elif len(guess) == 2 and any(digit in lottery for digit in guess):
    print("You win £1,000")
else:
    print("No prize")

print(f"The lottery number was {lottery}")

## Task 16: Lottery (Three-Digit)
The program prompts the user to enter a three-digit number and determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is £10,000.
2. If all the digits in the user input match all the digits in the lottery number, the award is £3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is £1,000.

import random

lottery = str(random.randint(100, 999))
guess = input("Enter a three-digit number: ")

if guess == lottery:
    print("You win £10,000")
elif len(guess) == 3 and sorted(guess) == sorted(lottery):
    print("You win £3,000")
elif len(guess) == 3 and any(digit in lottery for digit in guess):
    print("You win £1,000")
else:
    print("No prize")

print(f"The lottery number was {lottery}")

## Task 17: Find the Two Highest Scores
Write a program that prompts the user to enter the number of students and each student's score and displays the highest and second highest scores.

student_count = int(input("How many students? "))
scores = []

for _ in range(student_count):
    score = float(input("Enter a student's score: "))
    scores.append(score)

scores.sort(reverse=True)

print(f"Highest score: {scores[0]}")
print(f"Second-highest score: {scores[1]}")

## Task 18: Password Cracker
Write a program to print the accuracy of a password guess.

For example: The actual password is `MDX123` while a user tried `MDX321` or `mdx123`, the program should tell how accurately the password was guessed, in this case it should be `50%` accuracy. If a user enters `MDX124`, the output should be `83%` and in case of `123MDX` the output should be `0%`.

Points to keep in mind while calculating the accuracy:
- a) case of the letters entered
- b) order of the letters

If a password is accurately guessed, the output should state `Password cracked!`


actual_password = "MDX123"
guess = input("Guess the password: ")

if guess == actual_password:
    print("Password cracked!")
else:
    matching_characters = 0

    for actual, guessed in zip(actual_password, guess):
        if actual == guessed:
            matching_characters += 1

    accuracy = round(matching_characters / len(actual_password) * 100)
    print(f"Accuracy: {accuracy}%")
