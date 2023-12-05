import random,time

#Setting up constants:
DICE_WIDTH=11

DICE_HEIGHT=5
CANVAS_WIDTH=99
CANVAS_HEIGHT=24-3 #-3 For room to enter the sum at the botom

#The duriation is in seconds:
QUIZ_DURATION=30 #You can change this to 10 or 60
MIN_DICE=2
MAX_DICE=6

REWARD=4 #reward points
PENALTY=1 #penalty points

# The program hangs if all the dice can' fit on the screen

assert MAX_DICE<=14

D1=(['+---------+',
     '|         |',
     '|    0    |',
     '|         |',
     '+---------+'],1)

D2a=(['+---------+',
      '|        0|',
      '|         |',
      '|0        |',
      '+---------+'],2)

D2b=(['+---------+',
      '|0        |',
      '|         |',
      '|        0|',
      '+---------+'],2)

D3a=(['+---------+',
      '|0        |',
      '|    0    |',
      '|        0|',
      '+---------+'],3)

D3b=(['+---------+',
      '|        0|',
      '|    0    |',
      '|0        |',
      '+---------+'],3)

D4= (['+---------+',
      '|0       0|',
      '|         |',
      '|0       0|',
      '+---------+'],4)

D5= (['+---------+',
      '|0       0|',
      '|    0    |',
      '|0       0|',
      '+---------+'],5)

D6a= (['+---------+',
       '|0       0|',
       '|0       0|',
       '|0       0|',
       '+---------+'],6)
D6b= (['+---------+',
       '|0   0   0|',
       '|         |',
       '|0   0   0|',
       '+---------+'],6)


ALL_DICE=[D1,D2a,D2b,D3a,D3b,D4,D5,D6a,D6b]

print(f'''Dice math game
        Add up the side of all the dice displayed on te screen
        You have {QUIZ_DURATION} to answer as many as possible.
        You get{REWARD} points for each correct answer and lose
        {PENALTY} points for each incorrect answer.''')


input("Please press enter to Begin....")

# Keep track of how many answers were correct and incorrect

correctAnswer=0
incorrectAnswer=0
startTime=time.time()
while time.time()< startTime+QUIZ_DURATION: #Main game loop
    #comeup with Dice to dispaly:
    sumAnswer=0
    diceFaces=[]
    for i in range(random.randint(MIN_DICE,MAX_DICE)):
        die=random.choice(ALL_DICE)
        #die[0] contains the list of strings of the die face
        diceFaces.append(die[0])
        #die[1] conatins the value of pips on the face
        sumAnswer+=die[1]

    #contains (x,y) tuples of the top-left corner of each die
    topLeftDiceCorners=[]

    #Figure out where the dice should go:

    for i in range(len(diceFaces)):
        while True:
            #Find a random place on the canvase to put the die
            left=random.randint(0,CANVAS_WIDTH-1-DICE_WIDTH)
            top=random.randint(0,CANVAS_HEIGHT-1-DICE_HEIGHT)

            #Get the x,y coordinates for all the four corners:

            topLeftX=left
            topLeftY= top
            topRightX=left+DICE_WIDTH
            topRightY=top
            bottomLeftX=left
            bottomLeftY=top+DICE_HEIGHT
            bottomRightX=left+DICE_WIDTH
            bottomRightY=top+DICE_HEIGHT

            #Check if this die overlaps wit previous dice

            overlaps=False
            for prevDieLeft,prevDieTop in topLeftDiceCorners:
                prevDieRight=prevDieLeft+DICE_WIDTH
                prevDieBottom=prevDieTop + DICE_HEIGHT
                #Check each of the corner of this die is to see
                #if it is inside of the area of the previous die:
                for cornerX,cornerY in ((topLeftX,topLeftY),
                                        (topRightX,topRightY),
                                        (bottomLeftX,bottomLeftY),
                                        (bottomRightX,bottomRightY)):
                    if (prevDieLeft<=cornerX<prevDieRight and prevDieTop<=cornerY<prevDieBottom):

                        overlaps=True


            if not overlaps:
                #It doesn't overlap, so we can put it here:
                topLeftDiceCorners.append((left,top))
                break

    #Draw the dice on the canvas:


    #Keys are (x,y) tuples of ints, values the character
    #at that position on the canvas:
    canvas={}
    #loop over each die
    for i,(dieLeft,dieTop)in enumerate(topLeftDiceCorners):
        #loops over each characters in the die's face
        dieFace=diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                #copy this character to the oorreect place on the canvase:
                canvasX=dieLeft+dx
                canvasY=dieTop+dy
                #Note that in diceface, list of strings
                #the x and y are swapped:
                canvas[(canvasX,canvasY)]=dieFace[dy][dx]


    #Display the canvas on the screen:
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx,cy),' '),end='')
        print()

    response=input('Enter the sun: ').strip()
    if response.isdecimal() and int(response)==sumAnswer:
        correctAnswer+=1
    else:
        print('Incorrect, The answer is', sumAnswer)
        time.sleep(2)
        incorrectAnswer+=1


#Display the final scores:
score=(correctAnswer*REWARD)-(incorrectAnswer*PENALTY)
print('Correct:  ', correctAnswer)
print('Incorrect:  ',incorrectAnswer)
print('Score', score)
