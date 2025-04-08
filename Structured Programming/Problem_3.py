# File: Problem3.py
# Purpose: My submition for Game problem number 3{Subtract a square}
# Author: Yaseen Mohamed Kamal El-Olemy 
# ID: 20230468

import random   #import the random module to randomize the starting number of coins/tokens
import math     #used the math.sqrt() method to check if number has square root 

def main():
    print("Welcome to Subtrac
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
