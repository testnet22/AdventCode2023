import re
import os

fileSample=os.path.join("/home/serve/Python/Advent2023/data","day10example.txt")
fileSample1=os.path.join("/home/serve/Python/Advent2023/data","day10example1.txt")
file=os.path.join("/home/serve/Python/Advent2023/data","inputday10.txt")

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data

def bufferData(data):
    lines=data.split("\n")
    lineLen=len(lines[0])
    lines.insert(0,lineLen*'.')
    lines.append(lineLen*'.')
    for n in range(0,len(lines)):
        lines[n]='.'+lines[n]+'.'
        lines[n]=list(lines[n])
    #print(type(lines))
    #print(type(lines[0]))
    #print(lineLen)
    return lines



def determineTwoStarts(map,sLocation):
    sY=sLocation[0]
    sX=sLocation[1]
    startLocations=[]
    
    possibles=['-','J','7']
    if map[sY][sX+1] in possibles:
        startLocations.append((sY,sX+1))

    possibles=['-','F','L']
    if map[sY][sX-1] in possibles:
        startLocations.append((sY,sX-1))

    possibles=['|','J','L']    
    if map[sY+1][sX] in possibles:
        startLocations.append((sY+1,sX))

    possibles=['|','7','F']    
    if map[sY-1][sX] in possibles:
        startLocations.append((sY-1,sX))
    
    return(startLocations)

def nextMove (map,position):
    y=position[0]
    x=position[1]
    newY=0
    newX=0
    #print('')
    if map[y][x] == '|':#| move north or south
        if map[y-1][x]=='X':
            newY=y+1
            newX=x
        else:
            newY=y-1
            newX=x
    if map[y][x] == '-': #- move east or west
        if map[y][x-1]=='X':
            newY=y
            newX=x+1
        else:
            newY=y
            newX=x-1
    if map[y][x] == 'L': #L move north or east
        if map[y-1][x]=='X':
            newY=y
            newX=x+1
        else:
            newY=y-1
            newX=x
    if map[y][x] == 'J': #J move north or west
        if map[y-1][x]=='X':
            newY=y
            newX=x-1
        else:
            newY=y-1
            newX=x
    if map[y][x] == '7': #7 move sourth or west
        if map[y+1][x]=='X':
            newY=y
            newX=x-1
        else:
            newY=y+1
            newX=x
    if map[y][x] == 'F': #F move south or east
        if map[y+1][x]=='X':
            newY=y
            newX=x+1
        else:
            newY=y+1
            newX=x

    return(newY,newX)
    
    
def locateStart(map):
    for n, line in enumerate(map):
        #print(line)
        if 'S' in line:
            return (n,line.index('S'))
        
def setPositionX(map,position):
    map[position[0]][position[1]]='X'
    return map

def printMap(map):
    for line in map:
        print(line)

def findPathLen(map):
    lenPath=1
    startPosition=locateStart(map)
    loopStarts=determineTwoStarts(map,startPosition)
    map=setPositionX(map,startPosition)
    loop1,loop2=loopStarts[0],loopStarts[1]
    print(loop1,loop2)
    
    while not(loop1==loop2):
        loop1new=nextMove(map,loop1)
        loop2new=nextMove(map,loop2)
        map=setPositionX(map,loop1)
        map=setPositionX(map,loop2)
        loop1=loop1new
        loop2=loop2new
        lenPath+=1
        #printMap(map)
    print(lenPath)




data=openfile(file)
bData=bufferData(data)
for line in bData:
    print(line)
findPathLen(bData)
#startPosition=locateStart(bData)
#print(startPosition)
#print(determineTwoStarts(bData,startPosition))
#determineTwoStarts(bData,startPosition)
#bData[startPosition[0]][startPosition[1]]='X'
#print(bData[startPosition[0]][startPosition[1]])

#nextPost=(startPosition[0],startPosition[1]+1)
#print(nextPost)
#print(bData[nextPost[0]][nextPost[1]])
#newPos=nextMove(bData,nextPost)
#print(newPos)
#print(bData[newPos[0]][newPos[1]])

#print(bData)