"""Make practice passwords using random letters, numbers and symbols."""

import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters do you want? "))
nr_symbols = int(input("How many symbols do you want? "))
nr_numbers = int(input("How many numbers do you want? "))

# easy version: put the character groups in order
easy_password = ""
for _ in range(nr_letters):
    easy_password += random.choice(letters)
for _ in range(nr_symbols):
    easy_password += random.choice(symbols)
for _ in range(nr_numbers):
    easy_password += random.choice(numbers)

print("easy password:", easy_password)

# hard version: mix all the characters before joining them
password_list = []
for _ in range(nr_letters):
    password_list.append(random.choice(letters))
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = "".join(password_list)
print("shuffled password:", password)
