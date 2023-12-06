import re
import os


with open(os.path.join("/home/serve/Downloads","inputday1.txt"),"r") as f:
    data = f.read().strip()

def getnumbers(data):
    lines=data.split("\n")
    numList=[]
    numList2=[]
    for l in lines:
        numLine=re.findall("\d",l)
        l2=(
            l.replace("one","one1one")
            .replace("two","two2two")
            .replace("three","three3three")
            .replace("four","four4four") 
            .replace("five","five5five")
            .replace("six","six6six")
            .replace("seven","seven7seven")
            .replace("eight","eight8eight")
            .replace("nine","nine9nine")
        )
        numLine2=re.findall("\d",l2)
        #print(l," : ",numLines)
        #print(numLine[0],numLine[-1])
        #print(type(numLine[0]))
        num=int(numLine[0]+numLine[-1])
        num2=int(numLine2[0]+numLine2[-1])
        print(l," : ", numLine," : ",num," : ",l2," : ",numLine2," : ",num2)
        numList.append(num)
        numList2.append(num2)
    #print(numList)
    print(sum(numList))
    print(sum(numList2)) 

#data=(     
#    .replace("two","two2two")
#    .replace("three","3")
#    .replace("four","x4") 
#    .replace("five","5")
#    .replace("six","6")
#    .replace("seven","7")
#    .replace("eight","8")
#    .replace("nine","9")
#)

#print(data)
getnumbers(data)
print (os.path.join("/home/serve/Downloads","inputday1.txt"))