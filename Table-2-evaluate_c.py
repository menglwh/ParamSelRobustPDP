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
startindex=1
runindexs=2000

ps=[]
for runindex in range(startindex,runindexs+startindex):
    results=[]
    cpu_counts=3
    cmdstr="python Table-2-evaluate_c_subfunction_0.py  " + '%d' %(runindex) + " " +'1e-10'
    print  cmdstr
    oneps=subprocess.Popen(cmdstr, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE,shell = False)
    ps.append(oneps)
    if ((runindex-startindex) % cpu_counts)==(cpu_counts-1):
        for idx_ps in range(0,cpu_counts):
            ps[numpy.size(ps)-cpu_counts+idx_ps].wait()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stdin.close()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stdout.close()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stderr.close()
        
for runindex in range(0,runindexs):
    ps[runindex].wait()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stdin.close()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stdout.close()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stderr.close()

###########################################################################################
ps=[]
for runindex in range(startindex,runindexs+startindex):
    results=[]
    cpu_counts=3
    cmdstr="python Table-2-evaluate_c_subfunction_1.py  " + '%d' %(runindex) + " " +'1.5e-11'
    print  cmdstr
    oneps=subprocess.Popen(cmdstr,stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
    ps.append(oneps)
    if ((runindex-startindex) % cpu_counts)==(cpu_counts-1):
        for idx_ps in range(0,cpu_counts):
            ps[numpy.size(ps)-cpu_counts+idx_ps].wait()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stdin.close()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stdout.close()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stderr.close()
        
for runindex in range(0,runindexs):
    ps[runindex].wait()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stdin.close()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stdout.close()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stderr.close()
print ("Finished")

###########################################################################################
ps=[]
for runindex in range(startindex,runindexs+startindex):
    results=[]
    cpu_counts=3
    cmdstr="python Table-2-evaluate_c_subfunction_1.py  " + '%d' %(runindex) + " " +'1e-10'
    print  cmdstr
    oneps=subprocess.Popen(cmdstr,stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
    ps.append(oneps)
    if ((runindex-startindex) % cpu_counts)==(cpu_counts-1):
        for idx_ps in range(0,cpu_counts):
            ps[numpy.size(ps)-cpu_counts+idx_ps].wait()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stdin.close()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stdout.close()
            ps[numpy.size(ps)-cpu_counts+idx_ps].stderr.close()
        
for runindex in range(0,runindexs):
    ps[runindex].wait()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stdin.close()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stdout.close()
    ps[numpy.size(ps)-cpu_counts+idx_ps].stderr.close()
print ("Finished")


#params=[1.24688E-5,2074.85619,0.05498,12.68283] #10000
#params=[-4.14524E-7,0.098,0.02576,11.22639] #100000
#params=[-4.14524E-7,0.098,0.02576,11.22639] #100000
#params=[-6.81977E-7,0.19926,0.0276,11.05788]#200000
#params=[2.19324E-6,0.0374,0.02329,11.68589]#400000
#params=[2.36453E-6,0.03532,0.02322,11.62081]
#params=[-1.51586E-7,0.15001,0.02687,11.10264]#1000000
#params=[-1.52206E-6,119.44713,0.05033,10.83356]
#params=[-1.38895E-6,1.30152,0.03312,10.85597]

  







