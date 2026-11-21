player1=input("Enter player 1 name: ")
player2=input("Enter player 2 name: ")
print(f"Player 1: {player1} vs Player 2: {player2}")
choices=["snake","water","gun"]
choice1=input(f"{player1}, choose from {choices}: ")
choice2=input(f"{player2}, choose from {choices}: ")
if choice1==choice2:
    print("It's a tie!")
elif (choice1=="snake" and choice2=="water") or (choice1=="water" and choice2=="gun") or (choice1=="gun" and choice2=="snake"):
    print(f"{player1} wins!")
else:
    print(f"{player2} wins!")