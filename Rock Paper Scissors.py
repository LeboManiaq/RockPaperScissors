from random import randint

AiComputerScore = 0
HumanScore = 0
t = ["Rock","Paper","Scissors"]

Human = False
print("First to three wins. Good Luck!!!")

while Human == False:
    AIComputer = t[randint(0,2)]
    Human = input("Who are you Rock, Paper or Scissors? ")

    if AIComputer == Human:
        print("CPU is also ",AIComputer,"Intense, Game Tie!!!", 
              "\n","Your score: ",HumanScore,"CPU score: ",AiComputerScore)
        Human = False

    elif Human == "Paper":
        if AIComputer == "Rock":
            HumanScore = HumanScore +1
            print("CPU is ",AIComputer, "You Win! you slap CPU with paper",
                  "\n", "Your score: ",HumanScore,"CPU score: ",AiComputerScore)
            Human = False
        
        else:
            AiComputerScore = AiComputerScore + 1
            print("CPU is ",AIComputer, "You Lose CPU tears you to shreds",
                  "\n","Your score: ",HumanScore,"CPU score: ",AiComputerScore)
            Human = False
            
    elif Human == "Rock":
        if AiComputerScore == "Paper":
            AiComputerScore = AiComputerScore + 1
            print("CPU is ",AIComputer,"You Lose!!! ",AIComputer, "squeezes ",Human, "to death",
                  "\n","Your score: ",HumanScore,"CPU score: ",AiComputerScore)
            Human = False

        else:
            HumanScore = HumanScore + 1
            print("CPU is ",AIComputer,"You Win!!! ",Human, "Smashes ",AIComputer, "to pieces",
                  "\n","Your score: ",HumanScore,"CPU score: ",AiComputerScore)
            Human = False

    elif Human == "Scissors":
        if AIComputer == "Rock":
            AiComputerScore = AiComputerScore +1
            print("CPU is ",AIComputer,"You Lose!!! ",AIComputer, "breaks ",Human, "to little pieces",
                  "\n","Your score: ",HumanScore,"CPU score: ",AiComputerScore)
            Human = False
        else:
            HumanScore = HumanScore + 1
            print("CPU is ",AIComputer,"You Win!!! ",Human, "cuts ",AIComputer, "into confettiPa",
                  "\n","Your score: ",HumanScore,"CPU score: ",AiComputerScore)
            Human = False
    if HumanScore == 3:
        print("You win the game, Lets see if you can win again")
        AiComputerScore = 0
        HumanScore = 0
    elif AiComputerScore == 3:
        print("You lose the game, better luck in the new round")
        AiComputerScore = 0
        HumanScore = 0
    else:
        Human = False