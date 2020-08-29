import random
 
hidden = random.randrange(1, 201)
print(hidden)


guess = int(input("Please enter your guess: "))

while True:
    if guess == hidden:
        print("Hit! Congrats you have guessed successfully")
        break
    elif guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    guess = int(input("Please enter your guess: "))
