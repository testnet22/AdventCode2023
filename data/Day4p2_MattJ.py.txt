import os

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data

def tallyCards(data):
    intialNumberCards=len(data.split('\n'))
    numberCards=[1]*intialNumberCards
    card = data.split('\n')
    print(numberCards)
    for n in range(0,intialNumberCards):
        matchCount=0
        numbers,winners=card[n].split('|')
        winners=winners.split()
        numbers=numbers.split(':')[1]
        numbers=numbers.split()
        for item in numbers:
            matchCount+=winners.count(item)
        for i in range(1,matchCount+1):
            numberCards[n+i]+=1*numberCards[n]
            print(numberCards[n]," ",numberCards[n+i])
    print(numberCards)
    return sum(numberCards)

fileTest=os.path.join("/home/serve/Downloads","day4example.txt")
file=os.path.join("/home/serve/Downloads","inputday4.txt")

data=openfile(file)
score=tallyCards(data)
print(score)