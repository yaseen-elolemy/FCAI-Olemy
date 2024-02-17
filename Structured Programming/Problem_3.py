# File: Problem3.py
# Purpose: My submition for Game problem number 3{Subtract a square}
# Author: Yaseen Mohamed Kamal El-Olemy 
# ID: 20230468

import random   #import the random module to randomize the starting number of coins/tokens
import math     #used the math.sqrt() method to check if number has square root 

def main():
    print("Welcome to Subtract a square")       #welcome message
    choice = ''
    while(choice != 'enter' or choice != 'random'):
        choice = input("Would you like to enter an arbitrary number of tokens or Generate it randomly?\n\t[enter/random]: ") #ask user whether to choose number or randomize it
        if(choice == "enter"):
            tokens = int(input("Enter number of tokens: "))
            break
        elif(choice == "random"):
            tokens = random.randint(30, 300)    #random number range wasn't specified in problem page so I chose from 30  to 300
            print("Initial number of tokens is "+str(tokens))
            break
        else:
            print("Error: Please choose correct option...") #choice prompt is case sensetive must enter like in 2nd print statement above
    
    while(tokens>=0):   #while statement that keeps looping until number of tokens is less than ZERO
        player1 = int(input("Player1: "))   #asks player1 to enter number to take
        if(player1> tokens):    #shows error message if player choses to take more tokens than available
            print("ERROR: number selected cannot be greater than number of tokens")
        elif(str(math.sqrt(player1))[-2] != '.'):   #explanation at end of file on how to check whether user entered number is square
            print("ERROR: number doesn't have a square")
        else:
            tokens -= player1       #subtract number specified by player from the tokens
            print("Number of tokens: "+str(tokens)) #print message to show current number of tokens
        if(tokens == 0):    #check to see if user wins by comparing tokens to Zero
            print("Player 1 Won!!!") #if so then game declares winner, breaks while loop, and exits program
            break                    #if not then it proceeds to player 2 turn
        player2 = int(input("player2: "))   #player 2 algorithm, exactly identical as player 1's
        if(player2> tokens):
            print("ERROR: number selected cannot be greater than number of tokens")
        elif(str(math.sqrt(player2))[-2] != '.'):
            print("ERROR: number doesn't have a square")
        else:
            tokens -= player2
            print("Number of tokens: "+str(tokens))
        if(tokens == 0):
            print("Player 2 Won!!!")
            break
        
main()


'''in order to check whether user entered number has square or not; we call the sqrt method and typecast its 
return value into String, for example for 16 it will return exactly '4.0', so in order to check whether it has
square or not we see if the 2nd character from the right is a dot, if so then it is a square if not then the number
is NOT a square and we return an Error'''
