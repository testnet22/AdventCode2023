import os
from itertools import cycle
import math

fileSample=os.path.join("/home/serve/Python/Advent2023/data","day8example2.txt")
file=os.path.join("/home/serve/Python/Advent2023/data","inputday8.txt")

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data

def parseData(data):
    mapD={}

    lr,map=data.split('\n\n')
    lr=[*lr]
   
    for line in map.split('\n'):
        key,lrMap=line.replace(' ','').split('=')
        l,r=lrMap.replace('(','').replace(')','').split(',')
        #print(key,l,r)
        mapD[key]={'L':l,'R':r}

    return lr,mapD

def findPath(start,lr,map):
    steps=0
    loopLR=cycle(lr)
    position=start
    print(position)
    while not (position.endswith('Z')) or not (steps != 0):
        steps+=1
        #print(map[position])
        #print(map[position]['L'])
        position=map[position][next(loopLR)]
        #print (position)
    return steps#position]
    


data=openfile(file)
lr,map=parseData(data)
print(lr,map)
#findPath(lr,map)
#allKeys=map.keys()
startPoints = [key for key in map if key.endswith('A')]
firstZ=[]
for start in startPoints:
    firstZ.append(findPath(start,lr,map))
#for first in firstZ:
    #print(first[1])
#    first.append(findPath(first[1],lr,map))
lcm=firstZ.pop()
for num in firstZ:
    lcm=math.lcm(num,lcm)

print(lcm)
#print(firstZ)
#findPath('11Z',lr,map)
#findPath('22Z',lr,map)

