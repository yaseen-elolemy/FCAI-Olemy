#By Yaseen Mohamed Kamal El-Olemy: 20230468

userinput = ''
convertfrom = ''
convertto = ''

def DecimaltoBinary(usernum):
    rval = ''
    while usernum > 0:
        rval = str(usernum%2) + rval
        usernum = usernum //2
    return rval

def DecimaltoOctal(usernum):
    octalnumber = [0] * 100
    i = 0
    while (usernum > 0):
        octalnumber[i] = usernum % 8
        usernum = int(usernum / 8)
        i += 1
    for k in range(i - 1, -1, -1):

        print(octalnumber[k], end="")

def DecimaltoHex(num):
    hexaDeciNumber = ['0'] * 100
    i = 0
    while(num!= 0):
        temp = 0
        temp = num % 16
        if(temp < 10):
            hexaDeciNumber[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNumber[i] = chr(temp + 55)
            i = i + 1
        num = int(num / 16)
    j = i - 1
    while(j >= 0):
        print((hexaDeciNumber[j]), end="")
        j = j - 1


def BinarytoDecimal(binary):
    i = len(binary)-1
    number = 0
    powers = 0
    while(i>=0):
        if binary[i] == '1':
            number += 2**powers
        powers += 1
        i -= 1
    return number

def BinarytoOctal(binary):
    usernum = BinarytoDecimal(binary)
    octalnumber = [0] * 100
    i = 0
    while (usernum > 0):
        octalnumber[i] = usernum % 8
        usernum = int(usernum / 8)
        i += 1
    for k in range(i - 1, -1, -1):

        print(octalnumber[k], end="")

def BinarytoHex(binary):
    num = BinarytoDecimal(binary)
    hexaDeciNumber = ['0'] * 100
    i = 0
    while(num!= 0):
        temp = 0
        temp = num % 16
        if(temp < 10):
            hexaDeciNumber[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNumber[i] = chr(temp + 55)
            i = i + 1
        num = int(num / 16)
    j = i - 1
    while(j >= 0):
        print((hexaDeciNumber[j]), end="")
        j = j - 1


def OctaltoDecimal(num):
    decimal_value = 0
    base = 1

    while num:
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value

def OctaltoBinary(octalu):
    usernum = OctaltoDecimal(octalu)
    rval = ''
    while usernum > 0:
        rval = str(usernum%2) + rval
        usernum = usernum //2
    print(rval)

def OctaltoHex(octalu):
    num = OctaltoDecimal(octalu)
    hexaDeciNumber = ['0'] * 100
    i = 0
    while(num!= 0):
        temp = 0
        temp = num % 16
        if(temp < 10):
            hexaDeciNumber[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNumber[i] = chr(temp + 55)
            i = i + 1
        num = int(num / 16)
    j = i - 1
    while(j >= 0):
        print((hexaDeciNumber[j]), end="")
        j = j - 1


def HextoDecimal(uhex):
    uhex = uhex.strip().upper()
    num = 0
    hexdict = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10 , 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
    hexlen = len(uhex) - 1
    for digit in uhex:  
        num += hexdict[digit]*16**hexlen  
        hexlen -= 1
    return num

def HextoBinary(uhex):
    usernum = HextoDecimal(uhex)
    rval = ''
    while usernum > 0:
        rval = str(usernum%2) + rval
        usernum = usernum //2
    return rval

def HextoOctal(uhex):
    usernum = HextoDecimal(uhex)
    octalnumber = [0] * 100
    i = 0
    while (usernum > 0):
        octalnumber[i] = usernum % 8
        usernum = int(usernum / 8)
        i += 1
    for k in range(i - 1, -1, -1):

        print(octalnumber[k], end="")


def converter(cfrom, cto):             #cfrom: type of number to convert from. cto: type of number to convert to
    if(cfrom == cto):                  #shows an error message if user chose to convert to the same number type
        print("Error: can't convert two equal number types\n")
        return -1
    if(cfrom == 'A'):               #user choose from decimal, call functions corresponding to which type to transfer to, same of all else if statements
        userint = int(input('Enter the number in integer: '))
        if(cto =='B'):
            print(DecimaltoBinary(userint))
        elif(cto == 'C'):
            DecimaltoOctal(userint)
        elif(cto == 'D'):
            DecimaltoHex(userint)
    elif(cfrom == 'B'):
        userbin = input('Enter number in Binary: ')
        if(cto == 'A'):
            print(BinarytoDecimal(userbin))
        elif(cto  == 'C'):
            BinarytoOctal(userbin)
        elif(cto == 'D'):
            BinarytoHex(userbin)
    elif(cfrom == 'C'):
        useroct = int(input("Enter nubmer in Octal: "))
        if(cto == 'A'):
            print(OctaltoDecimal(useroct))
        elif(cto == 'B'):
            OctaltoBinary(useroct)
        elif(cto == 'D'):
            OctaltoHex(useroct)
    elif(cfrom == 'D'):
        userhex = input("Enter number in hex: ")
        if(cto == 'A'):
            print(HextoDecimal(userhex))
        elif(cto == 'B'):
            print(HextoBinary(userhex))
        elif(cto == 'C'):
            HextoOctal(userhex)






while(userinput != 'B'):                                        #Beginning of execution here, displaying multiple menus and getting input from the user
    print("\n** numbering system converter **\nA) insert a new number\nB) Exit program\n")
    userinput = str(input("-> "))
    if(userinput == 'A'):
        print("\n** Please select the base you want to convert a number from**\nA) Decimal\nB) Binary\nC) octal\nD) hexadecimal\n")
        convertfrom = str(input('-> '))
        if(convertfrom != 'A' and convertfrom != 'B' and convertfrom != 'C' and convertfrom != 'D'):
            print("please enter a valid choice\n")
        else:
            print('\n** Please select the base you want to convert a number to **\nA) Decimal\nB) Binary\nC) octal\nD) hexadecimal\n')
            convertto = str(input('-> '))
            if(convertto != 'A' and convertto != 'B' and convertto != 'C' and convertto != 'D'):
                print('please enter a valid choice')
            else:
                converter(convertfrom, convertto)               #main function which handles all the conversion and calling other converter functions
    elif(userinput != 'A' and userinput != 'B'):
        print("please select a valid choice:\n")
