# -*- coding: utf-8 -*-
import subprocess  
import time,sys  
import numpy
import matplotlib.pyplot as pl
import string
from mp2_Pdetect_two import mp2_Pdetect_two

def FindMin_c_to_Pdetect_and_Pdamage(nums,p,files,ss,minP):
    n=140
    k=128
    #minP= 1.8e-11#1e-10 #5.64723029431e-12
    #minP= 1e-10
    low=1
    high=20000#int(files)*n/k

    highP=2
    lowP=-1
    #print "Bin Searching......."
    idx=0
    while high-low>1:  
        #############################################
        c=round((low+high)/2,0)
	#print "mp2_Pdetect_two staring......."
        ss2=mp2_Pdetect_two(1,nums,p,files,"",c)
	#print "mp2_Pdetect_two finished......."
        maxP=numpy.max(ss*ss2)
	idx=numpy.argmax(ss*ss2)
        #print "[%d,%d]"%(low,high),c,maxP
        if maxP<minP:# or maxP<>maxP or maxP==float('Inf') or maxP==float('-Inf'):
            high=c
            highP=maxP
        else:
            low=c
            lowP=maxP
	#print str(files) + " " + '%d' %(high) + " " + str(high/files),lowP,highP
    #print str(files) + " " + '%d' %(high) + " " + str(high/files),lowP,highP,ss[idx],idx,p[idx]
    #print "",p[idx],
    if (0):
	    print str(files) + " " + '%d' %(high) + " " + str(high/files),lowP,highP,ss[idx],idx
	    ss2=mp2_Pdetect_two(1,nums,p,files,"",high)
	    while (idx>0):
		print str(idx) + " " + str(ss[idx]) +  " " + str(ss2[idx]) +  " " + str(ss2[idx]*ss[idx])  +  " " + str(p[idx]) 
		idx=idx-1
    return (high,highP)
    
if __name__=='__main__':  
#if 1==0:
    nums=101
    p=numpy.linspace(0,0.02,nums)
    #print p
    
    
    runindexs=1
       
    str_savepath="./tmp-test4" 
    str_savepath="./tmp-test4-20160122" 
    if numpy.size(sys.argv)>1:
        files=int(sys.argv[1])
    else:
        files=128000
    
    i_test_counts=200000
    
    ss=numpy.zeros(nums)
   
    for runindex in range(1,runindexs+1):
            st3=numpy.load ( str_savepath +"/mp2-pdamage-" +'%d' %(runindex) + "-" + str(files) + "-" + '%d' %(i_test_counts) + ".npy")
            ss=ss+st3
    ss=ss/runindexs 
    
    print  FindMin_c_to_Pdetect_and_Pdamage(nums,p,files,ss,1e-10)
