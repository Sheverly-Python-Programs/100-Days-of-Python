'''
Instructions

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

**Warning.** Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

Hint

1. Try to find out the data type of two_digit_number.
2. Think about what you learnt about subscripting.
3. Think about type conversion.

'''
# Angela Yu's Answer:

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type of two_digit_number
print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits togeter
two_digit_number = first_digit + second_digit

print(two_digit_number)

# Sheverly's solution
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
#print(type(two_digit_number))
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])
print((first_number) + (second_number))


################ UPDATED ##################

two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))
number_1 = int(two_digit_number)
# print(type(number_1))
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])
final_sum = first_number + second_number
print(final_sum)
