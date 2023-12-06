import os

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data

def tallyCards(data):
    score=0
    for line in data.split('\n'):
        matchCount=0
        numbers,winners=line.split('|')
        winners=winners.split()
        numbers=numbers.split(':')[1]
        numbers=numbers.split()
        for item in numbers:
            matchCount+=winners.count(item)
        print(numbers)
        print(winners)
        print(matchCount)
        if matchCount:
            score+=pow(2,(matchCount-1))
    return score

fileTest=os.path.join("/home/serve/Downloads","day4example.txt")
file=os.path.join("/home/serve/Downloads","inputday4.txt")

data=openfile(file)
score=tallyCards(data)
print(score)