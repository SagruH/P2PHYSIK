import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const
from scipy.interpolate import make_interp_spline, BSpline

def plateuanstieg11():
    hlines, data = ppk.readCSV("11aufgabe.csv",2)

    NpT = data[2]/ data[0]
    U = data[1]

    NpTPB = NpT[5:]
    UPB = U[5:]
    slope, intercept, r_value, p_value, std_err = stats.linregress(UPB, NpTPB)
    print("P-Anstieg", slope, " +- ", std_err)
    plt.plot(U, NpT, "xb")
    plt.plot(UPB, intercept + slope*UPB, "-b")
    plt.xlabel("Zählrate N/T")
    plt.ylabel("U in V")
    plt.grid(True)
    plt.show()
    return;

def nulleffekt12():
    hlines, data = ppk.readCSV("Nulleffekt2.csv",2)
    N = np.arange( len(data[1]) )
    for i in np.arange( len(data[1])-1 ):
        N[i+1] = data[1][i+1] - data[1][i]

    Nt = N/5

    NUm = np.mean(Nt)
    NUs = np.std(Nt)
    print(NUm, NUs)

    return;

def totzeit13():
    T = 180
    N12 = 18088
    N1 = 10042
    N2 = 7988

    tau = (T/N12)*(1- np.sqrt(1- ( ((N1+N2-N12)/(N1*N2))*N12 ) ) )
    print(tau)
    return;

def abstand():
    hlines, data = ppk.readCSV("14aufgabe.csv",2)
    d = data[0]
    lN = np.log10(data[1])
    rlN = lN[:15]
    rd = d[:15]

    slope, intercept, r_value, p_value, std_err = stats.linregress(rd, rlN)
    print(slope)

    plt.plot(d, lN, "xb")
    plt.plot(rd, intercept + slope*rd, "-b")
    plt.xlabel("d in cm")
    plt.ylabel("log(N)")
    plt.grid(True)
    plt.show()
    return;

def alpha():
    hlines, data = ppk.readCSV("alpha.csv",1)
    d = data[0] + 2 + 7 + 1
    Ruk = data[1]/200
    R0 = 0.224
    tau = 0.001
    r = 0.0045

    Rost = ( Ruk/(1-Ruk*tau) ) - R0
    R = Rost*( (4*(d**2))/(r**2) )

    plt.plot(d, Rost, "xb")
    plt.xlabel("d in mm")
    plt.ylabel("Korrigierte Zählrate")
    plt.grid(True)
    plt.show()
    plt.clf()

    plt.plot(d, R, "xb")
    plt.xlabel("d in mm")
    plt.ylabel("Korrigierte Zählrate")
    plt.grid(True)
    plt.show()
    return;

def beta():
    hlines, data = ppk.readCSV("beta.csv",1)
    d = data[0]*1e-6
    R0 = 0.224
    tau = 0.001
    rho = 2.71 *1000

    Ruk = data[1]/data[2]
    R = ( Ruk/(1-Ruk*tau) ) - R0
    R = np.log(R)

    slp1, int1, r_value, p_value, std_err = stats.linregress(d[:7], R[:7])
    slp2, int2, r_value, p_value, std_err = stats.linregress(d[7:16], R[7:16])
    polc1 = np.array([slp1,int1])
    polc2 = np.array([slp2,int2])
    polcR0 = np.array([0,R0])

    RY = np.roots(polc2-polcR0)
    RSr = np.roots(polc1-polc2)

    mySrY = slp1
    mySr = slp1 -slp2
    myY = slp2

    cSr = mySr / rho
    cY = myY / rho

    WSr = 1.92*np.sqrt((RSr**2 * rho**2) + (0.22*RSr*rho) )
    WY = 1.92*np.sqrt((RY**2 * rho**2) + (0.22*RY*rho) )

    cSr2 = 17*WSr**(-1.43)
    cY2 = 17*WY**(-1.43)

    print("Reichweite Sr, Y: ", RSr, RY)
    print("absorptions my Sr+Y, Sr, Y: ", mySrY, mySr, myY)
    print("massenabsorb c Sr, Y: " , cSr, cY)
    print("Flammersfeld W Sr, Y: ", WSr, WY)
    print("letztes c Sr, Y: ", cSr2, cY2)

    plt.plot(d[:-2], R[:-2], "xb")
    plt.plot(d[:7], slp1*d[:7]+int1, "-g")
    plt.plot(d[7:16], slp2*d[7:16]+int2, "-r")
    plt.xlabel("d in micrometer")
    plt.ylabel("Korrigierte Zählrate")
    plt.grid(True)
    #plt.show()

    return;




beta()
