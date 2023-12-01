import random,sys,time

WIDTH=70
PAUSE_AMOUNT=0.05

print('Deep cave')
print('Press CTL+C to Stop.')
time.sleep(2)

leftWidth=20
gapWidth=10

while True:
    #Display the tunnel segment:
    rightWidth=WIDTH-gapWidth-leftWidth
    print(('#'*leftWidth)+(' '*gapWidth)+('#'*rightWidth))
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()#When CTRL+C is pressed
    #Adjust left side width:
    diceRoll=random.randint(1,6)
    if diceRoll==1 and leftWidth>1:
        leftWidth=leftWidth-1#Decresses left side width.
    elif diceRoll==2 and leftWidth+gapWidth<WIDTH-1:
        leftWidth=leftWidth+1#Increase left side width.
    else:
        pass

    #Adjust the gap width:
    #
    # diceRoll=random.randint(1,6)
    # if diceRoll==1 and gapWidth>1:
    #     gapWidth=gapWidth-1
    # elif diceRoll==2 and leftWidth+gapWidth<WIDTH-1:
    #     gapWidth=gapWidth+1
    # else:
    #     pass


