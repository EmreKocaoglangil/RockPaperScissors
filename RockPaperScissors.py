import random
chosenByUser = str(input("Please enter 'R' for Rock , 'S' for Scissors , 'P' for Paper = ")).upper()
chosenByComputer = random.choice(["R" , "P" , "S"])
def play():
    
    if chosenByComputer == chosenByUser:
        return f"Computer has chosen {chosenByComputer} Tie Game!"
    if winCondition(chosenByUser,chosenByComputer):
        return f"Computer has chosen {chosenByComputer} You Won!"
    return f"Computer has chosen {chosenByComputer} You Lost!"

def winCondition(player,oppenent):
    if (player == "R" and oppenent == "S") or (player == "S" and oppenent =="P") or (player == "P" and oppenent == "R"):
        return True
print(play())