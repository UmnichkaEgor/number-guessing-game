from random import randint

print("Welcome to the number guessing game!")

lol = int(input("Enter a number that is the maximum of the number you will guess: "))

num = randint(1, lol)

def is_valid(w):
    if w < 1 or w > lol:
        return False
    else:
        return True

popitka = 0

while True:
    versuch = int(input("Guess the number: "))
    
    if is_valid(versuch) == False:
        print(f"Maybe we should still keep the number from 1 to {lol}?")
        continue
    else:
        pass
    
    popitka += 1

    if versuch < num:
        print("Too little. Try again.")
    elif versuch > num:
        print("Too much. Try again.")
    else:
        print("You guessed it. Congratulation!")
        break

print()       
print(f"Thank you for playing our game! You had {popitka} attempts!")







