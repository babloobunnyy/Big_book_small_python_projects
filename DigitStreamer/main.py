#Digital Streamer

import random,shutil,sys,time

MIN_STREAM_LENGTH=60
MAX_STREAM_LENGTH=140

PAUSE=0.1

STREAM_CHARS=['0','1'] #you can change this characters.


#Density can range from 0.0 to 1.0:
DENSITY=0.02

#Get the size of the terminal window:
WIDTH=shutil.get_terminal_size()[0]

#We can't print to the last colum on Windows without it
#adding a newline automaically, so reduce the width by one:

WIDTH-=1

print("Digital Stram, by Babloo")
print('Press CTRL-C to quit.')
time.sleep(2)

try:
    #For each column, when the counter is 0 no stream is shown.
    #Otherwise, it acts as a counter for how many times a 1 or 0
    #Should be displayed in that column.
    columns=[0]*WIDTH
    while True:
        #Set up counter for each column:
        for i in range(WIDTH):
            if columns[i]==0:
                if random.random()<=DENSITY:
                    #Restart a Stream on this column:
                    columns[i]=random.randint(MIN_STREAM_LENGTH,MAX_STREAM_LENGTH)

            if columns[i]>0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i]-=1
            else:
                print(' ',end='')

        print()#Prints a new line at the end of the row
        sys.stdout.flush()#Make sure the text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
