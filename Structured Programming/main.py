#Description:
#Authors:
#Author1: Eyad Haytham Ashry, 20230077, Problems: 1, 3, 5
#Author2: Yaseen Mohamed Kamal, 20230468, Problems: 2, 5
#Author3: Mazem Amr Mohamed, ...
#Version: 1.0
#Date: 23/2/2024



def p1():
	return

def p2():
	usin = input("Enter number to check if Armstrong: ")	#str datatype 
	pwr = len(usin)
	result = 0
	for i in range(pwr):
		resultbef = result
		result += int(usin[i]) ** pwr
		#print(f"Added {int(usin[i]) ** pwr} to {resultbef}, result: {result}\n")


	if str(result) == usin:
		print("Test success!!!\n\n\n")
	else:
		print("Test failure!!!\n\n\n")

def p3():
	return 

def p4():
	mainstr = input("Enter string to cipher: ")
	ciphered = ""
	for i in range(len(mainstr)):
		if(mainstr[i] == ' ' or mainstr[i] == '.' or mainstr[i] == ',' or mainstr[i] == ';'):
			ciphered += mainstr[i]
		
		elif(mainstr[i] == 'z'):
			ciphered += 'a'

		elif(mainstr[i] == 'Z'):
			ciphered += 'A'
		else:
			ciphered += chr(ord(mainstr[i]) +1)

	print(f"Ciphered Message: {ciphered}\n\n\n")
 

def p5():
	return 

def p6():
	return 

def main():
	print("Welcome to Assignment 3 main menu.\nPlease Chose the number corresponding to your desired function from the list bellow.\n\n")
	uschoice = ''
	while uschoice != '7':
		print("[1] Grading\n[2] Check Armstrong number")
		print("[3] Lebniz\n[4] Caesar Cipher")
		print("[5] Same Elements Check\n[6] Factors of +ve int")
		print("[7] Exit program")
		uschoice = input("-> ")
		if uschoice == '1':
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





main()