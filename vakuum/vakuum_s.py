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
    p0 = 1000 #mbar
    V = 10.1 #l
    l = 0.51 #m
    d = 0.002 #m
    xw = np.linspace(0,420,1000)

    p1ln = np.log(p1/p0)
    p2ln = np.log(p2/p0)
    p1n = np.array(p1ln[1:15])
    p2n = np.array(p2ln[15:23])
    t1n = np.array(t[1:15])
    t2n = np.array(t[15:23])

    slope1, intercept1, r_value, p_value, std_err = stats.linregress(t1n, p1n)
    slope2, intercept2, r_value, p_value, std_err = stats.linregress(t2n, p2n)
    S1 = -V*slope1
    S2 = -V*slope2
    L = 1/ ( (1/S2) - (1/S1) )
    print("S1 = ",S1)
    print("S2 = ",S2)
    print("L = ",L)

    plt.plot(t,p1ln,"or",label="P1")
    plt.plot(t1n,slope1*t1n+intercept1,"-b")
    plt.plot(t,p2ln,"og",label="P2")
    plt.plot(t2n,slope2*t2n+intercept2,"-c")
    plt.legend()
    plt.xlabel("t in s")
    plt.ylabel("-ln(p/p0)")
    plt.grid(True)
    plt.show()

    return;

aufgabe2()
