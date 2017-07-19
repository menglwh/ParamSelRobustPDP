# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import subprocess  
import time,sys  
import numpy
import matplotlib.pyplot as pl
import string
from FindMin_c_to_Pdetect_and_Pdamage import FindMin_c_to_Pdetect_and_Pdamage
import FitPdamage
import threading
import copy
        
def MyFunc_1(runindex,nums,p,files,delta,str_savepath):
    results=[]
    for indx_times in range(0,numpy.size(timess)):
        
        times=timess[indx_times]
        ss=numpy.load ( str_savepath +"/mp2-pdamage-" +'%d' %(runindex) + "-" + str(files) + "-" + '%d' %(times) + ".npy")
        #print ss

	if (1):
		p0=FitPdamage.FitPdamage2(p,ss)
		ss=FitPdamage.func0_3(p,p0)
		ymin=ss.min()
		ss=ss-ymin
		#print p0
	#print files,"......"
         
        #(result,maxP)= FindMin_c_to_Pdetect_and_Pdamage(nums,p,files,ss,1.8e-11)
        (result,maxP)= FindMin_c_to_Pdetect_and_Pdamage(nums,p,files,ss,delta)
        results=numpy.append(results,result)
        numpy.save("./results_40000/r2-%d-%s.npy"%(runindex,delta),results)
    #print results
    return results

if 1==1:
# if __name__=='__main__':    
	str_savepath="./40000_result"

	

	nums=101
	p=numpy.linspace(0,0.02,nums)
     
	bits=range(3,14)
	bits=range(3,4)
	bits=range(3,14)  #[128000, 256000, 512000, 1024000, 2048000, 4096000,  8192000, 16384000, 32768000, 65536000]
	myresultsall=numpy.zeros((20,numpy.size(bits)),dtype=numpy.int)
	for j in range(0,numpy.size(bits)):
		print bits[j],"............"
		files=16000*numpy.power(2,bits[j])
		#files=128000

		timess=[40000]
		delta="1e-10"
		if numpy.size(sys.argv)>2:
			delta=sys.argv[2]
		for runindex in range(1,21):
		
			myresultsall[runindex-1,j]=int(round(MyFunc_1 (runindex,nums,p,files,string.atof(delta),str_savepath)[0],0))
	avgResult=[]
	for j in range(0,numpy.size(bits)):
		#print myresultsall[:,j]
		oneresult=int(round(numpy.average(myresultsall[:,j]),0))
		avgResult.append(oneresult)
		print numpy.average(myresultsall[:,j]),	numpy.mean(myresultsall[:,j]),numpy.std(myresultsall[:,j])


	for runindex in range(1,11):
		for j in range(0,numpy.size(bits)):
			print "%d," %myresultsall[runindex-1,j],
		print ""
	for j in range(0,numpy.size(bits)):
			print "…," ,
	print ""
	for j in range(0,numpy.size(bits)):
			print "%d," %avgResult[j],
	print ""
	for j in range(0,numpy.size(bits)):
			print "%d," %int(round(numpy.std(myresultsall[:,j]),0)),
	#a = input("OK")
  







