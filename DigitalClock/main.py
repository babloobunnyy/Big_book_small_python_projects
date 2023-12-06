import sys, time, sevseg

try:
    while True: #Main program loop
        #Clear screen by printing several lines
        print('\n'*60)

        #Get the current time from the computer's clock:
        currentTime=time.localtime()
        # %12 so we can use a 12-hour clock, not 24:
        hours=str(currentTime.tm_hour%12)
        if hours=='0':
            hours='12' #12-hour clock shows 12:00
        minutes=str(currentTime.tm_min)
        seconds=str(currentTime.tm_sec)

        hDigits=sevseg.getSevSegStr(hours,2)
        hTopRow,hMiddleRow,hBottomRow=hDigits.splitlines()
        mDigits=sevseg.getSevSegStr(minutes,2)
        mTopRow,mMiddleRow,mBottomRow=mDigits.splitlines()
        sDigits=sevseg.getSevSegStr(seconds,2)
        sTopRow,sMiddleRow,sBottomRow=sDigits.splitlines()

        #Display the digital clock

        print(hTopRow   +'    '+ mTopRow +'    '+ sTopRow)
        print(hMiddleRow   +'    '+ mMiddleRow +'    '+ sMiddleRow)
        print(hBottomRow   +'    '+ mBottomRow +'    '+ sBottomRow)


        print("Press CTRL+C to quit.")


except KeyboardInterrupt:
    print("Digital clock by babloo")
    sys.exit()
