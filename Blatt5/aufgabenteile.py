import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

#np.random.seed(44) #seed macht das Ganze reprduzierbar
size = int(1e7)

mu = 2
sig = 1

log10hits = np.random.normal(mu, sig, size)
hits = [ int(10**x) for x in log10hits ]

dfBackHits = pd.DataFrame({'NumberOfHits': hits}) #Hits der Untergrundereignisse

plt.hist(log10hits, bins=50, density=True, label=r'Untergrund')
plt.xlabel(r'$\log_{10}{(\mathrm{Hits})}$')
plt.legend()
plt.tight_layout()
plt.savefig('e_hits.pdf')

plt.clf()

#np.random.seed(4)
def ort(mu, sig, rho, size):
    x=[] #leere Liste wird erzeugt
    y=[]
    while len(x)<size:
        xx = np.random.normal(0, 1)
        yy = np.random.normal(0, 1)

        xx = np.sqrt(1-rho**2)*sig*xx+rho*sig*yy+mu
        yy = sig*yy+mu

        if 0 <= xx <= 10 and 0 <= yy <= 10:
            x.append(xx) #xx wird an die leere Liste angehängt
            y.append(yy)

    return x, y

mu = 5
sig = 3
rho = 0.5

x, y = ort(mu, sig, rho, size)

plt.grid()
plt.hist2d(x,y, bins=[100,100], range=[[0,10],[0,10]], cmap='inferno')
plt.colorbar()
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.savefig('e_detektor.pdf')
plt.clf()

dfBackX = pd.DataFrame({'x': x})
dfBackY = pd.DataFrame({'y': y})

dfBackground = pd.concat([dfBackHits, dfBackX, dfBackY], axis=1)
dfBackground = dfBackground.to_hdf('NeutrinoMC.hdf5', key='Background')
