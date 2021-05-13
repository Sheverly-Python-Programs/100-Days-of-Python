'''
Write a program that switches the values stored in the variables a and b. 

**Warning.** Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

HINT: Think that variable a is like a glass of coffee and variable b is a cup of milk.
Think of a way on how you will switch the milk and coffee on one glass and the other.

ANSWER: You need a new cup. Likewise in Python, you need a new variable.

'''

# Solution

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
