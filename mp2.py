# -*- coding: utf-8 -*-
import subprocess  
import time,sys  
import numpy
import matplotlib.pyplot as pl
import string

def mp2 (runindex,nums,p,files,i_test_counts,str_savepath,i_dd) :   
    n=140
    k=128
    start=time.clock()
    ps=[]
    s=[""]*nums
    #并发多进程采用cpu个数
    cpu_counts=3
    #cpu_counts = 1
    for i in range(0,nums):
        
        d=round(files*(n-k)/k,0)
        x_f=round(files*p[i],0)
        x_r=round(files*p[i]*(n-k)/k,0)
        #cmdstr="test3.exe  " + '%d' %(files) + " " +'%d' %(d) + " " + '%d' %(k) + " " + '%d' %(n) + " " +  '%d' %(x_f) + " " + '%d' %(x_r) +" 5000"
        cmdstr="test4.exe  " + '%d' %(files) + " " +'%d' %(d) + " " + '%d' %(k) + " " + '%d' %(n) + " " +  '%d' %(x_f) + " " + '%d' %(x_r) +" " + '%d' %(i_test_counts)  + " " +'%d' %(i_dd) 
        print str(p[i]) + " " + cmdstr
        #exit(0)
        oneps=subprocess.Popen(cmdstr, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
        ps.append(oneps)
        
        if (i % cpu_counts)==(cpu_counts-1):
            for idx_ps in range(0,cpu_counts):
                ps[numpy.size(ps)-cpu_counts+idx_ps].wait()
 
    print "running runindex " + str(runindex) ,
   #################bugs#################   
    while True:
        time.sleep(1)
        for i in range(0,nums):
            stmp=ps[i].stdout.read()
            if stmp<>"":
                s[i]=s[i] + stmp
        print ".",
        OK=False
        ps[i].poll()
        if ps[i].returncode is None:
           OK=True
           break
        if not OK:
           break
    ##################################
    ss=[]
    for i in range(0,nums):
        stmp=ps[i].stdout.read()
        if stmp<>"":
            s[i]=s[i] + stmp
        ps[i].stdout.close()
        ps[i].stdin.close()
        ps[i].stderr.close()
        s[i]=s[i].replace("\r\n"," ")
        ssi=s[i].split()
        #print p[i], ssi[numpy.size(ssi)-1]
        ss=numpy.append(ss,string.atof (ssi[numpy.size(ssi)-1]))
        
    start2=time.clock()
    print "all times is", start2-start
    numpy.save(str_savepath+"/mp2-pdamage-" +'%d' %(runindex) + "-" + str(files) + "-" + '%d' %(i_test_counts) + "-costtime.npy",[start2-start])
    numpy.save (str_savepath+"/mp2-pdamage-" +'%d' %(runindex) + "-" + str(files) + "-" + '%d' %(i_test_counts) + ".npy",ss)
    print ss
    #print ss
#######################################################################################################  
if __name__=='__main__':    
#if 1==0:
    if numpy.size(sys.argv)>1:
        runindex=int(sys.argv[1])
    else:
        runindex=1
     
    nums=101
    p=numpy.linspace(0,0.02,nums)
       
    print p
    files=16000*numpy.power(2,3) #128000
    #p=numpy.linspace(1000,2500,nums)*1.0/files
    if numpy.size(sys.argv)>2:
        files=int(sys.argv[2])
        
    i_test_counts=40000
    if numpy.size(sys.argv)>3:
        i_test_counts=int(sys.argv[3])
        
    str_savepath="./tmp-test4"
    str_savepath="./testspeed"

    if numpy.size(sys.argv)>4:
        str_savepath=sys.argv[4]
    
    i_dd=13
    if numpy.size(sys.argv)>5:
        i_dd=int(sys.argv[5])
        
    mp2(runindex,nums,p,files,i_test_counts,str_savepath,i_dd)


