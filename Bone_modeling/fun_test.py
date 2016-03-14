#Modify inp file to add microcrack element
import re
import math
import random
import numpy as np
# from abaqus import *
# from abaqusConstants import *

# ###conduct interation to summit multiple jobs 20150607
# for DEN in range(13,25):
# 	for TRA in range(5,11):
# 		# Define file information of the mesh
# 		trail=TRA
# 		mesh_dimension=2 #mesh dimension
# 		density=DEN*0.01#particle density
# 		print density
# 		m=4  #element number per particle

		#lists initialization
trail = 1
DEN   = 50.  # Vf of mineral in extra fibrillar volume
density=DEN*0.01#particle density
print density



lin_num=0
element=[]
PZ=[]
microcrack=[]

PZ = np.array([range(25941,50385)])
micronumber=int(np.size(PZ)*density)
print np.size(PZ)
print micronumber
microcrack=np.random.randint(25941,50385,size=micronumber)


#read file
myfile=open('raw_inp.inp','r')
newfileName='density%03d_trail%02d'%(DEN,trail)
newfilePath='%s.inp'%newfileName
newfile=open(newfilePath,'w')
for line in myfile:
	if len(re.findall('insert microcrack here',line))==1:

		newfile.write('*Elset, elset=Microcrack'+'\n')
		totalelem=len(microcrack)
		for i in range(0,totalelem) :
			if (i+1)%16==0:
				newfile.write('%6d'%microcrack[i]+'\n')
			elif i == totalelem-1:
				newfile.write('%6d'%microcrack[i]+'\n')
			else: 
				newfile.write('%6d'%microcrack[i]+',')


		
	else:
		newfile.write(line)
		lin_num=lin_num+1

	##read element lable and its nodes
	# if len(re.findall('Element, type=CPE4R',line))==1:
	# 	for elementlist in myfile:
	# 		lin_num=lin_num+1
	# 		if len(re.findall('[a-z]',elementlist))>0:
	# 			newfile.write(elementlist)
	# 			break
	# 		else:
	# 			newfile.write(elementlist)
	# 			currentline=list(map(int,elementlist.split(',')))
	# 			element.append(currentline[1:5])

# # 	##read element in the PZ zone 20150601
# 	if len(re.findall('Elset, elset=_G3',line))==1:
# 		for dataline in myfile:
# 			lin_num=lin_num+1
# 			if len(re.findall('[a-z]',dataline))>0:
# 				newfile.write(dataline)
# 				break
# 			else:
# 				newfile.write(dataline)
# 				currentline=list(map(int,dataline.split(',')))
# 				#print len(re.findall('[a-z]',dataline)) #check
# 				for elenum in currentline:
# 					PZ.append(elenum)
# 	else:
# 		continue

# #Randomly choose element from PZ zone (including surrounding elements m=4) 25941-50385

# for i in range(0,np.size(microcrack)):
# 	lablenode=element[microcrack[i]]
# 	for j in range(0,len(element)):
# 		if (lablenode in element[j] and (j+1) in PZ):
# 			temp.append(j+1)
# print 'generated random elements %3d'%len(microcrack)
# print 'total element selected %3d'%len(temp)



# print 'elements after listed %3d'%len(microcrack)

	

#write final microcrack element to file



# myfile.close()
# ##read in the second part of the input file
# myfile=open('C:\\Temp\\Particle dimension\\rawfile_2.inp','r')
# for line_2 in myfile:
# 	newfile.write(line_2)
# myfile.close()
# newfile.close()


# mdb.JobFromInputFile(name=newfileName, 
# 	inputFileName=newfilePath, 
# 	type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
# 	memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
# 	explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, userSubroutine='', 
# 	scratch='', parallelizationMethodExplicit=DOMAIN, numDomains=2, 
# 	activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=2)
# mdb.jobs[newfileName].submit(consistencyChecking=OFF)
##: The job input file "mesh02_density000_group04_trail01.inp" has been submitted for analysis.



