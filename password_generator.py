import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password_choices = []
for letter in range(0, nr_letters):
    password_choices.append(random.choice(letters))
for number in range(0, nr_numbers):
    password_choices.append(random.choice(numbers))
for symbol in range(0, nr_symbols):
    password_choices.append(random.choice(symbols))

password = ''
for choice in range(0, len(password_choices)):
    random_number = random.randint(0, len(password_choices) - 1)
    password += password_choices.pop(random_number)

print(f"Your password is {password}")