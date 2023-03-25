from random import randint
from time import sleep
player=input("rock(r), paper(p) or scissors(s):\n")
chosen=randint(1,3)
computer=()

if chosen==1:
    computer=("rock")
elif chosen==2:
    computer=("paper")
elif chosen==3:
    computer=("scissors")
else:
    computer=(ValueError)

if player==("r"):
    player=("rock")
elif player==("p"):
    player=("paper")
elif player==("s"):
    player=("scissors")
else:
    player=(TypeError)

print (player, "vs", computer)

if player==computer:
    print ("draw")
elif player==("rock") and computer==("scissors"):
    print ("player wins!")
elif player==("paper") and computer==("rock"):
    print ("player wins!")
elif player==("scissors") and computer==("paper"):
    print ("player wins!")
elif computer==("rock") and player==("scissors"):
    print ("computer wins")
elif computer==("paper") and player==("rock"):
    print ("computer wins")
elif computer==("scissors") and player==("paper"):
    print ("computer wins")

sleep(10)