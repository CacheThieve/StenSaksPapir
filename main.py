import random
import pygame



while True:  
    userAction = input("Take a Choice(Sten, Saks, Papir): ").title()

    possibleActions = ["Sten", "Saks", "papir"]
    computerAction = random.choice(possibleActions)
    print(f"Du har valgt {userAction} \nComputeren har valgt {computerAction}.")

    if userAction == computerAction:
        print(f"I har begge valgt {userAction}. Det blev uafgjort! ")
    elif userAction == "Sten":
        if computerAction == "Saks":
            print("Sten slår saks! Du vinder! ")
        else:
            print("Papir slår sten! Du taber! ")
    elif userAction == "Papir":
        if computerAction == "Sten":
            print("Papir slår sten! Du vinder ")
        else:
            print("Saks Slår papir! DU taber! ")
    elif userAction == "Saks":
        if computerAction == "Papir":
            print("Saks slår papir! Du vinder! ")
        else:
            print("Sten slår Saks! Du Taber !")
            
    playAgain = input("Spil igen? (j/n): ")
    if playAgain.lower() != "j":
        break

    