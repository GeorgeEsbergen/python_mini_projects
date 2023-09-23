import random 
def rollDice():
    drawing_dice= {
        1:(
            " _________",
            "|         |",
            "|         |",
            "|    *    |",
            "|         |",
            "|_________|",
        ),
        2:(
            " _________",
            "|         |",
            "|   *     |",
            "|         |",
            "|     *   |",
            "|_________|",
        ),
        3:(
            " _________",
            "|         |",
            "|  *      |",
            "|    *    |",
            "|      *  |",
            "|_________|",
        ),
        4:(
            " _________",
            "|         |",
            "|  *   *  |",
            "|         |",
            "|  *   *  |",
            "|_________|",
        ),
        5:(
            " _________",
            "|         |",
            "|  *   *  |",
            "|    *    |",
            "|  *   *  |",
            "|_________|",
        ),
        6:(
            " _________",
            "|         |",
            "|  *   *  |",
            "|  *   *  |",
            "|  *   *  |",
            "|_________|",
        ),
    }

    roll=input("woudl you like to roll dice ? y/n").lower()
    while roll == "y" or roll=="yes" : 
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        print(f"Dice Rolled {dice1} and {dice2}")
        print(f"\n".join(drawing_dice[dice1]))
        print(f"\n".join(drawing_dice[dice2]))
        roll = input("Would you roll again ? y/n")


rollDice()

