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

    print(p1,p2,alpha1,alpha,tmin)
    return;

def kappa(h1,h2):
    return (h1/(h1-h2))

def aufgabe2():
    #immer linke Messwerte
    #richtig
    h1r = uc.ufloat(27.7,0.05) - uc.ufloat(10.4,0.05)
    h2r = uc.ufloat(21.2,0.05) - uc.ufloat(17.0,0.05)
    #langsam
    h1l = uc.ufloat(26.2,0.05) - uc.ufloat(12.0,0.05)
    h2l = uc.ufloat(20.7,0.05) - uc.ufloat(17.6,0.05)
    #unvollständig
    h1u = uc.ufloat(28.4,0.05) - uc.ufloat(9.7,0.05)
    h2u = uc.ufloat(23.7,0.05) - uc.ufloat(14.7,0.05)

    kr = kappa(h1r,h2r)
    kl = kappa(h1l,h2l)
    ku = kappa(h1u,h2u)

    print(kr,kl,ku)

    return;

def aufgabe3():
    n = 5
    T = np.array([5.69, 5.68, 5.62, 5.55, 5.34]) / n
    mK = uc.ufloat(16.68,(16.68*0.001)) / 1000
    At = np.pi*(16e-3/2)**2
    A = uc.ufloat(At,(0.005*At))
    pRaum = uc.ufloat(996,0.5) * 100 #pa
    V = uc.ufloat(10.58,(10.58*0.005)) /1000

    Tm = np.mean(T)
    Tstd = np.sqrt(np.var(T))
    T = uc.ufloat(Tm,Tstd)

    k1 = ( (2*np.pi)**2 ) / ( T**2 )
    k2 = (mK*V) / (pRaum * A**2)
    kappa = k1*k2
    print(kappa)

    return;

def aufgabe4():
    T, h = loadCSV("aufgabe4gase.csv",1)
    TRaum = 25.4
    Toffset = -273.15
    hRr = 21.93
    hRl = 36.15



    return;

aufgabe4()
