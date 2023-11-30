import copy,random,sys,time

WIDTH=100
HEIGHT=50

ALIVE='0'
DEAD='.'

#The cells and the next cells are dictionaries for the state of the gane,
#Their keys are (x,y) tuples and their values are one of the ALIVE or Dead values

nextCells={}
#Put random dead and alive cells into next cells
for x in range(WIDTH):
    for y in range(HEIGHT):
        #50/50 chances of starting cell being alive or dead
        if random.randint(0,1)==0:
            nextCells[(x,y)]=ALIVE
        else:
            nextCells[(x,y)]=DEAD

while True:
    #Each iteration of this loop is a step of the simulations
    print('\n'*50)#Separate each step with newLines.
    cells=copy.deepcopy(nextCells)

    #print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)],end='')
        print()
    print("Press ctrl+C to quit")

    #caluclate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get the neighboring coordinates of (x,y), even if they wrap around the edge
            left=(x-1)%WIDTH
            right=(x+1)%WIDTH
            above=(y-1)%HEIGHT
            below=(y+1)%HEIGHT

            #Count the number of living nighbors:
            numNeighbors=0
            if cells[(left,above)]==ALIVE:
                numNeighbors+=1 #Top-left neighbour is alive
            if cells[(x,above)]==ALIVE:
                numNeighbors+=1 #Top neighbor is alive
            if cells[(right,above)]==ALIVE:
                numNeighbors+=1 #Top-right neig is alive
            if cells[(left,y)]==ALIVE:
                numNeighbors+=1 #left is alive
            if cells[(right,y)]==ALIVE:
                numNeighbors+=1 #Right neighbour is alive
            if cells[(left,below)]==ALIVE:
                numNeighbors+=1
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1


            #Set cells based on Conway's Game of life rules:

            if cells[(x,y)]==ALIVE and (numNeighbors==2
                or numNeighbors==3):
                #living cells with 2 or 3 neigjbour stay aliv

                nextCells[(x,y)]=ALIVE
            elif cells[(x,y)]==DEAD and (numNeighbors==3):
                nextCells[(x,y)]=ALIVE
            else:
                nextCells[(x,y)]=DEAD

        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("Conway's Game of life")
            sys.exit()



