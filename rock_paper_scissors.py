# Rock scissor and paper Game with Computer.
import random


def play():
    computers = random.choice(["r","p","s"])
    users = input("Enter (r) for rock (s) for scissor and (p) for paper :").lower()
    if users == computers:
        print("Tie")

    # Using different function in this function
    elif win(users,computers):
        return "You win"
    
    # Returning from the play function.
    return "You loose"
    
      
def win(user,computer):
   
    if user == "r" and computer == "s":
        print("You win")
    elif(user == "p" and computer =="r"):
        print("You win")
    elif(user =="s" and computer =="p"):
        print("You win")
    

play()