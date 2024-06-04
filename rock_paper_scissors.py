import random

player_wins=0

computer_wins=0

ties=0

amount_of_games=0
options=["rock","paper","scissors"]

print("let's play rock,paper,scissors and if you wanna quit type q ")

while True:
    user_input = input("Enter either rock paper or scissors: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        print("That is not correct")
        continue  
    computer_input = random.randint(0,2)

    computer_response=options[computer_input]
    
    amount_of_games+=1
    
    print("You choose",user_input)
    print("The computer choose",computer_response)

    if user_input=="scissors" and computer_response == "paper":
        print("You win")
        player_wins+=1
    elif user_input=="rock" and computer_response == "scissors":
        print("You win")
        player_wins+=1
    elif user_input=="paper" and computer_response == "rock":
        print("You win")
        player_wins+=1
    elif user_input == computer_response:
        print("You tied")
        ties +=1 
    else:
        print("You lose")
        computer_wins+=1 
        
        
player_avarage = (player_wins/amount_of_games) * 100
computer_avarage=(computer_wins/amount_of_games) *100
tie_avarage= (ties/amount_of_games)*100
print("game over")
print(f"You won {player_avarage:.2f}% of the games.")
print(f"You lost {computer_avarage:.2f}% of the games.")
print(f"You tied {tie_avarage:.2f}% of the games.")