import numpy as np

def dcalc(y, n, max):
    y = y / 1000 #y von m zu mm
    L = (299 - 69.5) / 100 # abstand in meter
    lam = 632.8e-9
    na = np.arange(-n, n+1)
    d = np.array([])

    if max == True:
        for i in np.arange( len(y) ):
            if na[i] == 0:
                continue
            x = ( (na[i] + 0.5) * lam * L) / y[i]
            d = np.append(d,x)
    else:
        for i in np.arange( len(y) ):
            if na[i] == 0:
                continue
            x = (na[i] * lam * L) / y[i]
            d = np.append(d,x)
    return d;


def aufgabe1():

    return;

def aufgabe2():
    eSp2Max = np.array([-39, -34, -27, -21, -15, -9, 0, 8, 14, 20, 26, 32, 38])
    eSp2Min = np.array([-38, -32, -25, -19, -13, -7, 0, 6, 11, 17, 22, 28, 34])
    eSp2n = 6

    eSp3Max = np.array([-28, -23, -19, -13, -8, 2, 10, 16, 21, 26, 32])
    eSp3Max = eSp3Max - 2
    eSp3Min = np.array([-26, -21, -15, -9, -4, 2, 7, 13, 19, 24, 29])
    eSp3Min = eSp3Min - 2
    eSp3n = 5

    haarMin = np.array([-41, -26, -13, 0, 19, 33, 47])
    haarMin = haarMin -3
    haarMax = np.array([-50, -35, -19, 0, 25, 41, 56])
    haarMax = haarMax -3
    haarn = 3

    dSp2Max = np.mean( dcalc(eSp2Max, eSp2n, 1) )
    dSp2Min = np.mean( dcalc(eSp2Min, eSp2n, 0) )
    dSp2 = np.mean( [dSp2Max, dSp2Min])

    dSp3Max = np.mean( dcalc(eSp3Max, eSp3n, 1) )
    dSp3Min = np.mean( dcalc(eSp3Min, eSp3n, 0) )
    dSp3 = np.mean( [dSp3Max, dSp3Min])

    dhaarMax = np.mean( dcalc(haarMax, haarn, 1) )
    dhaarMin = np.mean( dcalc(haarMin, haarn, 0) )
    dhaar = np.mean( [dhaarMax, dhaarMin])

    print("Spaltbreite 0.2: Max, Min, Mean: ", dSp2Max, dSp2Min, dSp2)
    print("Spaltbreite 0.3: Max, Min, Mean: ", dSp3Max, dSp3Min, dSp3)
    print("Haar: Max, Min, Mean: ", dhaarMax, dhaarMin, dhaar)
    return;

aufgabe1()
