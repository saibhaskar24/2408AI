from copy import deepcopy

import  random , helper

def getbestmove(grid,runs):
    bestscore = 0
    bestmove = -1
    for i in range(4):
        res = multiplerandom(grid,i,runs)
        score = res['score']
        if score >= bestscore:
            bestscore = score
            bestmove = i
            bestmoveavg = res['avgmoves']

    return {'move':bestmove,'score':bestscore,'bestmoveavg':bestmoveavg}


def multiplerandom(grid,move,runs):
    total = 0
    min = int(10e5)
    max = 0
    totalmove = 0
    for i in range(runs):
        res= randRuns(grid,move)
        if res == -1:
            continue
        s = res['score']
        if s==-1:
            break
        total+=s
        totalmove+=res['moves']
        if s<min:
            min=s
        if s>max:
            max=s
    res = {'score':total/runs,'avgmoves':totalmove/runs}
    return res

def randRuns(grid,move):
    g = deepcopy(grid)
    score = 0
    res = moveandaddrandtiles(g,move)
    if (not res['moved']):
        return -1
    score+=res['score']
    moves  = 1
    while True:
        if (not helper.movesavilable(g)):
            break
        l = [0,1,2,3]
        res = helper.move(random.choice(l),g)
        if not res['moved']:
            continue
        score+=res['score']
        helper.addRandomData(g)
        moves+=1
    return {'moves':moves, 'score':score}

def moveandaddrandtiles(grid , dir):
    res = helper.move(dir,grid)
    if res['moved']:
        helper.addRandomData(grid)
    return res