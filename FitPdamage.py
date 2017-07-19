# -*- coding: utf-8 -*-
import subprocess  
import time,sys  
import numpy
import matplotlib.pyplot as pl
import string
from scipy.optimize import leastsq
from math import e


def func0_3(x,p):# method 2
    amin,amax,x0,h,s=p
    t=1.0*x/x0
    t=numpy.power(t,-h)+1
    t=numpy.power(t,s)
    y=(amax-amin)/t+amin
    return y

def residuals1(p,x,y):
	return y - func0_3(x,p)


def FitPdamage2(x,y):
    
    # method 2
    p0 = [0.0,2000,0.025,2,5]  
    plsq = leastsq(residuals1, p0, args=(x,y),maxfev=50000,ftol=1.49012e-8, xtol=1.49012e-8)
    return plsq[0]

if __name__=='__main__':
    files=128000
    nums=101
    p=numpy.linspace(0,0.02,nums)
    
    preTest="./tmp-test4"
    startindex=1
    runindexs=1000
    tmp_all=numpy.zeros(nums)
    for i in range(startindex,runindexs+startindex):
        OK=numpy.load ( preTest +"/mp2-pdamage-" +'%d' %(i) + "-" + str(files) + "-%d" %(1000000)+ ".npy")
        tmp_all=tmp_all+OK
    
    OK=tmp_all/runindexs
    p0=FitPdamage2(p,OK)
    print p0
    newy=func0_3(p,p0)
    newy= newy-newy.min()
    
    #[ -6.18473089e-07   1.06767571e-01   2.60406364e-02   1.11014693e+01] 1000
    #[ -6.12496620e-07   1.04404383e-01   2.59813112e-02   1.11070659e+01] 500
    #[ -6.45257169e-07   9.93377018e-02   2.58598980e-02   1.11074062e+01] 100
    pl.figure  
    ylabel="Fitted $P(damage)$"
    xlabel="the number of corruptions by the attacker"
    title="Fitted $P(damage)$ as a function of the number of corruptions by the attacker"
    pl.ylabel(ylabel)
    pl.xlabel(xlabel)
    pl.title(title)
    x=files*p
    #pl.xlim(500,3000)
    #pl.xlim(0,3000)
    #pl.xlim(1000,1400)
    #pl.xlim(0,5000) 
    #pl.ylim(0,0.007)
    #pl.ylim(0,0.000035)


    pl.plot (x,OK,'-*')#'-*'
    pl.plot (x,newy,'-^')#'-*'
    pl.grid(True)
    pl.show() 
    