# -*- coding: utf-8 -*-
import subprocess  
import time,sys  
import numpy
import matplotlib.pyplot as pl
import string
from mp2 import mp2 

runindexs=20000
runindexs=1
str_savepath="./tmp-test4"

nums=101
p=numpy.linspace(0,0.02,nums)
startindex=1
if numpy.size(sys.argv)>1:
    startindex=int(sys.argv[1]) 

files=128000
timess=[200,300,10000,20000,40000,80000,100000,200000,400000,800000,1000000]

multi_results=[]
for runindex in range(startindex,runindexs+1):
    results=[]
    for indx_times in range(0,numpy.size(timess)):
        times=timess[indx_times]
       
        #        cmdstr="python mp2.py " + '%d' %(i) + " " + '%d'%(files) + " " + str(times)+ " " + str_savepath +  " 13" 
        #        print cmdstr
        #        subprocess.call(cmdstr)
        mp2 (runindex,nums,p,files,times,str_savepath,13)
        print "Waiting for " + str(runindex) + " " +  '%d'%(files) + ' %d'%(times)
 
print "Finished"





