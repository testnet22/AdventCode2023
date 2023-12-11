import re
import os
import copy

fileSample2=os.path.join("/home/serve/Python/Advent2023/data","day10example2.txt")
fileSample3=os.path.join("/home/serve/Python/Advent2023/data","day10example3.txt")
fileSample4=os.path.join("/home/serve/Python/Advent2023/data","day10example4.txt")
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
    possibleS=[]
    sValue='X'
    
    possibles=['-','J','7']
    if map[sY][sX+1] in possibles:
        startLocations.append((sY,sX+1)) #east
        possibleS.extend(['-','F','L'])

    possibles=['-','F','L'] #west
    if map[sY][sX-1] in possibles:
        startLocations.append((sY,sX-1))
        possibleS.extend(['-','J','7'])

    possibles=['|','J','L']    #south
    if map[sY+1][sX] in possibles:
        startLocations.append((sY+1,sX))
        possibleS.extend(['|','F','7'])

    possibles=['|','7','F']    #north
    if map[sY-1][sX] in possibles:
        startLocations.append((sY-1,sX))
        possibleS.extend(['|','J','L'])
    for item in possibleS:
        if possibleS.count(item)==2:
            sValue=item
    #print(possibleS)
    return(startLocations),sValue

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
    loopStarts,sValue=determineTwoStarts(map,startPosition)
    map=setPositionX(map,startPosition)
    loop1,loop2=loopStarts[0],loopStarts[1]
    #print(loop1,loop2)
    
    while not(loop1==loop2):
        loop1new=nextMove(map,loop1)
        loop2new=nextMove(map,loop2)
        map=setPositionX(map,loop1)
        map=setPositionX(map,loop2)
        loop1=loop1new
        loop2=loop2new
        lenPath+=1
        #printMap(map)
    map=setPositionX(map,loop1)
    return map
    #print(lenPath)

def noExtraPipe(input,pathMap):
    cleanOut=input
    #printMap(cleanOut)
    for i,line in enumerate(cleanOut):
        for j,chr in enumerate(line):
            #print(chr)
            
            if pathMap[i][j]=='X':
                cleanOut[i][j]=cleanOut[i][j]
            else:
                cleanOut[i][j]='.'
            #print(pathMap[i][j],cleanOut[i][j])
    return cleanOut

def getChr(map,y,x):
    return map[y][x]

def whatIsS(map):
    sy,sx=locateStart(map)
    s=locateStart(map)
    otherEnds, sValue=determineTwoStarts(map,s)
    map[sy][sx]=sValue
    
    return map

data=openfile(file)
bData=bufferData(data)
#printMap(bData)
startData=copy.deepcopy(bData)

map=findPathLen(bData)
#print("")
#printMap(startData)
#printMap(map)
#print("")
cleanMap=noExtraPipe(startData,map)
printMap(cleanMap)
print("")
cleanMap=whatIsS(cleanMap)
#printMap(cleanMap)

for col,line in enumerate(cleanMap):
    out=True
    bowl=''
    for row, chr in enumerate(line):
        if out:
            #print(chr)
            if chr == '.':
                cleanMap[col][row]='O'
        if not(out):
            if chr == '.':
                cleanMap[col][row]='I'
        if chr== '|':
            out=not(out)
        if chr in 'LF':
            bowl=chr
            #print(bowl)
        elif chr == '7':
            if bowl == 'L':
                out=not(out)
        elif chr == 'J':
            if bowl =='F':
                out=not(out)
sum=0
for line in cleanMap:
    sum+=line.count('I')        


printMap(cleanMap)
print(sum)

