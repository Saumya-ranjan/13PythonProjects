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

def computerguess(n):
    feedback = ""
    low = 1
    high = n
    while feedback != "c" and low != high :
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} higher put (h). if lower put (l). if correct (c)").lower()
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess+1
    print("u guess the number correctly")        
        
computerguess(10)     

