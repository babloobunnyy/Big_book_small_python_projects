import sys, time

print('''This is Collatz Sequence, or the 3n+1 Problem
        If n is even, The next number n is n/2
        If n is odd, The next number n is 3n+1
        If n is 1, Stop. Otherwise, repeat.''')


print("Enter a starting number(greater than 0) or Quit: ")
response=input('>  ')

if not response.isdecimal() and response=='0':
    print("You must enter an Integer greater than 0")
    sys.exit()

n=int(response)
print(n,end='',flush=True)
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=3*n+1

    print(', '+str(n),end='',flush=True)
    time.sleep(0.1)
print()
