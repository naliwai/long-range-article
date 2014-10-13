#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad
import matplotlib as mpl
import sys

mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['font.family'] = "serif"
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 12
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['mathtext.default']="rm"

dx=[5e-4,1e-3,1.5e-3,2e-3,3e-3]
DX=["$5 \cdot 10^{-4}$","$10^{-3}$","$1.5 \cdot 10^{-3}$","$2 \cdot 10^{-3}$","$3 \cdot 10^{-3}$"]
FILES=[
"wake2013-12-19-133852.dat",
"wake2013-12-19-133854.dat",
"wake2013-12-19-133856.dat",
"wake2013-12-19-133858.dat",
"wake2013-12-19-133900.dat"
]

plt.subplot(211)
plt.xlim([52.5,60.0])
i=0
plts=[]
for fi in FILES:
	data=np.loadtxt(fi)
	temp,=plt.plot(data[:,0],data[:,1]/1000,linewidth=1.0)
	plts.append(temp)
	if i==0:
		plt.plot(data[:,0],15-data[:,3]*0.1,color="grey")
	i=i+1
plt.ylabel("$E_{x} / [kV/m]$")
plt.legend(plts,DX,ncol=2,loc=4)
plt.subplot(212)
plt.ylim([-0.5,0.5])
i=0
for fi in FILES:
	data=np.loadtxt(fi)
	plt.plot(data[:,0],data[:,1]/1000,linewidth=1.0)
	if i==0:
		i=i+1
		plt.plot(data[:,0],data[:,3]*0.01-0.5,color="grey")
plt.ylabel("$E_{x} / [kV/m]$")
plt.xlabel("z / m")
plt.tight_layout()
plt.show()
