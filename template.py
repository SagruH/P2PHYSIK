import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const

#import kafe
#from kafe.function_tools import FitFunction, LaTeX, ASCII
#from kafe.function_library import quadratic_3par

import uncertainties as uc
from uncertainties.umath import sqrt


def loadCSV(name,hlines=1,split=2): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def plot(data):  # alle zeilen zum ploten von daten
    plt.plot(data[0],data[1],label="test")
    plt.legend()
    plt.title("Messdaten")
    plt.xlabel("h in cm")
    plt.ylabel("t in s")
    plt.grid(True)
    plt.show()
    return;

def lineareRegression(x,y):
    return slope, intercept, r_value, p_value, std_err = stats.linregress(x, y);

'''
fehler rechung mit uncertainties
variable = uc.float(wert, fehler)
'''
