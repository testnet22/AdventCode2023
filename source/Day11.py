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
            mapStars.insert(n,['.']*len(mapStars[0]))
    #printMap(mapStars)
    print("")
    mapStars=(list(map(list,zip(*mapStars))))
    for n in range(len(mapStars)-1,0,-1):
        if '#' in mapStars[n]:
            next
        else:
            mapStars.insert(n,['.']*len(mapStars[0]))
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

data=openfile(file)
mapStars=expandData(data)
starLocations=findStars(mapStars)
#print(starLocations)
#printMap(bData)
sumValues=[]
while(starLocations):
    star=starLocations.pop(0)
    for stars in starLocations:
        sumValues.append(sum(subtractTuple(stars,star)))
#print(sumValues)
print(sum(sumValues))    
#print(sum(subtractTuple((10,9),(0,4))))