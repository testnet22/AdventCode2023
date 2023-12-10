import re
import os
from operator import itemgetter

fileSample=os.path.join("/home/serve/Python/Advent2023/data","day7example.txt")
file=os.path.join("/home/serve/Python/Advent2023/data","inputday7.txt")

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip().replace('A','E').replace('K','D').replace('Q','C').replace('J','B').replace('T','A')
    return data

def readCards(data):
    lines=data.split('\n')
    cards=[]
    for line in lines:
        card,bet=line.split()
        cards.append([card,bet])
    return(cards)

def sortCard(card):
    num=[]
    alp=[]
    str=''
    for chr in card:
        if chr.isnumeric():
            num.append(chr)
        else:
            alp.append(chr)
    return str.join(sorted(alp,reverse=True)+sorted(num,reverse=True))

def handRank(hand):
    #HighCard 9
    sortedHand=sortCard(hand)
    #print(hand,':',sortedHand)
    #five kind, Four kind, full house, three kinds, two pairs, one pair, high card, 1, 2, 3 4
    fiveKind=re.findall(r'(\w)\1{4}',sortedHand)#FiveKind F
    if(fiveKind):
        return 'F'+hand 
    
    fourKind=re.findall(r'(\w)\1{3}',sortedHand)#FourKind E
    if(fourKind):
        return 'E'+hand
    
    fullHouse=re.findall(r'(\w)\1{2}(\w)\2{1}',sortedHand)#FullHouse D
    if(fullHouse):
        return 'D'+hand
    fullHouse=re.findall(r'(\w)\1{1}(\w)\2{2}',sortedHand)
    if(fullHouse):
        return 'D'+hand

    threeKind=re.findall(r'(\w)\1{2}',sortedHand) #ThreeKind C
    if(threeKind):
        return 'C'+hand
    
    twoKind=re.findall(r'(\w)\1{1}',sortedHand) #TwoPair B
    if(len(twoKind)==2):
        return 'B'+hand
    if(twoKind):              #OnePair A
        return 'A'+hand
    
    return '9'+hand #Highcard

def handsToNumbers(hands):
    #print(hands)
    sumProduct=0

    for hand in hands:
        hand[0]=handRank(hand[0])
        hand.append(int(hand[0],16))

    hands=(sorted(hands,key=itemgetter(2)))
 
    for i,hand in enumerate(hands):
        sumProduct+=(i+1)*int(hand[1])
    print("sum of all",sumProduct)

data=openfile(file)
hands=readCards(data)
handsToNumbers(hands)
    