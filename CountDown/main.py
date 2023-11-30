import sys,time
import sevseg 

secondsLeft=10

try:
    while True:
        #Clear the screen by printing lines:
        print('\n'*50)
        #get hours second mins from the seconds left
        #Example 7265//3600 is 2 hours.
        hours=str(secondsLeft//3600)
        #And 7265%3600 is 65, and 65/60 is 1 minute
        minutes=str((secondsLeft%3600)//60)
        #And 7265%60 is 5 seconds:
        seconds=str(secondsLeft%60)

        #Gets the digit stings from sevseg module:
        hDigits=sevseg.getSevSegStr(hours,2)
        hTopRow,hMiddleRow,hBottomRow=hDigits.splitlines()
        mDigits=sevseg.getSevSegStr(minutes,2)
        mTopRow,mMiddleRow,mBottomRow=mDigits.splitlines()
        sDigits=sevseg.getSevSegStr(seconds,2)
        sTopRow,sMiddleRow,sBottomRow=sDigits.splitlines()

        #Display
        print(hTopRow       +'     '+mTopRow       +'     '+sTopRow)
        print(hMiddleRow       +'  :   '+mMiddleRow       +'  :   '+sMiddleRow)
        print(hBottomRow       +'  :   '+mBottomRow       +'  :   '+sBottomRow)

        if secondsLeft==0:
            print()
            print("*****---BOOOM---*****")
            break

        print()
        print('Press CTRL+C to stop')

        time.sleep(1)# Insert a one second pause.
        secondsLeft-=1

except KeyboardInterrupt:
    print("Count down by Babloo")
    sys.exit()
