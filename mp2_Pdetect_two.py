# -*- coding: utf-8 -*-
import subprocess  
import time,sys  
import numpy
import matplotlib.pyplot as pl
import string



def mp2_Pdetect_two(runindex,nums,p,files,str_savepath,c):#runindex always =1 and str_savepath can be ""
 ###################################################
    ss2=numpy.power(1-p,c)
    #numpy.save (str_savepath +"/mp2-1-pdetect-" +'%d' %(runindex) + "-" +str(c) + ".npy",ss2) 
    return ss2

def mp2_Pdetect_two_old(runindex,nums,p,files,str_savepath,c):#runindex always =1 and str_savepath can be ""
    n=140
    k=128
   
   #############################################
    c_f=round(c*k/n,0)
    c_r=c-c_f
  
    P_f_down=1-numpy.power(1-p,c_f)
    P_r_down=1-numpy.power(1-p,c_r)
    ###################
    P_f_up=1-numpy.power(1-1.0*files*p/(files-c_f+1),c_f)
    P_r_up=1-numpy.power(1-1.0*files*p*(n-k)/k/(1.0*files*(n-k)/k-c_r+1),c_r)
    ###############################################
    P_Detect1=P_f_down+P_r_down-P_f_up*P_r_up
    P_Detect2=P_f_down+P_r_down-P_f_down*P_r_down
    P_Detect3=P_f_up+P_r_up-P_f_up*P_r_up
    
    p_f_real=1.0
    for i in range(0,int(round(c_f,0))):
        p_f_real=p_f_real*(files-files*p-i)/(files-i)
    p_f_real=1-p_f_real
    p_r_real=1.0
    for i in range(0,int(round(c_r,0))):
        p_r_real=p_r_real*(1.0*files*(n-k)/k-1.0*files*(n-k)/k*p-i)/(1.0*files*(n-k)/k-i)
    p_r_real=1-p_r_real
    P_Detect4=p_f_real+p_r_real-p_f_real*p_r_real
###################################################
    ss2=1-P_Detect2
#    print 1-P_Detect1
#    print 1-P_Detect2
#    print 1-P_Detect3
#    print 1-P_Detect4
    #numpy.save (str_savepath +"/mp2-1-pdetect-" +'%d' %(runindex) + "-" +str(c) + ".npy",ss2) 
    return ss2

if __name__=='__main__':  
#if 1==0:
   
        
    files=128000
    str_savepath="./tmp-test4"
   
        
    nums=101
    p=numpy.linspace(0,0.02,nums)
    
    #nums=151
    #p=numpy.linspace(1000,2500,nums)*1.0/files
    print p
    
    
    c=[400,600,1000,1188,1500,2000]
    #for j in range(0,numpy.size(c)):
    c=[1188]
    
    
    pl.figure(figsize=(8,4))

    pl.subplot(1,2,1)
    ylabel=""
    xlabel=""
    title=''
    xticks=p
    pl.ylabel(ylabel)
    pl.xlabel(xlabel)
    pl.title(title)
    #pl.xlim(0.00022,0.00028)
    #pl.plot (p,1-P_Detect1,'-*')
    ss2= mp2_Pdetect_two(1,nums,p,files,str_savepath,c[0])
    pl.plot (p,ss2,'-*')
 
    sstmp=ss2
	
    pl.subplot(1,2,2)
    ylabel=""
    xlabel=""
    title=''
    xticks=p
    pl.ylabel(ylabel)
    pl.xlabel(xlabel)
    pl.title(title)
    #pl.xlim(0.00022,0.00028)
    #pl.plot (p,1-P_Detect1,'-*')
    ss2= mp2_Pdetect_two_old(1,nums,p,files,str_savepath,c[0])
    pl.plot (p,ss2,'-*')
	
    #pl.plot (p,1-P_Detect3,'-*')
    #pl.plot (p,1-P_Detect4,'-1')
    #pl.legend(['down-up','down-down','up-up','real'],loc='upper right')    
    pl.grid(True)
    pl.show()
	
    print "delta"
    print sstmp-ss2
    
  



