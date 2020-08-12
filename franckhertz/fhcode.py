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

def loadCSV3(name,hlines=1,split=2): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b,c=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    c = c[0]
    return a,b,c;

def loadCSV4(name,hlines=1,split=4): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b,c,d=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    c = c[0]
    d = d[0]
    return a,b,c,d;

def aufgabe1_2():
    #load parameters aufgabe 1.2
    #Temp in °C, U1 in V, U3 in V, Uf in V
    hlines, data = ppk.readCSV("Aufgabe1.csv",1)
    #load data
    #t,UA,U2
    hlines, d160 = ppk.readCSV("12aufgabe_120.csv",3)
    plt.plot(d160[0], d160[2], "-b", label= "U2")
    plt.plot(d160[0], d160[1], "-r", label= "Franck-Hertz-Kurve")
    plt.legend()
    plt.xlabel("t in s")
    plt.ylabel("U in V")
    plt.grid(True)
    plt.show()

    return;


aufgabe1_2()
