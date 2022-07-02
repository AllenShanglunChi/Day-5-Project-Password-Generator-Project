#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator coded by future exceptional programmer Allen Chi!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for letter in range(nr_letters):
#   password += letters[random.randint(0, nr_letters - 1)]

# for symbol in range(nr_symbols):
#   password += symbols[random.randint(0, nr_symbols - 1)]

# for number in range(nr_numbers):
#   password += numbers[random.randint(0, nr_numbers - 1)]

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for letter in range(nr_letters):
  password_list += letters[random.randint(0, nr_letters - 1)]
  #Or password_list.append(random.choice(letters))

for symbol in range(nr_symbols):
  password_list += symbols[random.randint(0, nr_symbols - 1)]
  #Or password_list += random.choice(symbols)

for number in range(nr_numbers):
  password_list += numbers[random.randint(0, nr_numbers - 1)]
  #Or password_list += random.choice(numbers)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char
print(f"Your password is: {password}")
