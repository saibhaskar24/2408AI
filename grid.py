import random
import manager
import time


myArray = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
inducerlist = [0,1,2,3]
myArray[random.choice(inducerlist)][random.choice(inducerlist)]=2
def move(user_input):
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
                myArray[i][j]=myArray[i][j]+myArray[i+1][j]
                myArray[i+1][j]=myArray[i+2][j]
                myArray[i+2][j]=myArray[i+3][j]
                myArray[i+3][j]=0
            if myArray[i+1][j]==myArray[i+2][j]:
                myArray[i+1][j]=myArray[i+1][j]+myArray[i+2][j]
                myArray[i+2][j]=myArray[i+3][j]
                myArray[i+3][j]=0
            if myArray[i+2][j]==myArray[i+3][j]:
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
                myArray[i+3][j]=myArray[i+3][j] + myArray[i+2][j]
                myArray[i+2][j]=myArray[i+1][j]
                myArray[i+1][j]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i+2][j]==myArray[i+1][j]:
                myArray[i+2][j]=myArray[i+2][j]+myArray[i+1][j]
                myArray[i+1][j]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i+1][j]==myArray[i][j]:
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
                myArray[i][j]=myArray[i][j]+myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+3]
                myArray[i][j+3]=0
            if myArray[i][j+1]==myArray[i][j+2]:
                myArray[i][j+1]=myArray[i][j+1]+myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+3]
                myArray[i][j+3]=0
            if myArray[i][j+2]==myArray[i][j+3]:
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
                myArray[i][j+3]=myArray[i][j+3] + myArray[i][j+2]
                myArray[i][j+2]=myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i][j+2]==myArray[i][j+1]:
                myArray[i][j+2]=myArray[i][j+2]+myArray[i][j+1]
                myArray[i][j+1]=myArray[i][j]
                myArray[i][j]=0
            if myArray[i][j+1]==myArray[i][j]:
                myArray[i][j+1]=myArray[i][j+1]+myArray[i][j]
                myArray[i][j]=0
                
                

def randomAvailableCell(myArray):
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

def printgrid():
    for i in range(4):
        for j in range(4):
            print(myArray[i][j],end="\t")
        print()

def reachedmax():
    for i in range(4):
        for j in range(4):
            if myArray[i][j] > 2000:
                return True
    return False


tstart = time.time()
counter = 0
moveno = 0
try:
    while True:
        aialgo = manager.runa(myArray)
        # user_input = input("u for upward direction, d for downwards, l for left and r for Right : ")
        user_input = aialgo['move']
        move(user_input)
        pos = randomAvailableCell(myArray)
        if pos == -1:
            break
        else:
            myArray[pos[0]][pos[1]] = 2
        if reachedmax():
            printgrid()
            break
        counter+=1
        moveno+=1
        if counter == 100:
            printgrid()
            print("Moves",moveno)
            counter = 0
        moveno+=1
except :
    printgrid()

tend = time.time()
print("Total Moves",moveno)
print ("Game over")
print("Times taken : " ,tend - tstart ) 
