import random

#constant set up!

OBJECT_PRONOUNS=['Him','Her','Them']
POSSESIVE_PRONOUNS=['Her','His','Their']
PERSONAL_PRONOUNS=['She','He','They']
STATES=['Karnataka','TamilNadu','Kerala','Andra Pradesh',
        'Telengana','Madhya Pradesh','Goa','Maharastra',
        'Punjab','Gujurat','Arunachal pradesh', 'Jammu & Kadhmir']
NOUNS=['Athlete','Clown','Shovel','Doctor',
       'Lawyer','Student', 'Teacher','ZooKeeper','Babloo',
       'Police']
PLACES=['Don','Babloo','Lover','Serial killer',
       'ATM', 'Terror attack','Cricket','Lottery','House'
       'Deposit','Work place','Psycho killer','Robbery','Bank',
        'School','College']
WHEN=['Soon','This Year','Later Today','RIGHT NOW','Next week',
      'Coming month', 'Today', 'Tomorrow']


def generateAreMillialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f'Are Millennials killing the {noun} Industry?'


def generateWhatDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f'Without This {noun}, {pluralNoun} Could kill you {when}'


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper{noun2}'


def generateYouWontBelieveHeadline():
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    state = random.choice(STATES)
    place = random.choice(PLACES)
    noun = random.choice(NOUNS)
    return f'You won\'t Believe What this {state} {noun} found in {pronoun} {place}'


def generateDontWantYouToKnowHeadlinr():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return f'What {pluralNoun1} Don\'t Want you to know about{pluralNoun2}'


def generateGiftIdeaHeadline():
    state = random.choice(STATES)
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    return f'{number} Gift ideas to give your {noun} from {state}'


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    number2 = random.randint(1, number1)
    return f'{number1} Reasons Why {pluralNoun} Are Interseting than you think(Numbers {number2} will surprise you!!'


def generateJobAutomatedHeadlline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return f'''This is {state} {noun} Didn\'t Think
        Robots would take {pronoun1} Job. {pronoun2}
        were Wrong'''
    else:
        return f'''This {state} {noun} Didn\'t Think
        Robots would take {pronoun1} Job. {pronoun2}
        was Wrong'''


def main():
    print("This is a click bait generator")
    print()
    print("Our website needs to trick people into looking at ads")

    while True:
        print("How many click baits do you want?")
        response=input('>  ')
        if not response.isdecimal():
            print("Enter a number")
        else:
            numberOfHeadlines=int(response)
            break
    for i in range(numberOfHeadlines):
        clickbaitType=random.randint(1,8)
        if clickbaitType==1:
            headline=generateAreMillialsKillingHeadline()
        elif clickbaitType==2:
            headline=generateWhatDontKnowHeadline()
        elif clickbaitType==3:
            headline=generateBigCompaniesHateHerHeadline()
        elif clickbaitType==4:
            headline=generateYouWontBelieveHeadline()
        elif clickbaitType==5:
            headline=generateDontWantYouToKnowHeadlinr()
        elif clickbaitType==6:
            headline=generateGiftIdeaHeadline()
        elif clickbaitType==7:
            headline=generateReasonsWhyHeadline()
        elif clickbaitType==8:
            headline=generateJobAutomatedHeadlline()

        print(headline)
        print()
        print()

        website=random.choice(['wobsite','blag','Googles','X',
                               'Facenote','lateogram','bark'])
        when=random.choice(WHEN).lower()
        print("Post these to our",website,when, 'or you\'re fired!')


    #headlines functions


if __name__=='__main__':
    main()
