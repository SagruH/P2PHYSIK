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
from uncertainties.umath import sqrt, sin


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
    xl = uc.ufloat(1.3,0.001)
    xrt = uc.ufloat(0.293,0.001)
    xr = xl - (xl.n - xrt.n)
    f = xl - xr
    R = uc.ufloat(0.571, 0.029)
    n = R/f + 1
    print("f  ", f, "\nn  " ,n)
    return;


def aufgabe22():
    hlines, data = ppk.readCSV("22aufgabe.csv",2)
    k = data[0]
    deg = data[1]
    min = [0,1,2,3,4]
    for i in np.arange(len(data[2])):
        x = data[2][i]
        min[i]= uc.ufloat(x, 3)
    min[2] = uc.ufloat(0,0)
    lamNa = 589.3e-9 #m
    min = np.array(min)

    ddec = deg + (min * (1/60))
    ddec[0] -= 360
    ddec[1] -= 360
    sindeg = [0,1,2,3,4]
    sdoe = [0,1,2,3,4]
    se = [0,1,2,3,4]
    for i in np.arange(5):
        x = ddec[i]
        x = (x/180)*np.pi
        sx = sin(x)
        sindeg[i] = sx
        sdoe[i] = sx.n
        se[i] = sx.s

    slp, inter, r_value, p_value, std_err = stats.linregress(k, sdoe);
    m = uc.ufloat(slp,std_err)
    g = lamNa / m
    print("g ", g)

    plt.plot(k, sdoe, "or")
    plt.plot(k , k*slp + inter, "-b")
    plt.xlabel("k")
    plt.ylabel("sin(alpha)")
    plt.grid(True)
    plt.show()

    return;

def aufgabe23():
    g = uc.ufloat(1.658,0.006)
    g = g * 1e-6

    hlines, data = ppk.readCSV("232aufgabe.csv",2)
    k = data[0]
    deg = data[1]
    min = [0,1,2,3,4]
    for i in np.arange(len(data[2])):
        x = data[2][i]
        min[i]= uc.ufloat(x, 3)
    min[2] = uc.ufloat(0,0)
    min = np.array(min)

    ddec = deg + (min * (1/60))
    ddec[0] -= 360
    ddec[1] -= 360
    sindeg = [0,1,2,3,4]
    sdoe = [0,1,2,3,4]
    se = [0,1,2,3,4]
    for i in np.arange(5):
        x = ddec[i]
        x = (x/180)*np.pi
        sx = sin(x)
        sindeg[i] = sx
        sdoe[i] = sx.n
        se[i] = sx.s

    slp, inter, r_value, p_value, std_err = stats.linregress(k, sdoe);
    m = uc.ufloat(slp,std_err)
    lam = g*m
    print("l ", lam)

    plt.plot(k, sdoe, "or")
    plt.plot(k , k*slp + inter, "-b")
    plt.xlabel("k")
    plt.ylabel("sin(alpha)")
    plt.grid(True)
    plt.show()
    return;

def aufgabe24():
    hlines, data = ppk.readCSV("24aufgabe.csv",2)
    k = data[0]
    deg = data[1]
    min = [0,1,2,3,4,5,6]
    for i in np.arange(len(data[2])):
        x = data[2][i]
        min[i]= uc.ufloat(x, 3)
    min[2] = uc.ufloat(0,0)
    lamNa = 589.3e-9 #m
    min = np.array(min)

    ddec = deg + (min * (1/60))
    ddec[0] -= 360
    ddec[1] -= 360
    ddec[2] -= 360
    sindeg = [0,1,2,3,4,5,6]
    sdoe = [0,1,2,3,4,5,6]
    se = [0,1,2,3,4,5,6]
    for i in np.arange(7):
        x = ddec[i]
        x = (x/180)*np.pi
        sx = sin(x)
        sindeg[i] = sx
        sdoe[i] = sx.n
        se[i] = sx.s

    slp, inter, r_value, p_value, std_err = stats.linregress(k, sdoe);
    m = uc.ufloat(slp,std_err)
    g = lamNa / m
    print("g ", g)

    plt.plot(k, sdoe, "or")
    plt.plot(k , k*slp + inter, "-b")
    plt.xlabel("k")
    plt.ylabel("sin(alpha)")
    plt.grid(True)
    plt.show()
    return;

def aufgabe25():
    g = uc.ufloat(6.098,0.016)
    g = g * 1e-6

    hlines, data = ppk.readCSV("25raufgabe.csv",2)
    k = data[0]
    deg = data[1]
    min = [0,1,2,3,4]
    for i in np.arange(len(data[2])):
        x = data[2][i]
        min[i]= uc.ufloat(x, 3)
    min[2] = uc.ufloat(0,0)
    min = np.array(min)

    ddec = deg + (min * (1/60))
    ddec[0] -= 360
    ddec[1] -= 360
    sindeg = [0,1,2,3,4]
    sdoe = [0,1,2,3,4]
    se = [0,1,2,3,4]
    for i in np.arange(5):
        x = ddec[i]
        x = (x/180)*np.pi
        sx = sin(x)
        sindeg[i] = sx
        sdoe[i] = sx.n
        se[i] = sx.s

    slp, inter, r_value, p_value, std_err = stats.linregress(k, sdoe);
    m = uc.ufloat(slp,std_err)
    lam = g*m
    print("l ", lam)

    plt.plot(k, sdoe, "or")
    plt.plot(k , k*slp + inter, "-b")
    plt.xlabel("k")
    plt.ylabel("sin(alpha)")
    plt.grid(True)
    plt.show()
    return;


aufgabe25()
