# File: Problem3.py
# Purpose: My submition for Game problem number 3{Subtract a square}
# Author: Yaseen Mohamed Kamal El-Olemy 
# ID: 20230468

import random   #import the random module to randomize the starting number of coins/tokens

#If number of coins where to be in negative, program will exit and game will be deemed void


def main():
    list_of_squares = [1, 4, 9, 16, 25, 36]
    coins = random.randint(50, 100)   #select a random number of tokens between 50 & 100 
    print("Welcome to Subtract a square NIM")
    print("\nRules: \n-> Choose ONLY square number\n-> Maximum number is 36\n-> First to 0 wins\n")

    print("Initial number of tokens: " + str(coins) )

    while(coins>=0):
        player1 = int(input("-> Player 1: "))  #player one turn
        if(player1 not in list_of_squares):
            print("Please read the Rules again.")
        else:
            coins -= player1
            print("Number of coins "+ str(coins) + '\n')
        if(coins <= 0):
            print("Player 1 WON!!!")
            break
        
        player2 = int(input("-> Player 2: "))  #player two turn
        if(player2 not in list_of_squares):
            print("Please read the Rules again")
        else:
            coins -= player2
        if(coins <= 0):
            print("Player 2 WON!!!")
            break

        print("Number of coins "+ str(coins) + "\n")


    


main()
