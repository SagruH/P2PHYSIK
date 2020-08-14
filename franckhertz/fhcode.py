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

UK = 2.57   #V

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

def plot(splines, i):
    IAspl = splines[2*i]
    U2 = splines[2*i+1]
    IA = IAspl(U2)

    plt.plot(U2, IA, "-r", label= "Franck-Hertz-Kurve")
    plt.legend()
    plt.xlabel("Beschleunigungsspannung U2 in V")
    plt.ylabel("Annodenstrom IA in nA")
    plt.grid(True)
    plt.show()
    return;

def spline_it(data,n):
    splx = np.array([])
    for i in np.arange(n):
        t  = data[i][0]
        IA = data[i][1]
        U2 = data[i][2]

        U2new = np.linspace(U2[0],U2[-1],100)
        spl = make_interp_spline(U2,IA,k=5)

        pair = np.array([spl,U2new])
        splx = np.hstack((splx,pair))

    return splx;



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

    splx = spline_it(dcsv,4)

    HP160, TP = minmaxfind( splx[0]( splx[1] ) )
    HP150, TP = minmaxfind( splx[2]( splx[3] ) )
    HP140, TP = minmaxfind( splx[4]( splx[5] ) )
    HP120, TP = minmaxfind( splx[6]( splx[7] ) )

    #korrekturen
    HP140 = np.delete(HP140,0)
    HP120 = np.delete(HP120, [0,1,2])
    HP = [HP160, HP150, HP140, HP120]

    #berechungen
    i = 0
    UKm = np.array([])
    while i < 4:
        U1 = data[1][i]
        U2 = splx[2*i+1]
        peaks = HP[i]
        pc = len(peaks)

        UDach = U2[peaks[0]] + U1
        DeltaU = np.array([])

        for j in np.arange(1,pc-1):
            temp = U2[peaks[j]] - U2[peaks[j-1]]
            DeltaU = np.hstack((DeltaU, temp))
        DUm = np.mean(DeltaU)
        UK = UDach - DUm
        UKm = np.hstack((UKm, UK))
        print(i, DUm, UK, "\n")
        i += 1
        pass
    UKm = np.mean(UKm)
    print(UKm)
    '''
    for i in np.arange(4):
        plot(splx,i)
    '''
    return;

def aufgabe1_3():
    U1 = 2.3    #V
    Uf = 6.0    #V
    U3 = 0.91   #V
    T  = 150     #°C
    #U2 in V, Ig2 in myA
    hlines, data = ppk.readCSV("Aufgabe1_3.csv",2)
    data[0] = data[0]**(3/2)

    slope, intercept, r_value, p_value, std_err = stats.linregress(data[0][:15], data[1][:15]);
    print(slope)

    plt.plot(data[0],data[1],"ob")
    plt.plot(data[0][:15], slope*data[0][:15] + intercept, "-r")
    plt.xlabel("Spannung U2^(3/2) in V^(3/2)")
    plt.ylabel("Anodenstrom I in \u039CA")
    plt.grid(True)
    plt.show()
    return;

def aufgabe1_4a():
    U1 = 2.3    #V
    Uf = 6.0    #V
    U3 = 0.91   #V
    T  = 120     #°C
    #U2 in V, Ig2 in A
    hlines, data = ppk.readCSV("Aufgabe1_4a.csv",2)
    data[0] = data[0] - UK

    slb, intb, r, p, std = stats.linregress(data[0][:6], data[1][:6]);
    slr, intr, r, p, std = stats.linregress(data[0][6:12], data[1][6:12]);

    pb = np.poly1d([slb,intb])
    pr = np.poly1d([slr,intr])
    xb = np.linspace(-3,12,50)
    xr = np.linspace(8,20,50)

    x0 = np.roots((pb-pr))
    print(x0)

    plt.plot(data[0][0:6],data[1][0:6],"ob")
    plt.plot(xb,pb(xb),"-b")

    plt.plot(data[0][6:12],data[1][6:12],"or")
    plt.plot(xr,pr(xr),"-r")

    plt.plot(x0,pb(x0),"xk")
    plt.plot(data[0][12:],data[1][12:],"og")

    plt.xlabel("U2 in V")
    plt.ylabel("Anodenstrom I in A")
    plt.grid(True)
    plt.show()
    return;

def aufgabe1_4b():
    #t,UA,U2
    hlines, data = ppk.readCSV("14baufgabe.csv",3)
    data[2] = data[2] - UK

    plt.plot(data[2], data[1], "-r")
    plt.xlabel("U2 in V")
    plt.ylabel("UA in V")
    plt.grid(True)
    plt.show()
    return;

def aufgabe2():
    #t,UA,U2
    hlines, data = ppk.readCSV("2aufgabe.csv",3)
    data[2] = data[2] - UK + 0.5
    U2 = data[2]
    UA = data[1]

    U2new = np.linspace(U2[0],U2[-1],100)
    spl = make_interp_spline(U2,UA,k=5)

    HP,TP = minmaxfind(spl(U2new))
    HP = np.delete(HP,[0,1,2,3])
    print(U2new[HP])

    for i in HP:
        plt.axvline( U2new[i], 0, 12 )
    plt.plot(U2new, spl(U2new), "-r")
    plt.xlabel("U2 in V")
    plt.ylabel("UA in V")
    plt.grid(True)
    plt.show()

    return;

aufgabe2()
