import re
import os

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

def isSymbol(testChr):
    #return not testChr.isdigit() and testChr!='.' and testChr!='X'
    return testChr=='*'

def printGrid(bData):
    for line in bData:
        print(line)

def findNumber(bData,row,col):
    number=bData[row][col]
    bData[row][col]='X'
    i=col+1
    k=col-1
    while bData[row][i].isdigit():
        number=number+bData[row][i]
        bData[row][i]='X'
        i+=1
    while bData[row][k].isdigit():
        number=bData[row][k]+number
        bData[row][k]='X'
        k=k-1
    #print(number)    
    return bData,int(number)

def findNumbers(bData):
    numbers=[]
    lenList=len(bData)
    lenLine=len(bData[0])
    for row in range(1,lenList-1):
        for col in range(1,lenLine-1):
            number=0
            tempNumber=[]
            if isSymbol(bData[row][col]):
                if bData[row-1][col-1].isdigit():
                    bData,number=findNumber(bData,row-1,col-1)
                    tempNumber.append(number)
                    #bData[row-1][col-1]='X'
                if bData[row-1][col].isdigit():
                    bData,number=findNumber(bData,row-1,col)
                    tempNumber.append(number)
                    # bData[row-1][col]='X'
                if bData[row-1][col+1].isdigit():
                    bData,number=findNumber(bData,row-1,col+1)
                    tempNumber.append(number)
                    #bData[row-1][col+1]='X'
                if bData[row][col-1].isdigit():
                    bData,number=findNumber(bData,row,col-1)
                    tempNumber.append(number)
                    #bData[row][col-1]='X'
                if bData[row][col+1].isdigit():
                    bData,number=findNumber(bData,row,col+1)
                    tempNumber.append(number)
                    #bData[row][col+1]='X'
                if bData[row+1][col-1].isdigit():
                    bData,number=findNumber(bData,row+1,col-1)
                    tempNumber.append(number)
                    #bData[row+1][col-1]='X'
                if bData[row+1][col].isdigit():
                    bData,number=findNumber(bData,row+1,col)
                    tempNumber.append(number)
                    #bData[row+1][col]='X'
                if bData[row+1][col+1].isdigit():
                    bData,number=findNumber(bData,row+1,col+1)
                    tempNumber.append(number)
                    #bData[row+1][col+1]='X'
            if len(tempNumber)==2:
                numbers.append(tempNumber[0]*tempNumber[1])   
            #bData[x][y]=bData[x][y]+'.'
    print(numbers)
    print(sum(numbers))
    return bData






fileTest=os.path.join("/home/serve/Downloads","day3example.txt")
file=os.path.join("/home/serve/Downloads","inputday3.txt")

data=openfile(file)
bData=bufferData(data)
print(data)
printGrid(bData)
endData=findNumbers(bData)
print('END DATA')
printGrid(endData)