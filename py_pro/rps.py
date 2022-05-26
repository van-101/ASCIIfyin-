import random

def move():
    your_move=str(input("(rock)/(paper)/(scissor):"))
    computer=random.choice(["rock", "paper", "scissor"])
    print(winner(your_move, computer))


def winner(x,y):
    
    if(x==y):
        return "tie"
    elif(x=="rock" and y=="scissor" or x=="scissor" and y=="paper" or x=="paper" and y=="rock"):
        return f"user wins, with {x} over {y}!"
    else:
        return f"computer wins, with {y} over with {x}!"

move()