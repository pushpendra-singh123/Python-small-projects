import random  # you will make it like rock ,paper,scissors

# Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True

print("Comp Turn: Rock(r) or Scissor(s) or Paper(p)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 's'
elif randNo == 3:
    comp = 'p'

you = input("Your Turn: Rock(r) or Scissor(s) or Paper(p)?")
a = gameWin(comp, you)

print(f"Computer chose: {comp}")
print(f"You chose: {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")