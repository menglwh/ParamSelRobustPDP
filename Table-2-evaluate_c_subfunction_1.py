# -*- coding: utf-8 -*-
import subprocess  
import time,sys  
import numpy
import matplotlib.pyplot as pl
import string
from mp2 import mp2 
from FindMin_c_to_Pdetect_and_Pdamage import FindMin_c_to_Pdetect_and_Pdamage
import FitPdamage
import threading
import copy
        
def MyFunc_1(runindex,nums,p,files,delta,str_savepath):
    results=[]
    for indx_times in range(0,numpy.size(timess)):
        
        times=timess[indx_times]
        ss=numpy.load ( str_savepath +"/mp2-pdamage-" +'%d' %(runindex) + "-" + str(files) + "-" + '%d' %(times) + ".npy")
     
       
        if(1):
		p0=FitPdamage.FitPdamage2(p,ss)
		ss=FitPdamage.func0_3(p,p0)
		ymin=ss.min()
		ss=ss-ymin        

        #(result,maxP)= FindMin_c_to_Pdetect_and_Pdamage(nums,p,files,ss,1.8e-11)
        (result,maxP)= FindMin_c_to_Pdetect_and_Pdamage(nums,p,files,ss,delta)
        results=numpy.append(results,result)
        numpy.save("./results/r2-%d-%s.npy"%(runindex,delta),results)
    print results
    
if 1==1:
#if __name__=='__main__':    
    if numpy.size(sys.argv)>1:
        runindex=int(sys.argv[1])
    else:
        runindex=91
    str_savepath="./tmp-test4"
    times=1000
    nums=101
    p=numpy.linspace(0,0.02,nums)
     
    #        for j in range(0,numpy.size(bits)):
                #files=16000*numpy.power(2,bits[j])
    files=128000
    timess=[10000,20000,40000,80000,100000,200000,400000,800000,1000000,10000000]
    timess=[10000,20000,40000,80000,100000,200000,400000,800000,1000000]
    #timess=[1000000]
    delta=2.5e-11
    if numpy.size(sys.argv)>2:
        delta=sys.argv[2]
    MyFunc_1 (runindex,nums,p,files,string.atof(delta),str_savepath)

  







