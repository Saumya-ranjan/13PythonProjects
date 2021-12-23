import random

# We guess the Number:
def randomguess(x):

    Number  = random.randint(1,x)
    guess = 0
    while guess != Number:
        guess = int(input("Guess the Number between 1 and {}:".format(x)))
        if Number > guess: 
           print("Ur value is somewhat less than the computer NUmber")
        elif Number < guess: 
           print("Ur value is somewhat more than the computer NUmber")
    print("You have Guessed the Number Correctly") 
randomguess(10)


# Computer Guess the Number Now: 
