import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const

#import kafe
#from kafe.function_tools import FitFunction, LaTeX, ASCII
#from kafe.function_library import quadratic_3par

import uncertainties as uc
from uncertainties.umath import sqrt


def loadCSV(name,hlines=1,split=3): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b,c=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    c = c[0]
    return a,b,c;

def aufgabe2():
    t,p1,p2 = loadCSV("2aDaten.csv")
    print(t,p1,p2)




    return;

aufgabe2()
