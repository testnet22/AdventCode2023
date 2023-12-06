import re
import os


with open(os.path.join("/home/serve/Downloads","inputday2.txt"),"r") as f:
    data = f.read().strip()

def testGames(data):
    games=data.split('\n')
    sum1=0
    sum2=0
    for game in games:
        gameMax={
            'red':0,
            'green':0,
            'blue':0
        }
        gameNum,draws=game.split(':')
        gameNum=int(gameNum.split(" ")[1])
        print(gameNum)
        print(draws)
        for draw in draws.split(';'):
            #print(draw)
            for balls in draw.split(','):
                numBalls,color = balls.split()
                #numBalls=numBalls.strip()
                #color=color.strip()
                #print(color,":",numBalls,":")
                gameMax[color]=max(int(numBalls),gameMax[color])
        print(gameMax)
        if(gameMax['red']<=12 and gameMax['green']<=13 and gameMax['blue']<=14):
            print("game ",gameNum," is possible")
            sum1+=gameNum
        sum2+=gameMax['red']*gameMax['green']*gameMax['blue']
    print("sum possible games ",sum1)
    print("part duo ", sum2)
        




testGames(data)
