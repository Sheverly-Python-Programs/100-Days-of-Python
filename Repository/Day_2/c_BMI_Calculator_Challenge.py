'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
https://www.omnicalculator.com/health/bmi
*** Warning you should convert the result to a whole number.
Hint
1. Check the data type of the inputs.
2. Try to use the exponent operator in your code.
3. Remember PEMDAS.
4. Remember to convert your result to a whole number (int). 
Test Your Code: https://repl.it/@appbrewery/day-2-2-test-your-code
Solution: https://repl.it/@appbrewery/day-2-2-solution
'''
########################################################################################################################
# Sheverly's Answer

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# This is to get the Data type of height and weight.
print(type(height)) # results will be 'str'
print(type(weight)) # results will be 'str'

# This is to convert the Data type from 'str' to 'int'.
user_height = float(height)
user_weight = int(weight)

final_bmi = int(user_weight / (user_height ** 2))  # results will be 'int' to make it whole number
print(final_bmi)

########################################################################################################################
# Angela's Solution

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)

########################################################################################################################

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = int(weight) / float(height) ** 2
BMI_Whole_Number = int(BMI)
print(BMI_Whole_Number)
