import re
import os

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data

def mapNewValue(value,dsr):
    for mapping in dsr:
        destination,source,r=mapping
        destinationEnd=destination+r-1
        sourceEnd=source+r
        result=0
    #print("Des",destination,"-",destinationEnd)
    #print("source",source,"-",sourceEnd)
        if(value in range(source,sourceEnd)):
            return value-source+destination
    return value

def createSeeds(data):
    seedlist=[]
    lines=data.split('\n')
    seeds=lines[0].split()
    seeds.pop(0)
    #print(seeds)
    for i in range(len(seeds)):
        seedlist.insert(i,
            {
            'seed':int(seeds[i]),
            'soil':0,
            'fertilizer':0,
            'water':0,
            'light':0,
            'temperature':0,
            'humidity':0,
            'location':0
            }
        )
    return seedlist
        
def getMappings(data):
    mappings=[]
    data+='\n'
    data=data.split('\n')
    data.pop(0)
    data.pop(0)
    for k in range(0,7):
        tempMappings=[]
        data.pop(0)
        while data[0]:
            line=data.pop(0)
            line=line.split()
            mapLine=list(map(int,line))
            tempMappings.append(mapLine)
        #print(mappings)
        #line=map(int,line)
        #print(line)
        #print(mappings)
        #mappings[k].append(map(int():line.split()))
        mappings.insert(k,tempMappings)
        data.pop(0)
#    print(mappings)
#    print(data)
    return mappings

def mapValues(seeds,mappings):
    index=[
        'seed',
        'soil',
        'fertilizer',
        'water',
        'light',
        'temperature',
        'humidity',
        'location'
    ]
    for i,mp  in enumerate(mappings):
        print(index[i+1],"-",mappings[i],'*****')
        for seed in seeds:
            seed[index[i+1]]=mapNewValue(seed[index[i]],mp)
            print(seed)
    return seeds
        

fileSample=os.path.join("/home/serve/Python/Advent2023/data","day5example.txt")
file=os.path.join("/home/serve/Downloads","inputday5.txt")
runData=openfile(fileSample)

seeds=createSeeds(runData)
mappings=getMappings(runData)
finalLocations=mapValues(seeds,mappings)

locationArray=[]
for location in finalLocations:
    locationArray.append(location['location'])

print(min(locationArray))
#print(seeds)
#print(seeds[0])
#seeds[0]['seed']=0
#print(seeds)
#print(mappings)
#x=mapNewValue(79,[[50,98,2],[52,50,48]])
#print(x)
