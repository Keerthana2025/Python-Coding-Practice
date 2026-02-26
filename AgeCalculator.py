Python Exercise 1.2: Age Calculator
Create a Python program that asks for the user's birth year and calculates their current age.

Your program should:

Ask the user for their Birth Year (integer).
Get the Current Year (e.g., 2025).
Calculate the Age by subtracting the birth year from the current year.
Print the result in a friendly sentence.
Bonus Challenge: Handle the case where they haven't had their birthday yet this year (requires asking for birth month/day). For this basic exercise, we will assume the birthday has passed.

Sample Interaction:
Input
Output
2000
Enter your birth year: 2000
--------------------
Current Year: 2025
You are approximately 25 years old.

CODE:
import datetime
# 1. Ask for Birth Year
birthyear = int(input("Enter your BirthYear: "))
# 2. Get Current Year
current_year = datetime.date.today().year
# 3. Calculate Age
age = current_year - birthyear
# 4. Print the result
print("You are", age, "years old.")

OUTPUT:
Enter your BirthYear: 2003
You are 23 years old.

=== Code Execution Successful ===
