import random

def HumanGuess(lim):
     cp=random.randint(1,lim)

     guess=int(input(f"guess a no. between 1 to {lim}: "))

     while guess<cp:
           guess=int(input("a little more:"))

     while guess>cp:
        guess=int(input("a little less:"))

     print(f"congratulations! you've guessed the correct number, {cp}")

def CompGuess(lim):
    low=1
    high=lim
    answer=""

    while answer!="yes" and low!=high: 
        cg=random.randint(low,high)
        answer=input(f"is {cg} (low), (high) or (yes)?:")
        if answer=="low":
            low=cg-1
        if answer=="high":
            high=cg-1
    print(f"so the answer is {cg}. BAM!")

    


CompGuess(10)