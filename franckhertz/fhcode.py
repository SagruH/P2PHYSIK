import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const
from scipy.interpolate import make_interp_spline, BSpline

#import kafe
#from kafe.function_tools import FitFunction, LaTeX, ASCII
#from kafe.function_library import quadratic_3par

import uncertainties as uc
from uncertainties.umath import sqrt

def plot(data,i):
    t  = data[i][0]
    UA = data[i][1]
    U2 = data[i][2]

    tnew = np.linspace(t[0],t[-1],250)
    spl = make_interp_spline(t,UA,k=3)
    UAspl = spl(tnew)
    print(spl)

    HP,TP = minmaxfind(UAspl)
    print(tnew[HP])


    plt.plot(tnew,UAspl,"-b", Label = "fit")
    #plt.plot(t, U2, "-b", label= "U2")
    plt.plot(t, UA, "-r", label= "Franck-Hertz-Kurve")
    plt.legend()
    plt.xlabel("t in s")
    plt.ylabel("U in V")
    plt.grid(True)
    plt.show()
    return;

def spline(data,i):
    return;

def loadCSV3(name,hlines=1,split=2): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b,c=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    c = c[0]
    return a,b,c;

def minmaxfind(a):
    #findet hoch und tiefpunkte, geht davon aus das zuerst ein Hochpunkt kommt
    #kann mit HP /TP im ersten bzw letzten wert nicht richtig umgehen
    HP = np.array([])
    TP = np.array([])
    l = len(a)
    j = a[0]
    HPisNext = 1
    for k in np.arange(1,l):
        i=a[k]
        if HPisNext == 1:
            if j>i:
                HP = np.hstack((HP,k-1))
                HPisNext=0
        elif HPisNext == 0:
            if j<i:
                TP = np.hstack((TP,k-1))
                HPisNext=1
        j=a[k]
    HP=np.int_(HP)
    TP=np.int_(TP)
    return HP,TP;

def aufgabe1_2():
    #load parameters aufgabe 1.2
    #Temp in °C, U1 in V, U3 in V, Uf in V
    hlines, data = ppk.readCSV("Aufgabe1.csv",1)
    #load data
    #t,UA,U2
    hlines, d160 = ppk.readCSV("12aufgabe_160.csv",3)
    hlines, d150 = ppk.readCSV("12aufgabe_150.csv",3)
    hlines, d140 = ppk.readCSV("12aufgabe_140.csv",3)
    hlines, d120 = ppk.readCSV("12aufgabe_120.csv",3)
    dcsv = [d160,d150,d140,d120]


    HP,TP = minmaxfind(dcsv[0][1])
    plot(dcsv,0)


    return;


aufgabe1_2()
