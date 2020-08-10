import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const

import uncertainties as uc
from uncertainties.umath import sqrt

def loadCSV(name,hlines=2,split=2): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def aufgabe1():
    pRaum = uc.ufloat(996,0.5) * 100 #pa
    #Delta der zwei Messwerte
    h1 = uc.ufloat(-4,0.05) / 100 #m
    h2 = uc.ufloat(21.1,0.05) / 100 #m
    g = 9.81
    rhoHG = 13546
    gamma = 2.5e-5

    t1 = uc.ufloat(0,0.5)
    t2 = uc.ufloat(99.5,0.5)

    #druck = Raumdruck +Delta p
    p1 = pRaum + g*rhoHG*h1
    p2 = pRaum + g*rhoHG*h2

    alpha1 = (p2 - p1)/(p1*t2-p2*t1)
    alpha = alpha1 + (p2/p1)*gamma
    tmin = -1/alpha

    print(tmin)




    return;

aufgabe1()
