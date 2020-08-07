import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const

def loadCSV(name,hlines=2,split=2): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def polplots(phi,r):
    phi2 = phi+180
    phi = np.hstack((phi,phi2))
    r = np.hstack((r,r))
    plt.polar((phi/360)*2*np.pi,r,"ob")
    #plt.xlabel("h in cm")
    #plt.ylabel("t in s")
    plt.grid(True)
    plt.show()

    return;

def main():
    almFF, ulmFF = loadCSV("datenlinmFF.csv")
    aloFF, uloFF = loadCSV("datenlinoFF.csv")
    acir, ucir = loadCSV("datenCir.csv")
    ae50, ue50 = loadCSV("datenelip50.csv")
    ae60, ue60 = loadCSV("datenelip60.csv")

    lam = 632.5 * 10**(-9)
    d1 = 47.5 * 10 **(-6)
    d2 = 60 * 10 **(-6)

    T1 = 0.01
    T2 = 0.22
    L1 = 1.41
    L2 = 2.8

    n1 = (lam/(np.pi*d1))*np.arctan(np.sqrt(L1/T1))
    n2 = (lam/(np.pi*d2))*np.arctan(np.sqrt(L2/T2))

    print(n1, n2)

    angel = np.array([almFF,aloFF,acir,ae50,ae60])
    volt = np.array([ulmFF,uloFF,ucir,ue50,ue60])
    #for x in [0,1,2,3,4]: plots
        #polplots(angel[x],volt[x])
    return;

main()
