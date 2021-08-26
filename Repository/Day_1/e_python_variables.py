'''
This is the same as the previous len() function topic. But this time, variable/s have been applied to the program.
'''

name = input("What is your name? ")
length = len(name) #this is to count the number of characters in "name" variable
print(length) # this is to print the result/total of length

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


