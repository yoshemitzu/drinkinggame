# https://www.reddit.com/r/math/comments/408a45/how_many_turns_does_it_take_on_average_until_this/
import random

def sliceStringByNeedles(string,sneedle,eneedle):
    start = string.rfind(sneedle)+len(sneedle)
    return string[start:string.find(eneedle,start)]

def getScriptName(withpath=False):
    import sys
    scriptpath = sys.argv[0]
    scriptname = sliceStringByNeedles(scriptpath,"\\",".")
    if withpath:
        end = len(scriptpath)-len(scriptname)-len(".py")
        scriptname = scriptpath.replace(scriptname,'')[0:end]+scriptname
    return scriptname

class Data:
    def __init__(self,path=None):
        import os
        if path == None:
            path = getScriptName()+"_data.txt"
        self.path = path
    def read(self):
        import os
        if os.path.exists(self.path):
            f = open(self.path,"r")
            data = f.read()
            f.close()
        else:
            data = ""
            self._write(data)
            print "File did not exist."
        return data
    def clear(self):
        self._write("")
    def _write(self,data):
        f = open(self.path,"w")
        f.write(data)
        f.close()
    def write(self,data):
        olddata = self.read()
        self._write(olddata+data)
        
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
        avgdata = Data("drinkinggame_data.txt")
        lines = avgdata.read().split("\n")
        numruns = len(lines)-1
        
        turnsumdata = Data("turnsum.txt")
        if numruns != 0:
            turnsum = int(turnsumdata.read())
        else:
            turnsum = 0
        runs = ""
        while True:
            turnsum += self.run()
            numruns += 1
            avg = float(turnsum)/numruns
            runs += str(avg)+"\n"
            if numruns % 10000 == 0:
                print "Avg so far: "+str(avg)+" turns after "+str(numruns)+" runs"
                avgdata.write(runs)
                runs = ""
                turnsumdata.clear()
                turnsumdata.write(str(turnsum))

def createemptyglasses(numglasses=6):
    glasses = []
    for x in range(0,numglasses):
        glasses.append(Glass())
    return glasses

print Game().avgturns()
