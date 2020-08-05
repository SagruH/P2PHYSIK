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
def loadCSV2(name,hlines=1,split=2): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

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

def aufgabe3():
    t,p = loadCSV2("3aDaten.csv")
    p0 = 1000 #mbar
    V = 10.1 #l
    S = -1*np.log(p/p0)*(V/t)
    Sq = np.array(S[8:25])
    Sm = np.mean(Sq)
    print("Mittelwert von S", Sm)

    plt.plot(p,S,"or")
    plt.xscale("log")
    plt.legend()
    plt.xlabel("p in mbar")
    plt.ylabel("S in l/s")
    plt.grid(True)
    plt.show()
    return;

def aufgabe4():
    p,t = loadCSV2("Vakuum_A4.csv")
    p0 = 1000
    V = 10.1
    pln = np.log(p/p0)
    pln = np.array(pln[5:])
    t = np.array(t[5:])
    pf = np.array(pln[:15])
    tf = np.array(t[:15])

    slope, intercept, r_value, p_value, std_err = stats.linregress(tf, pf)
    S = slope*V
    print("S  ", S)

    plt.plot(t,pln,"or")
    plt.plot(tf,slope*tf+intercept,"-b")
    plt.xlabel("t in s")
    plt.ylabel("ln(p/p0)")
    plt.grid(True)
    plt.show()
    return;

def aufgabe5():
    p = np.array([4.3,8.8,13.5,19,24.7,30.9,37.5,45.7,52,63.6,75.2,83.6])
    p = p/1000
    n = np.arange(0,len(p))
    p0 = 1

    slope, intercept, r_value, p_value, std_err = stats.linregress(p, n*p0)
    print("epsilon = ", slope
    )
    plt.plot(p,n*p0,"or")
    plt.plot(p,slope*p+intercept,"-b")
    plt.xlabel("p in bar")
    plt.ylabel("n*p0 in bar")
    plt.grid(True)
    plt.show()
    return;

def aufgabe6():
    p,U = loadCSV2("6aDaten.csv")
    U=U/1000

    plt.plot(p,U,"xr")
    plt.plot(p,U,"-r")
    plt.ylabel("U in kV")
    plt.xlabel("p in mbar")
    plt.xscale("log")
    plt.grid(True)
    plt.show()



    return;














aufgabe6()
