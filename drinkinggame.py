# https://www.reddit.com/r/math/comments/408a45/how_many_turns_does_it_take_on_average_until_this/
import random

class Glass:
    def __init__(self):
        self.full = False

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.glasses = createemptyglasses()

    def run(self):
        numturns = 0
        while True:
            num = random.randint(0,len(self.glasses)-1)
            glass = self.glasses[num]
            glass.full = not glass.full
            allfull = True
            for each in self.glasses:
                if not each.full:
                    allfull = False
            numturns += 1
            if allfull == True:
                self.reset()
                return numturns

    def avgturns(self):
        numruns = 0 # set to 0 to reset
        turnsum = 0 # set to 0 to reset
        while True:
            turnsum += self.run()
            numruns += 1
            avg = float(turnsum)/numruns
            if numruns % 10000 == 0:
                print "Avg so far: "+str(avg)+" turns after "+str(numruns)+" runs"

def createemptyglasses(numglasses=6):
    glasses = []
    for x in range(0,numglasses):
        glasses.append(Glass())
    return glasses

print Game().avgturns()
