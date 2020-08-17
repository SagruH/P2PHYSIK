import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const
from scipy.interpolate import make_interp_spline, BSpline


def a14():
    hlines, doK = ppk.readCSV("daten14oK.csv",3)
    hlines, dmK = ppk.readCSV("daten14mK.csv",3)
    vok = doK[2]/doK[1]
    vmk = dmK[2]/dmK[1]

    plt.plot(doK[0], vok, "xb", label = "Ohne Kondensator")
    plt.plot(doK[0], vok, "-b")
    plt.plot(dmK[0], vmk, "xr", label = "Mit Kondensator")
    plt.plot(dmK[0], vmk, "-r")
    plt.legend()
    plt.xscale("log")
    plt.xlabel("f in Hz")
    plt.ylabel("Verstärkungsfaktor")
    plt.grid(True)
    plt.show()
    return;


def a23():
    hlines, d = ppk.readCSV("daten23.csv",3)
    v = d[1]/0.5

    plt.plot(d[0], v, "xb")
    plt.plot(d[0], v, "-b")
    plt.legend()
    plt.xscale("log")
    plt.xlabel("f in Hz")
    plt.ylabel("Verstärkungsfaktor")
    plt.grid(True)
    plt.show()
    return;


a23()
