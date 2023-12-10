import os
import math

fileSample=os.path.join("/home/serve/Python/Advent2023/data","day9example.txt")
file=os.path.join("/home/serve/Python/Advent2023/data","inputday9.txt")

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data

def findNext(sequence):
    tempList=[list(map(int,sequence))]
    #print(tempList)
    #while sum(tempList[0])!=0:
    while not(all(element==0 for element in tempList[0])):
        next=[]
        for n in range(len(tempList[0])-1):
            next.append(tempList[0][n+1]-tempList[0][n])
        tempList.insert(0,next)
        #print(tempList)

    tempList[0].append(0)
    #print(tempList)

    for n in range(len(tempList)-1):
        tempList[n+1].append(tempList[n][-1]+tempList[n+1][-1])
    #print(tempList)
    return tempList[-1][-1]

data=openfile(file)
sequences= [line.split() for line in data.split('\n')]
#sequences= map(int(),sequences)
#print(sequences)

nextValueArray=[]

for sequence in sequences:
    nextValueArray.append(findNext(sequence))
print(nextValueArray)
print(sum(nextValueArray))

