import random  # Importing random module for generating random numbers
import time    # Importing time module for adding delay
import os      # Importing os module for clearing the console

def runers(numero1,numero2): #Function to print the positions of two runners.
    print((numero1*" ") + "O" )
    print((numero2*" ") + "O" )

def cash(): #Function to start the game by getting initial money from the user.
    money = int(input("Write the amount of money: "))
    while money < 10:
        money = int(input("Write the amount of money greater than 10: "))

    carrera(money)

def carrera(money): #Function to handle the race and betting logic.

    thisMoney = money

    if thisMoney < 5:
        print("you lost all sorry :C")
        exit()

    optionContinue = 1  #Variable to control the continuation of the game
    while optionContinue == 1:
        moneyToBet = int(input("how amount do you want to bet?: "))
        while moneyToBet < 5:
            moneyToBet = int(input("the amount needed greater than 5: "))

        while moneyToBet > thisMoney:
            moneyToBet = int(input(f"You cannot bet this amount, bet an amount less or equal to {thisMoney}: "))

        bet = int(input("select your bet is 1 or 2 "))
        while bet != 1 and  bet != 2:
            try:
                bet = int(input("Select just 1 or 2: "))
            except ValueError:
                print("Please enter a valid number.")

        counter1 = 0
        counter2 = 0
        while (counter1 < 40) and (counter2 < 40):
            numero = random.randint(1, 2)

            if numero == 1:
                counter1 += 1
            
            if numero == 2:
                counter2 += 1

            os.system("cls")# Clear the console for Windows or Unix-based systems
            print(runers(counter1,counter2))# Print the positions of the runners
            time.sleep(0.05)# Add a small delay for better visualization

        winner = 1 if counter1 == 40 else 2 # Determine the winner

        if winner == bet: # Update the money if the bet is correct
            thisMoney += moneyToBet
            print(f"you won!! \ncurrent money: {thisMoney}")
            optionContinue = int(input("do you want to continue? \n1.yes \n2.no:\n"))
        else:
            thisMoney -= moneyToBet # Update the money if the bet is incorrect
            print(f"you lost \n current money: {thisMoney}")
            optionContinue = int(input("do you want to continue? \n1.yes \n2.no:\n"))

        while optionContinue != 1 and  optionContinue != 2:
            try:
                optionContinue = int(input("Select just 1 or 2 \n1. Yes \n2. No:\n"))
            except ValueError:
                print("Please enter a valid number.")

        if optionContinue == 1:
            carrera(thisMoney)
        if optionContinue == 2:
            print(f"you won!! {thisMoney}")
            exit()
cash()