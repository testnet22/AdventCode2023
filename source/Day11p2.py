import os


fileSample=os.path.join("/home/serve/Python/Advent2023/data","day11example.txt")

file=os.path.join("/home/serve/Python/Advent2023/data","inputday11.txt")

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data

def printMap(map):
    for line in map:
        print(line)

def expandData(data):
    lines=data.split("\n")
    #printMap(lines)
    mapStars=(list(map(list,zip(*lines))))
    #printMap(mapStars)

    for n in range(len(mapStars)-1,0,-1):
        if '#' in mapStars[n]:
            next
        else:
            mapStars[n]=['+']*len(mapStars[0])
    #printMap(mapStars)
    print("")
    mapStars=(list(map(list,zip(*mapStars))))
    for n in range(len(mapStars)-1,0,-1):
        if '#' in mapStars[n]:
            next
        else:
            mapStars[n]=['+']*len(mapStars[0])
    #printMap(mapStars)
    return mapStars

def findStars(mapStars):
    stars=[]
    for y,row in enumerate(mapStars):
        for x,chr in enumerate(row):
            #print(chr,y,x)
            if chr=='#':
                stars.append((y,x))
    return stars

def subtractTuple(a,b):
    return tuple(abs(x-y) for x,y in zip(a,b))

expansionScale=1000000
data=openfile(file)
mapStars=expandData(data)
printMap(mapStars)
starLocations=findStars(mapStars)
#print(starLocations)
#printMap(bData)
sumValues=0
while(starLocations):
    star=starLocations.pop(0)
    r1,c1=star[0],star[1]
    #print(r1,c1)
    for (r2,c2) in starLocations:
        for r in range(min(r1,r2),max(r1,r2)):
            if(mapStars[r][c2]=='+'):
                sumValues+=expansionScale
            else:
                sumValues+=1
        for c in range(min(c1,c2),max(c1,c2)):
            if(mapStars[r2][c]=='+'):
                sumValues+=expansionScale
            else:
                sumValues+=1
        #sumValues.append(sum(subtractTuple((r2,c2),star)))

#print(sumValues)
print(sumValues)    
#print(sum(subtractTuple((10,9),(0,4))))