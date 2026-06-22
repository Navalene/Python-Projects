import random
length = input("How long do you want the password to be?")
length = int(length)

print("So the password will be", length, "characters long")

numbers = input("Do you want to include numbers? (yes/no): ")
symbols = input("Do you want to include symbols? (yes/no): ")

characters = "abcdefghijklmnopqrstuvwxyz"

if numbers == "yes":
    characters = characters + "0123456789"

if symbols == "yes":
    characters = characters + "!@#$%^&*()?"

password = ""

for i in range(length): 

    random_char = random.choice(characters)

    password = password + random_char
print("Your secure password is:", password)
