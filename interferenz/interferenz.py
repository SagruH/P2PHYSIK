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


def aufgabe11():
    #R**2 = R*k*lambda
    lambdaGelb = 590e-9
    lambdaBlau = 465e-9
    #n, r links in mm, r rechts in mm
    hlines, data = ppk.readCSV("11aufgabeG.csv",2)
    #hlines, data = ppk.readCSV("11aufgabeB.csv",2)
    #lambdaGelb = lambdaBlau
    '''
    for i in np.arange(len(data[2])):
        x = data[2][i]
        data[2][i] = uc.ufloat(x, 0.1)
    for i in np.arange(len(data[1])):
        data[1][i] = uc.ufloat(data[1][i], 0.1)
    for i in np.arange(len(data[0])):
        data[0][i] = uc.ufloat(data[0][i],0)
    '''

    rsq = ( ( (data[1]-data[2])/2 ) * (10**(-3)) )**2
    R = (rsq)/(data[0]*lambdaGelb)
    R = uc.ufloat( np.mean(R), np.std(R) )
    lGk = data[0]*lambdaGelb
    lGk = lGk * (10**9)
    rsq = rsq * (10**9)

    slp, inter, r_value, p_value, std_err = stats.linregress(lGk, rsq)
    #p = np.polyfit(lGk, rsq, 1)
    #pol = np.poly1d(p)
    R2 = uc.ufloat(slp, std_err)
    print(R2)


    plt.plot(lGk, rsq,  "or")
    plt.plot(lGk , lGk*slp + inter, "-b")
    #plt.errorbar(lGk, rsq, yerr = 0.06)
    #plt.plot(lGk , pol(lGk), "-c")
    plt.title("Aufgabe 1.1 Gelbe LED")
    plt.xlabel("lambda*n in nm")
    plt.ylabel("r^2 in nm^2")
    plt.grid(True)
    plt.show()
    return;

def aufgabe12():
    lambdaGelb = 590e-9
    R = 0.701
    hlines, data = ppk.readCSV("12aufgabe.csv",2)
    rsq = ( ( (data[1]-data[2])/2 ) * (10**(-3)) )**2
    lGk = data[0]*lambdaGelb*R
    lGk = lGk * (10**9)
    rsq = rsq * (10**9)

    slp, inter, r_value, p_value, std_err = stats.linregress(lGk, rsq);
    R2 = uc.ufloat(1/slp, std_err)

    plt.plot(lGk, rsq,  "or")
    plt.plot(lGk , lGk*slp + inter, "-b")
    plt.title("Aufgabe 1.2")
    plt.xlabel("lambda*n in nm")
    plt.ylabel("r^2 in nm^2")
    plt.grid(True)
    plt.show()

    print(R2)
    return;

def aufgabe134():


    return;

aufgabe12()
