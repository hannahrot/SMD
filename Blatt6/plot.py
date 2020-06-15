import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

from scipy.optimize import curve_fit

#import uncertainties.unumpy as unp

from uncertainties import ufloat

from scipy.stats import stats

from scipy import linalg



P0x = np.array([1,2,1.5,2,2,3])
P0y = np.array([1,1,2,2,3,3])
P1x = np.array([1.5, 2.5, 3.5, 2.5, 3.5, 4.5])
P1y = np.array([1,1,1,2,2,2])

m=0.254/(-0.256)
def f(x):
  return m*x+4



x = np.linspace(0.9, 3.6,100)
#y = np.linspace(0.9, 3.6,100)



plt.plot(P0x, P0y, 'bx', label=r'$P_0$')

plt.plot(P1x, P1y, 'rx', label=r'$P_1$')

plt.plot(x, f(x), 'k-', label=r'Projektionsgerade $\lambda \vec{e}_\lambda$')



plt.legend()

plt.tight_layout()

plt.savefig('c.pdf')



plt.clf()



# d)
