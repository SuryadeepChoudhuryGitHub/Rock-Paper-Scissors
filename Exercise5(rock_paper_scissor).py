# to make a game like rock paper scissor
import random
i = 0
while i <1:
    while True:
        player_in = input("enter rock paper or scissor(r/p/s): ")
        if player_in == "r":
            index = 0
            break
        elif player_in == "p":
            index = 1
            break
        elif player_in == "s":
            index = 2
            break
        else:
            print("invalid input")

    computer_in = random.randint(0,2)

    computer_out = ["Rock", "Paper", "Scossor"]

    score = [
          # computer
        ["T", "C", "P"], 
        ["P", "T", "C"], #player
        ["C", "P", "T"]  
    ]
    
    if score[index][computer_in] == "T":
        print(f"Computer: {computer_out[computer_in]}")
        print("draw")
        
    elif score[index][computer_in] == "C":
        print(f"Computer: {computer_out[computer_in]}")
        print("Computer wins!")

    elif score[index][computer_in] == "P":
        print(f"Computer: {computer_out[computer_in]}")
        print("player wins!")

    while True:
        ask = input("do you want co continue: ").lower()

        if ask == "n":
            i = 2
            break
        elif ask == "y":
            break
        else:
            print("invalid input")
            