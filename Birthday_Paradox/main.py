import datetime,random

def getBirthdays(numberofBirthdays):
    birthdays=[]
    for i in range(numberofBirthdays):
        startOfYear = datetime.date(1999,1,1)
        randomNumberOfDays=datetime.timedelta(random.randint(0,364))
        birthday=startOfYear+randomNumberOfDays
        birthdays.append(birthday)

    return birthdays


def getMatch(birthdays):
    if len(birthdays)==len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA==birthdayB:
                return birthdayA

print('''The Birthday paradox shows us that in  a group of N people, The
        odds that two of them having matching birthdays is surprisingly large.
        This program does a Monte Carlo simulation''')
print('''It is not actually a paradoc, It's just a surprising result.''')

MONTHS=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',)

while True:
    print('How many Birthdays shall I generate?(MAX 100')
    response=input('> ')
    if response.isdecimal()and(0<int(response)<=100):
        numBDays=int(response)
        break
print()
print()

print('Here are',numBDays,'birthdays:')
birthdays=getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i!=0:
        print(',',end='')

    monthName=MONTHS[birthday.month-1]
    dateText='{} {}'.format(monthName,birthday.day)
    print(dateText,end='')

print()
print()

match=getMatch(birthdays)
print('In This simulation, ', end='')
if match!=None:
    monthName=MONTHS[match.month-1]
    dateText='f{monthName} {Match.day}'
    print('multiple people have a birthday on', dateText)
else:
    print('There are no matching birthdays.')

print()

print('Generating', numBDays,'random birthdays 100,000 times....')
input('press Enter to begin....')

print('Let\'s run another 100,00 simulations.')
simMatch=0
for i in range(100_000):
    #Report on the progress every 10,000 simulations:
    if i%10_000==0:
        print(i, 'simulations run....')
    birthdays=getBirthdays(numBDays)
    if getMatch(birthdays)!=None:
        simMatch=simMatch+1
print('100,000 simulations run.....')
#
#Display result

probability=round(simMatch/100_000*100,2)
print('Out of 100,000 simulations of', numBDays, 'People, There was a ')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays,'people have a ', probability, '% chance of')
print('having a matching birthday in their group.')


