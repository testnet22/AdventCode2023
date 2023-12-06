import re
import os
import cmath
import math

def openfile(path):
    with open(path,"r") as f:
        data = f.read().strip()
    return data

def parseInput(Data):
    #print(Data.split("\n")[0].split(':')[1].replace(" ",""))
    time=int((Data.split("\n")[0].split(':')[1].replace(" ","")))
    print(Data.split("\n"))
    print(Data.split("\n")[1].split(':')[1].replace(" ",""))
    distance=int((Data.split("\n")[1].split(':')[1].replace(" ","")))
    #print(time)
    print(distance)
    return time,distance
        
def compute(time,distance):
    product=1
    d=cmath.sqrt(time**2-distance*4)
    d=d.real
    #print(d)
    x1=((time+d)/2)
    x2=((time-d)/2)
    if(x2.is_integer()):
        x2+=1
    x2=math.ceil(x2)
    if(x1.is_integer()):
        x1=x1-1
    x1=math.floor(x1)
        #print(type(x2))
    numberSolution=x1-x2+1
    product*=numberSolution
    print(x1,'**',x2,'***',numberSolution)
    print(product)

fileSample=os.path.join("/home/serve/Python/Advent2023","day6example.txt")
file=os.path.join("/home/serve/Python/Advent2023","inputday6.txt")
runData=openfile(file)

time,distance=parseInput(runData)
compute(time,distance)
#mappings=getMappings(runData)
#finalLocations=mapValues(seeds,mappings)

locationArray=[]
#for location in finalLocations:
#    locationArray.append(location['location'])

#print(min(locationArray))
#print(seeds)
#print(seeds[0])
#seeds[0]['seed']=0
#print(seeds)
#print(mappings)
#x=mapNewValue(79,[[50,98,2],[52,50,48]])
#print(x)
