import random

randon_number = random.randint(1, 100)

running = True

while running:
    guess = int(input("Enter a number between 1 to 100: "))

    if guess < randon_number:
        print("Too Low!")
    elif guess > randon_number:
        print("Too High!")
    else:
        print("your guess is correct")
        running = False
    
