#!/hera/bhs/fpetrov/epd-7.3-1-rh5-x86_64/bin/python
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
mpl.rcParams['legend.fontsize'] = 14
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['mathtext.default']="rm"

data=np.loadtxt(sys.argv[1])
x=np.arange(0,len(data[1]),1)
y=np.arange(0,len(data),1)
dx=2.0*1.0/(len(x)-1)
dy=7.5/(len(y)-1)
X=np.ones(2)*(0.04*1.05-0.04)/2
Y=np.array([0,0.04*1.05])
mina=np.amin(data)
maxa=np.amax(data)
mean=np.mean(data)
#plt.subplot(211)
#plt.subplot(211)
CS=plt.contourf(x*dx,y*dy,np.log((data/maxa)*1000.0+1.0),50)
#CS=plt.contourf(x*dx,y*dx,np.log(data*100/maxa+1.0),50)
#plt.subplot(211)

#CS=plt.contourf(x*dx,y*dx,data/maxa,50)
#plt.ylim([0,500])
XX=[]
YY=[]
plt.xlabel("x / cm")
plt.ylabel("z / m")
cbar = plt.colorbar(CS)
cbar.ax.set_ylabel('ln($n_{e}/n_{e,max} \cdot 1000$+1)')
#plt.subplot(212)
#plt.plot(x,data[500],marker="o")
#maxa=np.amax(data[500])
#plt.ylim([0,maxa])
#print("Maximum %e" % (maxa))
#print("Average %e" % (np.sum(data[500]*x)/np.sum(x)))
#plt.subplot(221)
LENG=len(data)/9
#for i in range(9):
#	plt.plot(x,np.sum(data[i*LENG:(i+1)*LENG],axis=0)*100/LENG+maxa*LENG/10*i)
plt.show()
#plt.savefig("uniform1.png")
