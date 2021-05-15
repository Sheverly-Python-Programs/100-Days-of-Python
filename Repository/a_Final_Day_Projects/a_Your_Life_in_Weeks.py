'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 
It will take your current age as the input and output a message with our time left in this format:
> You have x days, y weeks, and z months left. 
Where x, y and z are replaced with the actual calculated numbers. 
**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.
Hint
1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.
Test Your Code
Before checking the solution, try copy-pasting your code into this repl:
https://repl.it/@appbrewery/day-2-3-test-your-code
Solution [https://repl.it/@appbrewery/day-2-3-solution]
'''
#################################################################################################################################
# Sheverly's Solution

# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(type(age))
desired_days_age = int(90 * 365)
user_days_age = int(age * 365)
total_days = (desired_days_age - user_days_age)
#print(total_days)

desired_weeks_age = int(90 * 52)
user_weeks_age = int(age * 52)
total_weeks = (desired_weeks_age - user_weeks_age)
#print(total_weeks)

desired_months_age = int(90 * 12)
user_months_age = int(age * 12)
total_months = (desired_months_age - user_months_age)
#print(total_months)

print(f"You have {total_days} days, {total_weeks} weeks, and {total_months} months left.")

#################################################################################################################################

# Angela's Solution

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#################################################################################################################################
