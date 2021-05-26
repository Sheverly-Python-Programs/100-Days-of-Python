import random
# This is to Split String method.
names_strings = input("Give me everybody's names, separated by a comma: \n")
names = names_strings.split(", ") # This is to Split the list of names.
# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items -1)
# Pick out random person from list of names using the random numnbers.
person_who_will_win = names[random_choice]
print(person_who_will_win + " is going to win the game today!")
