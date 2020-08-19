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

plateuanstieg11()
