first_number = input("Enter a number: ")
second_number = input("Enter another number: ")

first_number = int(first_number)
second_number = int(second_number)

print("addition:", first_number + second_number)
print("subtraction:", first_number - second_number)
print("multiplication:", first_number * second_number)
print("division:", first_number / second_number)
print("exponents:", first_number ** second_number)

name = input("what is your name?")
print("hello", name)
favorite_animal = input("what is your favorite animal?")
print("your lucky animal is", favorite_animal)
age = input("whats your age?")
print("so you are", age, "years old")
print(name, "at age", age, "will soon ride a giant", favorite_animal)

secret_number = 7
guess = input("guess the secret number:")
guess = int(guess)

if guess > secret_number:
     print("Too High")

if guess < secret_number:
    print("Too Low")
     
if guess == secret_number:
    print("correct!")
    
