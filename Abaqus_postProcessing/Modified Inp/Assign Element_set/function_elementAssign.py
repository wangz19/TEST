import random
# import re

#This function write node list to .inp file
#input information is the listname and filename of node list
def wirteNodeList(ListName, filePath):
	Collumn_No = 16
	newfilePath='%s'%filePath+'.inp'
	newfile=open(newfilePath,'w')
	for i in range(len(ListName)):
		i = i+1
		if i == len(ListName):
			temp = '%6d'%ListName[i-1]
			newfile.write(temp)
		elif i%Collumn_No == 0:
			temp = '%6d\n'%ListName[i-1]
			newfile.write(temp)
		else:
			temp = '%6d,'%ListName[i-1]
			newfile.write(temp)
	
# This function generate relization of heterogeneous case with defined particle density
def elementAssign (Den_hard, Den_trans):
	# default debug value
	# Den_hardParticle = 0.4  # density of hard particle
	# Den_transform = 0.1  # Particles transformed into bilinear plastic material
	myfile_down=open('down_new.inp','r') #fliped using 'flip.py'
	myfile_up=open('up.inp','r')
	Hard_element = []
	Soft_element = []
	Transformed_element = [] #Transformed particle list
	##Related to symmetrical assignment of hyterogeneity
	Element_up = []      # Element upper side of the model
	Element_down = []	#Element lower side of the model
	Collumn_NO = 16 # number of collumn # Default value for .inp file data structure
	##Read elements in up-area line by line
	for line in myfile_up:
				# read the node list
		currentline=list(map(float,line.split(',')))
		for i in range(Collumn_NO):
			Element_up.append(currentline[i])
	# print Element_up
	for line in myfile_down:
				# read the node list
		currentline=list(map(float,line.split(',')))
		for i in range(Collumn_NO):
			Element_down.append(currentline[i])
	# print Element_down
	if len(Element_up) == len(Element_down):
		population = range(len(Element_up)) # number of element in up/down area, generate indecies
	else:
		print "error in up/down element list, element number do not match"
	## Select Hard particles
	index = sorted(random.sample(population, int(len(population)*Den_hard)))
	# print index
	# print len(index)
	for i in index:
		Hard_element.append(int(Element_up[i]))
		Hard_element.append(int(Element_down[i]))
	# print Hard_element
	wirteNodeList(Hard_element,'hard_new')
	## All the particle not included in the hard_particle set Z
	index_difference = list(set(population).difference(set(index)))
	## Select transformed particles
	index_transformed = sorted(random.sample(index_difference, int(len(index_difference)*Den_trans)))
	for i in index_transformed:
		Transformed_element.append(int(Element_up[i]))
		Transformed_element.append(int(Element_down[i]))
	wirteNodeList(Transformed_element,'transformed_new')
	index_soft = list(set(index_difference).difference(set(index_transformed)))
	for i in index_soft:
		Soft_element.append(int(Element_up[i]))
		Soft_element.append(int(Element_down[i]))
	wirteNodeList(Soft_element,'soft_new')

# main function
import re
import math
import random
from abaqus import *
from abaqusConstants import *

Den_hard = 0.4
Den_trans = 0.0
raw_file = hetero_raw_1

NumOfRealization = 3

for trail in range(NumOfRealization):
	newfileName='Hetero_%02d_%02d_trail%02d'%(Den_hard*100,Den_trans*100,trail)
	newfilePath='%s.inp'%raw_file

	elementAssign(Den_hard,Den_trans)

	mdb.JobFromInputFile(name=newfileName, 
				inputFileName=newfilePath, 
				type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
				memory=99, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
				explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, userSubroutine='', 
				scratch='', parallelizationMethodExplicit=DOMAIN, numDomains=2, 
				activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=2)
	mdb.jobs[newfileName].submit(consistencyChecking=OFF)
# mdb.jobs[newfileName].waitForCompletion()
