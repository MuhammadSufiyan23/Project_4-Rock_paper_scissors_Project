# PROJECT: 4
#ROCK, PAPER, SCISSOR GAME PROJECT

import random


choices = ["rock", "paper", "scissors"]
emoji_dict = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

print("🎮 Welcome to Rock, Paper, Scissors!")
print("🤖 You are playing against the computer. Let's see who wins!")


player_choice = input("🔢 Enter Rock, Paper, or Scissors: ").lower()



if player_choice not in choices:
    print("⚠️ Invalid choice! Please choose Rock, Paper, or Scissors.")
else:
    computer_choice = random.choice(choices)


    print(f"\n👤 Player chose: {emoji_dict[player_choice]} {player_choice.capitalize()}")
    print(f"💻 Computer chose: {emoji_dict[computer_choice]} {computer_choice.capitalize()}\n")


    if player_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("🎉 Player Wins! 🏆")
    else:
        print("😔 Computer Wins! 💻🏆")
