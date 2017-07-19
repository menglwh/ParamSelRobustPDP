# -*- coding: utf-8 -*-
import subprocess  
import time,sys  
import datetime
import numpy
import matplotlib.pyplot as pl
import string
from mp2 import mp2 
#from FindMin_c_to_Pdetect_and_Pdamage import FindMin_c_to_Pdetect_and_Pdamage

runindexs=1
str_savepath="./resulttestspeed-20170712"

nums=101
p=numpy.linspace(0,0.02,nums)
startindex=1
if numpy.size(sys.argv)>1:
    startindex=int(sys.argv[1]) 

files=128000
timess=[200,300,10000,20000,40000,80000,100000,200000,400000,800000,1000000]
timess=[5000,20000,40000,80000]
multi_results=[]
bits=range(10,11)
p1=p
for j in range(0,numpy.size(bits)):
	files=16000*numpy.power(2,bits[j])
	for runindex in range(startindex,runindexs+1):
		results=[]
		for indx_times in range(0,numpy.size(timess)):
			times=timess[indx_times]
		   
			#        cmdstr="python mp2.py " + '%d' %(i) + " " + '%d'%(files) + " " + str(times)+ " " + str_savepath +  " 13" 
			#        print cmdstr
			#        subprocess.call(cmdstr)
			print "Waiting for " + str(runindex) + " " +  '%d'%(files) + ' %d'%(times)
			sys.stderr.write("Waiting for " + str(runindex) + " " +  '%d'%(files) + ' %d'%(times)+"\n")
			sys.stderr.write("==========================\n"+str(datetime.datetime.now())+"\n")
			
			start=time.clock()
			sys.stderr.write(str(start)+"\n")
			mp2 (runindex,nums,p,files,times,str_savepath,13)
			start2=time.clock()
			sys.stderr.write("all times is " + str(start2-start)+"\n")
			sys.stderr.write("==========================\n"+str(datetime.datetime.now())+"\n")

print "Finished"





