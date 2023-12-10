import os
from itertools import cycle

fileSample=os.path.join("/home/serve/Python/Advent2023/data","day8example.txt")
fileSample1=os.path.join("/home/serve/Python/Advent2023/data","day8example1.txt")
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

def findPath(lr,map):
    steps=0
    loopLR=cycle(lr)
    position='AAA'
    while position != 'ZZZ':
        steps+=1
        #print(map[position])
        #print(map[position]['L'])
        position=map[position][next(loopLR)]
        #print (position)
    print(steps)


data=openfile(file)
lr,map=parseData(data)
print(lr,map)
findPath(lr,map)
