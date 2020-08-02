import random
number=random.randint(1,9)
chance=0
while chance<=5:
    guess=int(input("Enter a number:"))
    if guess<number:
        print("Your guess is too low guess a number greater than",guess)
    elif guess>number:
        print("Your guess is too high guess a number less than",guess)
    else:
        print("Congrats!! Your guess is correct")
        break
    chance=+1    
if chance>5:
    print("Your chances are over try again later")
