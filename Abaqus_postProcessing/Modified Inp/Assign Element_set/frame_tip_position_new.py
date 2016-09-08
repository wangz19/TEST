# This code calculate the total reaction force acting on RVE 
#during displacement control
import re
from odbAccess import *

# initialization of modulus name
#        =------------default---------------- -= #
# filePath     = '**'
odbName = 'Hetero_0particle.odb'
stepName = 'Step-2'
assemblyName = 'PART-1-1'
crack_length = 0

#objective sets
ob_set = 'cohesive_layer'
mylabel = []
#crack_tip = []

# Open odb file
odb = openOdb(path = odbName)
myInstance = odb.rootAssembly.instances[assemblyName]

Frames = odb.steps[stepName].frames
CohesiveSet      = myInstance.elementSets[ob_set.upper()]  # convert it to upper nodes

for myele in CohesiveSet.elements:
	mylabel.append(myele.label)


newfilePath='%s_%s_Cracktip.txt'%(odbName,stepName)
newfile=open(newfilePath,'w')
newfile.writelines('frame No., tipPosition:\n')

propagation_frameNo =[]
tipPosition =[]

frame_num = 0
x_temp = 0
for frame in Frames:
	#for frame_num in range(0,len(Frames),interval):
# get field-output
	Damage_coefficient = frame.fieldOutputs['SDEG']
# Get the tip position
	for label in mylabel:
			# print val.data
		if Damage_coefficient.getSubset(region = myInstance.getElementFromLabel(label)).values[0].data > 0.9998:
			tip_node  = myInstance.getElementFromLabel(label).connectivity[1]
			x     = myInstance.getNodeFromLabel(tip_node).coordinates[0]
			# judge if multiple element is degraded in the same step
			if x_temp < x:
				x_temp = x
				#mylabel.remove(label)
				#print label, x
				newfile.writelines('%6d, %6.2f\n'%(frame_num, x_temp))
				propagation_frameNo.append(frame_num)
				tipPosition.append(x)
	frame_num+=1

newfile.close()

previous_frame = 0
#crack_initiation_frame = []
#crackAdvance = []
newfilePath='%s_%s_initiationCrack.txt'%(odbName,stepName)
newfile=open(newfilePath,'w')
newfile.writelines('frame No., tipPosition:\n')
index = 0
for num in propagation_frameNo:
	if (num-previous_frame)> 50:# number of frame difference can be changed
		#crack_initiation_frame.append(num)
		#crackAdvance.append(tipPosition[index])
		newfile.writelines('%6d, %6.2f\n'%(num, tipPosition[index]))
	previous_frame = num
	index+=1

newfile.close()


		
		

	
