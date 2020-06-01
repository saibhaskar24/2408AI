
import ai


d = {0:"u",1:"r",2:"d",3:"l"}

def runa(grid):
    # print(grid)
    best = ai.getbestmove(grid,100)
    best['move'] = d[best['move']]
    # print(best)
    return best
    



