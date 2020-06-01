
import random
from copy import deepcopy


def availableCell(myArray):
    listfori = []
    listforj = []
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            if myArray[i][j]==0:
                count+=1
                listfori.append(i)
                listforj.append(j)
    if count > 0:
        if count > 1:
            randomindex = listfori.index(random.choice(listfori))
            return (listfori[randomindex],listforj[randomindex])
        else:
            return (listfori[0],listforj[0])
    else:
        return -1


def addRandomData(grid):
    cord = availableCell(grid)
    if cord != -1:
        grid[cord[0]][cord[1]] = 2


def movesavilable(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return True

d = {0:"u",1:"r",2:"d",3:"l"}

def move(user_input,myArray):
    moved = False
    grid = deepcopy(myArray)
    score = 0
    user_input = d[user_input]
    # print(user_input)
    if user_input == "u":
        i=0
        for j in range(0,4):
            if myArray[i][j]!=0 or myArray[i+1][j]!=0 or myArray[i+2][j]!=0 or myArray[i+3][j]!=0:
                if myArray[i][j]==0:
                    while myArray[i][j]==0:
                        myArray[i][j]=myArray[i+1][j]
                        myArray[i+1][j]=myArray[i+2][j]
                        myArray[i+2][j] = myArray[i+3][j]
                        myArray[i+3][j]=0
                if myArray[i+1][j]==0 and (myArray[i+2][j]!=0 or myArray[i+3][j]!=0):
                    while myArray[i+1][j]==0:
                        
                        myArray[i+1][j]=myArray[i+2][j]
                        myArray[i+2][j]=myArray[i+3][j]
                        myArray[i+3][j]=0
                if myArray[i+2][j]==0 and (myArray[i+3][j]!=0):
                    while myArray[i+2][j]==0:
                        myArray[i+2][j]=myArray[i+3][j]
                        myArray[i+3][j]=0
        i=0
        for j in range(0,4):
            if myArray[i][j]==myArray[i+1][j]:
                score+=myArray[i][j]*2
                myArray[i][j]=myArray[i][j]+myArray[i+1][j]
                myArray[i+1][j]=myArray[i+2][j]
                myArray[i+2][j]=myArray[i+3][j]
                myArray[i+3][j]=0
            if myArray[i+1][j]==myArray[i+2][j]:
                score+=myArray[i+1][j]*2
                myArray[i+1][j]=myArray[i+1][j]+myArray[i+2][j]
                myArray[i+2][j]=myArray[i+3][j]
                myArray[i+3][j]=0
            if myArray[i+2][j]==myArray[i+3][j]:
                score+=myArray[i+2][j]*2
                myArray[i+2][j]=myArray[i+2][j]+myArray[i+3][j]
                myArray[i+3][j]=0
    elif user_input == "d":
        i=0
        for j in range(0,4):
            if myArray[i][j]!=0 or myArray[i+1][j]!=0 or myArray[i+2][j]!=0 or myArray[i+3][j]!=0:
                if myArray[i+3][j]==0:
                    while myArray[i+3][j]==0:
                        myArray[i+3][j]=myArray[i+2][j]
                        myArray[i+2][j]=myArray[i+1][j]
                        myArray[i+1][j]=myArray[i][j]
                        myArray[i][j]=0
                if myArray[i+2][j]==0 and (myArray[i+1][j]!=0 or myArray[i][j]!=0):
                    while myArray[i+2][j]==0:
                        myArray[i+2][j]=myArray[i+1][j]
                        myArray[i+1][j]=myArray[i][j]
                        myArray[i][j]=0

                if myArray[i+1][j]==0 and myArray[i][j]!=0:
                    while myArray[i+1][j]==0:
                        myArray[i+1][j]=myArray[i][j]
                        myArray[i][j]=0
        i=0
        for j in range(0,4):
            if myArray[i+3][j]==myArray[i+2][j]:
                score+=myArray[i+3][j]*2
                myArray[i+3][j]=myArray[i+3][j] + myArray[i+2][j]
                myArray[i+2][j]=myArray[i+1][j]
                myArray[i+1][j]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i+2][j]==myArray[i+1][j]:
                score+=myArray[i+2][j]*2
                myArray[i+2][j]=myArray[i+2][j]+myArray[i+1][j]
                myArray[i+1][j]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i+1][j]==myArray[i][j]:
                score+=myArray[i+1][j]*2
                myArray[i+1][j]=myArray[i+1][j]+myArray[i][j]
                myArray[i][j]=0
    elif user_input == "l":
        j=0
        for i in range(0,4):

            if myArray[i][j]!=0 or myArray[i][j+1]!=0 or myArray[i][j+2]!=0 or myArray[i][j+3]!=0:
                if myArray[i][j]==0:
                    while myArray[i][j]==0:
                        myArray[i][j]=myArray[i][j+1]
                        myArray[i][j+1]=myArray[i][j+2]
                        myArray[i][j+2] = myArray[i][j+3]
                        myArray[i][j+3]=0
                if myArray[i][j+1]==0 and (myArray[i][j+2]!=0 or myArray[i][j+3]!=0):
                    while myArray[i][j+1]==0:
                        myArray[i][j+1]=myArray[i][j+2]
                        myArray[i][j+2]=myArray[i][j+3]
                        myArray[i][j+3]=0
                if myArray[i][j+2]==0 and (myArray[i][j+3]!=0):
                    while myArray[i][j+2]==0:
                        myArray[i][j+2]=myArray[i][j+3]
                        myArray[i][j+3]=0
        j=0
        for i in range(0,4):
            if myArray[i][j]==myArray[i][j+1]:
                score+=myArray[i][j]*2
                myArray[i][j]=myArray[i][j]+myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+3]
                myArray[i][j+3]=0
            if myArray[i][j+1]==myArray[i][j+2]:
                score+=myArray[i][j+1]*2
                myArray[i][j+1]=myArray[i][j+1]+myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+3]
                myArray[i][j+3]=0
            if myArray[i][j+2]==myArray[i][j+3]:
                score+=myArray[i][j+2]*2
                myArray[i][j+2]=myArray[i][j+2]+myArray[i][j+3]
                myArray[i][j+3]=0
    elif user_input == "r":
        j=0
        for i in range(0,4):
            if myArray[i][j]!=0 or myArray[i][j+1]!=0 or myArray[i][j+2]!=0 or myArray[i][j+3]!=0:
                if myArray[i][j+3]==0:
                    while myArray[i][j+3]==0:
                        myArray[i][j+3]=myArray[i][j+2]
                        myArray[i][j+2]=myArray[i][j+1]
                        myArray[i][j+1]=myArray[i][j]
                        myArray[i][j]=0
                if myArray[i][j+2]==0 and (myArray[i][j+1]!=0 or myArray[i][j]!=0):
                    while myArray[i][j+2]==0:
                        myArray[i][j+2]=myArray[i][j+1]
                        myArray[i][j+1]=myArray[i][j]
                        myArray[i][j]=0

                if myArray[i][j+1]==0 and myArray[i][j]!=0:
                    while myArray[i][j+1]==0:
                        myArray[i][j+1]=myArray[i][j]
                        myArray[i][j]=0
        j=0
        for i in range(0,4):
            if myArray[i][j+3]==myArray[i][j+2]:
                score+=myArray[i][j+2]*2
                myArray[i][j+3]=myArray[i][j+3] + myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i][j+2]==myArray[i][j+1]:
                score+=myArray[i][j+1]*2
                myArray[i][j+2]=myArray[i][j+2]+myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i][j+1]==myArray[i][j]:
                score+=myArray[i][j+1]*2
                myArray[i][j+1]=myArray[i][j+1]+myArray[i][j]
                myArray[i][j]=0

    if myArray != grid:
        moved = True
    dic = {'moved':moved,"score":score}
    return dic