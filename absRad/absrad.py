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
    plt.xlabel("log(d) in log(cm)")
    plt.ylabel("log(N)")
    plt.grid(True)
    plt.show()
    return;

abstand()
