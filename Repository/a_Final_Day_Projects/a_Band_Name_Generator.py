'''
Create a Band Name Generator using all what you have learned.
1. Create a greeting for your program.
2. Ask the user for the city that they grew up in.
3. Ask the user for the name of a pet.
4. Combine the name of their city and pet and show them their band name.
5. Make sure the input cursor shows on a new line, see the example at:
https://band-name-generator-end.appbrewery.repl.run/
'''

print("Hello! Welcome to the Band Name Generator!")

city = input("From what city did you grew up?: \n")

pet = input("What is the name of your pet?: \n")

print("Your Band name could be " + city + " " + pet)


#1. Create a greeting for your program.
print("Hola! Welcome to Band Name Generator!\nIn order to generate the name of the Band, please answer the following questions below. Thank you!\n")
#2. Ask the user for the city that they grew up in.
city = input("From what city do you grew up in? ")
#3. Ask the user for the name of a pet.
pet = input("What is the name of your pet? ")
#4. Combine the name of their city and pet and show them their band name.
print("Now the name of your band is " + city + " " + pet + ". Congratulations!")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
