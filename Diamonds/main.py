def main():
    print('Diamonds, by Babloo')
    #Display Diamonds of sizes 0 through 6:
    for diamondSize in range(0,6):
        displayOutlinedDiamond(diamondSize)
        print('\n'*2)
        displayFilledDiamond(diamondSize)
        print('\n'*2)


def displayOutlinedDiamond(size):
    #Display the top half of the Diamond:
    for i in range(size):
        print(' '*(size-i-1),end='')#left side space.
        print('/',end='')#left side of diamond.
        print(' '*(i*2),end='')#Interior of diamond.
        print('\\')#right side of the Diamond

    #Display bottom half of the Diamond:
    for i in range(size):
        print(' '*i,end='')#left side space.
        print('\\',end='')#Left side of Diamond.
        print(' '*((size-i-1)*2),end='')
        print('/')#right side of the diamond



def displayFilledDiamond(size):
    #Display top half of the Diamond
    for i in range(size):
        print(' '*(size-i-1),end='')#left side space.
        print('/'*(i+1),end='')#left half od diamond.
        print('\\'*(i+1))#Right half of Diamond

    #Display the  bottom half of the Diamond:
    for i in range(size):
        print(' '*i,end='')#Left side space.
        print('\\'*(size-i),end='')#Left side of the Diamond
        print('/'*(size-i))#Right side of Diamond

#Run main program:
if __name__=='__main__':
    main()



