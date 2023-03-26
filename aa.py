# import random
# def winner(player,opponent):
#     if(player == "r" and opponent=="s") or (player == "s" and opponent =="p") or (player == "p" and opponent =="r"):
#         return True
# def lets_play():
#     print("lets play a Rock Papper Scissor Game for Fun")
#     print("""-------MENU--------------
#              r = ROck
#              p = Papper
#              s = Scissor""")
#     user = input("enter r , p or s for game choice ").lower()
#     print("Your choice is",user)
#     computer = random.choice(['r','p','s'])
#     print("Opponent choice is",computer)
#     if user == computer:
#         print("Tie!!!")
#     elif winner(user,computer):
#         print("You won the game")
#     else:
#         print("you lose the game")
# lets_play()
import random
def winner(player, opponent):
    if (player=="r" and opponent =="p") or (player == "s" and opponent == "p") or (player == "p" and opponent =="r"):
        return True
    
def lets_play():
    print("""Enter any letter from r , p , s/
                    r = ROck
                    p = paper
                    s = scissor""")
    user = input("enter any letter from suggestions  ")
    print("so you enter",user)
    computer = random.choice(['r','p','s'])
    print("so the opponent choice" , computer)
    if user == computer:
        print("Tie....!")
    elif winner(user,computer):
        print("You won")
    else:
        print("you lose")
lets_play()
again =input("Want to play again/n please say yes or no  ")
if again=="yes":
    print("okay lets play again")
else:
    print("okay the end")
for i in range(0,3):
    lets_play()


