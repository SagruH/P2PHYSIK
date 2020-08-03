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


def loadCSV(name,hlines=1,split=2): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def plot(data):  # alle zeilen zum ploten von daten
    plt.plot(data[0],data[1],label="test")
    plt.legend()
    plt.title("Messdaten")
    plt.xlabel("h in cm")
    plt.ylabel("t in s")
    plt.grid(True)
    plt.show()
    return;

def lineareRegression(x,y):
    return slope, intercept, r_value, p_value, std_err = stats.linregress(x, y);

'''
fehler rechung mit uncertainties
variable = uc.float(wert, fehler)
'''


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

def num_int_calc(d, S): #numerisches Integrieren noch ziemlcih buggy
    a = np.linspace(d,S,10000)
    da = a[100]-a[99]
    lamda = np.array([])
    Integral= 0
    for i in a:
        y = lamdafunc(i) #name der funktion unter der integriert wird
        lamda = np.hstack((lamda,y))

    for j in np.arange(len(lamda)):
        if j>0:
            Integral = Integral + (lamda[j-1]*da) + (lamda[j]-lamda[j-1])*da*1/2

    lamdaq = (1/(S-d))*Integral
    return lamdaq;
