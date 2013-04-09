import random
import math
#import scipy
#import matplotlib.pyplot as plt
#import pylab
from sys import argv
script, ICPC, ML, SL, SC = argv

def generateSeq(SL):
    sequence = ''
    for i in range(SL):
        r = random.random()
        if r < 0.25:
            sequence += 'A'
        elif r < 0.5:
            sequence += 'C'
        elif r < 0.75:
            sequence += 'G'
        else:
            sequence += 'T'
    return(sequence)

def checkICPC(Wa,Wc,Wg,Wt):
    return(Wa*(math.log(Wa)+math.log(4))+Wc*(math.log(Wc)+math.log(4))+Wc*(math.log(Wc)+math.log(4))+Wt*(math.log(Wt)+math.log(4)))


def generateICweights(ICPC):
    s = 2 - ICPC
    p2 = random.uniform(0,s)
    p1 = random.uniform(0,p2)
    p3 = random.uniform(p2,s)
    return([p1, p2 - p1, p3 - p2, s - p3])

def generatePWcolumn(ICPC):
    weights = generateICweights(ICPC)
    w1=0.15
    w2=0.25
    w3=0.2
    w4=0.4
    return([w1, w2, w3, w4])





print(generateSeq(int(SL)))

#x = range(20)
#y = range(20)
#plt.plot(x, y)
#pylab.show()