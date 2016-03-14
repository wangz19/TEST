#! /user/bin/python
# - * - coding: UTF-8 - * -
from abaqus import *
from abaqusConstants import *
###---- change working directory-------------
import os
os.chdir(r"Z:\Users\zehaiwang\GitHub\Hetero_square")   #change to function directory to souce macro_modeing

from macro_modeling import *

#parameters
a = 100.0 #正方形边长
m = 1.0 # mesh变长
enginnering_strain = 0.03 # strain 大小3%

square(a,m,enginnering_strain)

### ------------define Job file-------------
mdb.Job(name = 'Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)



### ------------submit jobs----------------
os.chdir(r"C:\Temp\Square")  #chdir to out-put directory
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)







