# snake ,gun and water game 
import random

def gamewin(comp,you):
    if comp == you :
        return None
    elif comp =='s':
        if you =='g':
            return True
        elif you =='w':
            return False

    elif comp =='g':
        if you =='w':
            return True
        elif you =='s':
            return False
    elif comp =='w':
        if you =='s':
            return True
        elif you =='g':
            return False


print("computer turn , choose : snake(s),water(w),gun(g)")

randNo = random.randint(1,3)

if randNo == 1:
    comp ='s'
elif randNo == 2:
    comp = 'w'

elif randNo == 3 :
    comp = 'g'


you =input("your turn ,choose: snake(s),water(w),gun(g):..")

a=gamewin(comp,you)
print(f"computer choose ::..{comp}")
print(f"you choose::.. {you}")

if a == None :
    print("game is Tie !")
elif a :
    print("You win the game")

else:
    print("You lose the game")