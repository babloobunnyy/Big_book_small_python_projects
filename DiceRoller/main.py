import random, sys

print('''Dice Roller,
    Enter want kind kind and how many dice you want to
    roll. The format is number of dice, followed by
    "d", followed by the number of sides the dice have.
    You can also add a plus or minus adjustment
    
    Examples:
    3d6 rolls 3 six sided dice
    1d10+2 rolls 1 10 sided dice, and adds 2
    2d38-1 rolls two 38-sided die, and subtracts 1
    QUIT quits the program
    ''')

while True: #Main program loop:
    try:
        diceStr= input('>  ') #The prompt to enter the dice string
        if diceStr.startswith('q'):
            print('Thanks for playing!!')
            sys.exit()

    #Clean up the dice string:
        diceStr=diceStr.lower().replace(' ','')

    #Find the "d" in the dice string input:
        dIndex=diceStr.find('d')
        if dIndex==-1:
            raise Exception("Missing the 'd' character.")

    #Get the number of dice.( The "3" in "3d6+1"):
        numberOfDice=diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of Dice.')
        numberOfDice=int(numberOfDice)
    #Find if there is a plus or a minus sign:
        modIndex=diceStr.find('+')
        if modIndex==-1:
            modIndex=diceStr.find('-')

    #Find the number of sides. (The 6 in 3d6+1):
        if modIndex==-1:
            numberOfSides=diceStr[dIndex+1]
        else:
            numberOfSides=diceStr[dIndex+1:modIndex]
        if not numberOfSides.isdecimal():
            raise Exception("Missing the number of sides.")
        numberOfSides=int(numberOfSides)
    #Find the modifier amount.( The "1" in 3d6+1)
        if modIndex==-1:
            modAmount=0
        else:
            modAmount=diceStr[modIndex+1:]
            modAmount=int(modAmount)
            if diceStr[modIndex]=='-':
                modAmount=-modAmount

    # Simulate the dice rolls:
        rolls=[]
        for i in range(numberOfDice):
            rollResult=random.randint(1, numberOfSides)
            rolls.append(rollResult)

    #Display the total:
        print("Total: ", sum(rolls)+modAmount, '(Each die: ', end="")

    #Display the individual rolls:
        for i,roll in enumerate(rolls):
            rolls[i]=str(roll)
        print(', '.join(rolls), end='')
        print(' )')

    #Display the modifier amount:
        if modAmount!=0:
            modSign=diceStr[modIndex]
            print(f',{modSign} {abs(modAmount)}',end='')
            print(' )')

    except Exception as exc:
    #Catch any exception and display the message to the user:
        print("Invalid Input. Enter something like '3d6' ")
        print("Input was Invalid because:" + str(exc))
        continue #Go back to the dice string prompt
