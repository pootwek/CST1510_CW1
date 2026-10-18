# Week 1 – Values, Types and Input/Output – Programming Problems

## Task 1: Questionnaire
Write a program that asks for name, interest, nationality, course, and programming experience, then prints a formatted summary using escape sequences (`\n`, `\t`).

**Example Output:**
```
User Information:
	Name: Alice
	Interest: Security
	Nationality: UK
	Course: Cyber
	Experience: Beginner
```
name = input("Name: ")
interest = input("Interest: ")
nationality = input("Nationality: ")
course = input("Course: ")
experience = input("Experience: ")

print("\nUser Information:")
print("\tName:", name)
print("\tInterest:", interest)
print("\tNationality:", nationality)
print("\tCourse:", course)
print("\tExperience:", experience)	

## Task 2: Rectangle Area & Perimeter
Calculate and print the area and perimeter of a rectangle using fixed values: width = 4.5 and height = 7.9.
Formulas: `area = width * height`, `perimeter = 2 * (width + height)`.

**Example Output:**
```
Area = 35.55
Perimeter = 24.80

width = 4.5
height = 7.9

area = width * height
perimeter = 2 * (width + height)

print("Area =", area)
print("Perimeter =", perimeter)
perimeter = 24.8
area=35.04
```

## Task 3: Convert Pounds to Kilograms
Ask the user for a value in pounds, convert to kilograms using `1 lb = 0.454 kg`, and print the result.

**Example Output:**
```
55.5 pounds is 25.197 kilograms

pounds = float(input("Enter pounds: "))
kilograms = pounds * 0.454

print(pounds, "pounds is", kilograms, "kilograms")
318lbs is 144.372kg
```

## Task 4: Convert Feet to Meters
Ask the user for a value in feet, convert to meters using `1 ft = 0.305 m`, and print the result.

**Example Output:**
```
16.5 feet is 5.0325 meters
```
feet = float(input("Enter feet: "))
metres = feet * 0.305

print(feet, "feet is", metres, "metres")

## Quick Check (no code submission)
- What data type does `input()` return? Use `type(input("x"))` to verify.
- Show one example of an escape sequence in `print()`.
- What is the difference between `/` and `//`? Provide a one-line example for each.
input() returns a string, even if you type a number.

An escape sequence example is print("Hello\nWorld"). The backslash n starts a new line.
7 / 2 gives 3.5. 7 // 2 gives 3 because it rounds the result down to a whole number.
## Task 5: Total Time to Watch a Series
Compute total viewing time (no breaks) for a series:
- 5 seasons, 10 episodes per season
- Season 1: 45 minutes 35 seconds per episode
- Seasons 2–5: 35 minutes 15 seconds per episode

Display the total as hours, minutes, and seconds.



**Example Output:**
```
Total time: 39h 30m 0s
```

season_1_seconds = 10 * (45 * 60 + 35)
seasons_2_to_5_seconds = 40 * (35 * 60 + 15)

total_seconds = season_1_seconds + seasons_2_to_5_seconds

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("Total time:", hours, "h", minutes, "m", seconds, "s")

## Task 6: Savings Projection (3 Years)
Compute final savings after 3 years given:
- Save £10 every week for 3 years
- Year 1 bonus: +£20 each week
- Every 2 weeks: −£0.50 (sister)

Assume 52 weeks per year; use arithmetic and augmented assignment; no conditionals.

**Example Output:**
```
Final savings after 3 years: £4689.50

savings = 0

savings += 10 * 52 * 3
savings += 20 * 52

two_week_periods = (52 * 3) // 2
savings -= 0.50 * two_week_periods

print("Final savings after 3 years: £", savings)
```

## Task 7: Cyber: HTTP Log Composer
Ask for IP, method, path, status, and bytes, then print a single combined log line (Apache-style).

**Example Output:**
```
192.168.1.10 - "POST /auth" 401 512

ip = input("IP address: ")
method = input("Method: ")
path = input("Path: ")
status = input("Status code: ")
bytes_sent = input("Bytes sent: ")

log_line = ip + ' - "' + method + " " + path + '" ' + status + " " + bytes_sent
print(log_line)
```

## Task 8: Pure Python EDA: Dataset Metadata
Ask for dataset name, rows, and columns. Print:
- dataset name in quotes
- rows and columns
- total cells (rows × columns)

**Example Output:**
```
"sales.csv"
Rows: 120
Columns: 8
Cells: 960

dataset_name = input("Dataset name: ")
rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))

total_cells = rows * columns

print('"' + dataset_name + '"')
print("Rows:", rows)
print("Columns:", columns)
print("Cells:", total_cells)
```

## Task 9: IT: INI-style Config Printer
Ask for three `key=value` pairs (via separate prompts) and print them as an INI block with indentation.

**Example Output:**
```
[config]
	max_connections = 200
	timeout = 30
	region = eu-west-2
```
key1 = input("First key: ")
value1 = input("First value: ")

key2 = input("Second key: ")
value2 = input("Second value: ")

key3 = input("Third key: ")
value3 = input("Third value: ")

print("[config]")
print("\t" + key1 + " = " + value1)
print("\t" + key2 + " = " + value2)
print("\t" + key3 + " = " + value3)

## Task 10: Sum of First n Integers
Ask for a positive integer `n` and compute the sum `n*(n+1)//2`. Print the result.

**Example Output:**
```
Sum of 1..10 = 55
```
n = int(input("Enter a positive integer: "))
total = n * (n + 1) // 2

print("Sum of 1.." + str(n) + " = " + str(total))



## Task 11: Population Projection (5 Years)
Assume current population is 312032486 and 1 year = 365 days.
Rates: birth every 7s, death every 13s, immigrant every 45s.
Compute projected population for each of the next 5 years using integer division (`//`).

**Example Output:**
```
Year 1: 315,xxx,xxx
...
Year 5: ...
```
*Optional hint:* Compute yearly net change once; then add each year.

seconds_per_year = 365 * 24 * 60 * 60

births = seconds_per_year // 7
deaths = seconds_per_year // 13
immigrants = seconds_per_year // 45

yearly_change = births - deaths + immigrants
population = 312032486

for year in range(1, 6):
    population += yearly_change
    print("Year", year, ":", population)

## Task 12: Payroll Statement
Ask for: employee name, hours worked, hourly rate, federal tax rate, state tax rate.
Print a formatted payroll slip with gross pay, each deduction, and net pay (2 d.p.).

**Example Output:**
```
Employee: Smith
Gross pay: £97.50
Federal withholding: £19.50
State withholding: £8.78
Net pay: £69.22
```


name = input("Employee name: ")
hours = float(input("Hours worked: "))
hourly_rate = float(input("Hourly rate: "))
federal_rate = float(input("Federal tax rate (%): ")) / 100
state_rate = float(input("State tax rate (%): ")) / 100

gross_pay = hours * hourly_rate
federal_tax = round(gross_pay * federal_rate, 2)
state_tax = round(gross_pay * state_rate, 2)
net_pay = gross_pay - federal_tax - state_tax

print("Employee:", name)
print("Gross pay: £{:.2f}".format(gross_pay))
print("Federal withholding: £{:.2f}".format(federal_tax))
print("State withholding: £{:.2f}".format(state_tax))
print("Net pay: £{:.2f}".format(net_pay))
