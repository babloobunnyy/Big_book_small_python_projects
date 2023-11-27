import datetime
print("This is a calender maker")
print()

DAYS=('Sunday','Monday','Tuesday','Wednesday','Thursday',
      'Friday','Saturday')

MONTHS=('January','February','March','April','May','June',
        'July', 'August','September','October','November',
        'December')
while True:
    print('Please enter the year you want to print')
    response=input('> ')

    if response.isdecimal() and int(response)>0:
        year=int(response)
        break
    print("Please enter the valid year, like 2023")
    continue

while True:
    print("Enter the month of the calender you want to print. 1-12:")
    response=input('> ')
    if not response.isdecimal():
        print("please enter the valid month, Like 3 for march")
        continue
    month=int(response)
    if 1< month <=12:
        break

    print('Please enter a number from 1 to 12')

def getCalenderFor(year,month):
    calText=''
    calText+=(' '*34)+MONTHS[month-1]+' '+str(year) + '\n'
    calText+= '...Sunday....Monday....Tuesday....Wednesday....Thursday....Friday....Saturday..\n'

    #Hori line that separates weeks:

    weekSeparator=('+----------' * 7)+ '+\n'

    #The blank row will have 10 spaces in between | day separators

    blankRow=('|          '*7)+'| \n'

    currentDate=datetime.date(year,month,1)

    while currentDate.weekday()!=6:
        currentDate-=datetime.timedelta(days=1)

    while True:
        calText+=weekSeparator
        dayNumberRow=''
        for i in range(7):
            dayNumberLable=str(currentDate.day).rjust(2)
            dayNumberRow+='|'+dayNumberLable+(' '*8)
            currentDate+= datetime.timedelta(days=1)
        dayNumberRow+='|\n'

        calText+=dayNumberRow
        for i in range(3):
            calText+=blankRow
        if currentDate.month!=month:
            break

    calText+=weekSeparator
    return calText

calText=getCalenderFor(year,month)
print(calText)

calendarFileName=f'calendar{year}{month}'
with open(calendarFileName,'w') as fileObj:
    fileObj.write(calText)

print('Saved to'+ calendarFileName)
