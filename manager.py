
import ai


d = {0:"u",1:"r",2:"d",3:"l"}

def runa(grid,runs = 100):
    # print(grid)
    best = ai.getbestmove(grid,runs)
    best['move'] = d[best['move']]
    # print(best)
    return best
    



