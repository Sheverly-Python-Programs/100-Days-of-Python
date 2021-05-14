'''
Type () - Function that would check whatever you put between the parentheses and give you the type.
Type Checking and Type Conversion
'''

# Sample of Type Checking
num_char = len(input("What is your name? "))
print(type(num_char)) # --- <class 'int'>

# Sample of Type Conversion
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Other samples with mathematical operators
a = float(123)  # --- <class 'float'>
b = str(123)  # --- <class 'str'>
c = int(123)  # --- <class 'int'>
print(type(a))
print(type(b))
print(type(c))

print(70 + float("100.5")) # --- 170.5
print(str(70) + str(100)) # --- 70100
