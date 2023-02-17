import random

def get_choices():
    player = input("Enter a choice [rock , paper, scissors] :")
    options = ["rock", "paper", "scissors"]
    comupter = random.choice(options)
    game_start = {"You": player, "AI": comupter}

    if game_start.get("You") == game_start.get("AI"):
        print(game_start)
        print("it's a tie")
    elif game_start.get("You") == "scissors" and game_start.get("AI") == "paper":
        print(game_start)
        print("Winner")
    elif game_start.get("You") == "rock" and game_start.get("AI") == "paper":
        print(game_start)
        print("Lose")
    elif game_start.get("You") == "rock" and game_start.get("AI") == "scissors":
        print(game_start)
        print("Winner")
    elif game_start.get("You") == "paper" and game_start.get("AI") == "scissors":
        print(game_start)
        print("Lose")
    elif game_start.get("You") == "paper" and game_start.get("AI") == "rock":
        print(game_start)
        print("Winner")
    elif game_start.get("You") != "paper" or "rock" or "scissors":
        print("Choose a valid key !!!!!!!!!!!!")     
    else:
        print(game_start)
        print("Lose") 
    
        
a = get_choices()
print(a)