#Program: This is the submitted solution file for Task 3, Assignment 1 
#Authors:
#Author1: Eyad Haytham Ashry, 20230077, Problems: 1, 3, 5
#Author2: Yaseen Mohamed Kamal, 20230468, Problems: 2, 4, menu design
#Author3: Mazem Amr Mohamed, 20230307, Problems: 6
#Version: 1.0
#Date: 23/2/2024



def p1():
	#A+=>=90,  90>A>=85 , 85>B+>=80 , 80>B>=75 , 75>C+>=65 , 65>C=<60 60>D+>=55 , 55>D=>50 ,  F<50
	while True:
		try:     #code to check if the input is an integer between 0 and 100
			grade=float(input("Please enter your mark: "))
			if grade<0 or grade>100:
				print ("Invalid input")  #display error message if the entered value is not integer between 0 and 100
				continue
			break
		except:ValueError
		print ("Invalid input")          #display error message if the entered value is not integer between 0 and 100

	if  grade >= 90 :
		print ("Your Grade is A+")
	elif 85 <= grade < 90 :
		print ("Your Grade is A")
	elif  80 <= grade < 85 :
		print ("Your Grade is B+")
	elif 75<= grade <80:
		print ("Your Grade is B")
	elif  65<= grade < 75:
		print ("Your Grade is C+")
	elif  60<= grade < 65:
		print ("Your Grade is C")
	elif   55<= grade < 60:
		print ("Your Grade is D+")
	elif   50<= grade < 55:
		print ("Your Grade is D")
	elif    0<=grade < 50:
		print ("Your Grade is F")
	return

def p2():
	usin = input("Enter number to check if Armstrong: ")	 
	pwr = len(usin)		#power variable which is based on the number of digits of the number that the user enters
	result = 0			#placeholder to add every digit raised to the power of the length of the number to
	for i in range(pwr):	#for loop that goes through every digit in the number
		resultbef = result
		result += int(usin[i]) ** pwr	#adds the digit^pwr to the result variable

	if str(result) == usin:		#compares the {result} variable to the user input to check if test succeeds
		print("Test success!!!\n\n\n")
	else:
		print("Test failure!!!\n\n\n")

def p3():
	result=1   
	count=1 
	x=3
	while True:
		#code to check if the input is integer
		try:       
			n = int(input("Please enter number of terms: "))
			break
		except ValueError:
			print("Invalid input. Please enter an integer.")    #display error message if the entered value is not integer

	while count<=n-1:
		if count%2==1:       #when count is odd
			result=result-(1/x)
			count=count+1
			x=x+2
			
		
		else:               #when count is even
			result=result+(1/x)
			count=count+1
			x=x+2
	print ("The result is: ",result)
	return 

def p4():
	mainstr = input("Enter string to cipher: ")		#mainstr variable contains message before ciphering
	ciphered = ""							#temporarily empty placeholder to contain the encrypted message
	for i in range(len(mainstr)):		#for loop to go through each character in the main string
		if(mainstr[i] == ' ' or mainstr[i] == '.' or mainstr[i] == ',' or mainstr[i] == ';'):	#condition to leave special characters and whitespace as they are
			ciphered += mainstr[i]
		
		elif(mainstr[i] == 'z'):	#wrap around z small character to be a
			ciphered += 'a'

		elif(mainstr[i] == 'Z'):	#wrap around Z capital character to be Z
			ciphered += 'A'
		else:
			ciphered += chr(ord(mainstr[i]) +1)	#ord() function gets ascii code for character, chr() function returns corresponding letter to the ascii code number entered

	print(f"Ciphered Message: {ciphered}\n\n\n")
 
def p5():
	firstlist=list(input("Please input the first list: "))
	secondlist=list(input("Please input the second list: "))

	# Check if each element in the first list is present in the second list
	for firstlist_element in firstlist:
		found = False
		for seclist_element in secondlist:
			if firstlist_element == seclist_element:
				found = True
				break
		if found==False:
			print("Lists are NOT equal")   # Print that an element from the first list was not found in the second list.
			break

	if found==True:
		print("Lists are equal")      # If all elements of the first list were found in the second list
	return 

def p6():
	num=int(input("Enter a number: "))
	if num>0:	#check to verify that number is positive
		print(f"Factors for {num} are:")
		for i in range(1,num+1):	#for each number smaller than the number specified
			fct = num/i		#variable contains number divided by i
			if fct%1==0:	#verify that it is a factor by checking that dividend is an integer
				print(i)
	return 

def main():		#main function where execution starts
	print("Welcome to Assignment 3 main menu.\nPlease Chose the number corresponding to your desired function from the list bellow.\n")
	uschoice = ''
	while uschoice != '7':		#while loop that repeats until user choses 7 to exit
		print("\n--------------------------------------------------------------")
		print("[1] Grading\n[2] Check Armstrong number")
		print("[3] Leibniz\n[4] Caesar Cipher")
		print("[5] Same Elements Check\n[6] Factors of +ve int")
		print("[7] Exit program")
		uschoice = input("-> ")
		if uschoice == '1':		#if statement to select functionaility based off of user choice 
			p1()
		elif uschoice == '2':
			p2()
		elif uschoice == '3':
			p3()
		elif uschoice == '4':
			p4()
		elif uschoice == '5':
			p5()
		elif uschoice == '6':
			p6()
		elif uschoice == '7':
			print("Exiting...")
		else:
			print("Invalid choice.")

main()		#Calling for main() function
