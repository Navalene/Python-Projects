secret_number = 9
while True:
    guess = input("guess the secret number:")
    guess = int(guess)
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("You Win🏆")
        break


