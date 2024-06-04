import random
round_total = 0
player1_score=0
player2_score=0
turns=5
player=0 #player 1 is zero and player 2 is 2

def dice():
     return random.randint(1,6)
     
while turns > 0:
    roll=dice()
    prompt = ""
    while prompt !="h":
        if roll == 1:
            print(roll)
            print(f"Player {player + 1} rolled a 1 and loses the round points. Current total: {player1_score if player == 0 else player2_score}")
            break
        else:
            round_total+=roll
            print(roll)
            prompt=input("do you want to hold or reroll (h or r) if you want to quit type q: ")
            if prompt == "h":
                break
            elif prompt == "r":
                roll=dice()
                continue
            elif prompt =="q":
                exit()
            else:
                print("Invalid input. Please enter 'r' to roll again or 'h' to hold.")
        if player == 0:
            player1_score += round_total
            player=1
        else:
            player2_score += round_total
            player=0
        round_total = 0
        turns -= 1
print(player1_score)
print(player2_score)
            
            