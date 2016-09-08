# Function select element for domain J-integral
# by defining the ring center (x_c, y_c) && inner/outter radius r1/r2
# for planar crack center_y = 0
# t1='distance from inner contour to the crack tip', ringThickness, tipPosition):
import math
def polygonArea (x,y):
	# input coordinates of n vortices
	if len(x) == len(y):
		n = len(x)
	else:
		print 'input vertices error, please check'
	#extend the coordinate lists
	x.append(x[0])
	y.append(y[0])
	temp_p, temp_n = 0,0
	for i in range (0,n):
		temp_p += x[i]*y[i+1]
		temp_n += y[i]*x[i+1]
	Area = abs(0.5*(temp_p-temp_n))
	return Area

def Geometrical_set (odb, center_x, center_y, t1, ringThickness, tipPosition, IntegralSet):
	#initiate default parameter
	# stepName     = 'Step-1'
	assemblyName = 'PART-1-1'
	r1           = abs(center_x-tipPosition)+t1
	r2           = r1+ringThickness
	# Set model database
	myInstance        = odb.rootAssembly.instances[assemblyName]
	IntegralCandidate = myInstance.elementSets[IntegralSet.upper()] # Name of element set should be in upper case
	# Interested parameter
	# parameter from element geometrical information
	elementClass  = []		# Elements (labels) in the integral domain
	q_coefficient = []	
	nodeLabel     = []		# node connectivity for each element 
	Xs            = []		# dx/ds
	xe            = []		# element x coordinate
	ye            = []		# element y coordinate	
	Xeta          = []		# dx/deta
	Ys            = []		# dy/ds
	Yeta          = []		# dy/deta
	Jacobian      = []
	dA            = []		#element Area
	# N Shape function coefficient for bilinear 4 node element
	Ns            = [0.25, -0.25, -0.25, 0.25]	# dN/ds
	Neta          = [0.25, 0.25, -0.25, -0.25]	# dN/deta
	# loop over the candidate element sets
	for myele in IntegralCandidate.elements:
		mylabel = myele.label
		myNode  = [0,0,0,0]
		x = [0,0,0,0]
		y = [0,0,0,0]
		# Position of single integration point
		tempX,tempY  = 0,0
		for i in range(0,4):
			myNode[i] = myInstance.getElementFromLabel(mylabel).connectivity[i]
			x[i]      = myInstance.getNodeFromLabel(myNode[i]).coordinates[0]
			y[i]      = myInstance.getNodeFromLabel(myNode[i]).coordinates[1]
			tempX     = tempX+ 0.25*x[i]
			tempY     = tempY+ 0.25*y[i]
		# what hppened here
		tempR = math.sqrt((tempX-center_x)**2+(tempY-center_y)**2)
		if tempR >=r1 and tempR <= r2:
			tempLabel       = mylabel
			q               = (tempR-r2)/(r1-r2)
			coefficient_x   = (tempX-center_x)/((r1-r2)*tempR)
			coefficient_y   = (tempY-center_y)/((r1-r2)*tempR)
			area = polygonArea(x,y)
			dA.append(area)
			nodeLabel.append([myNode[0],myNode[1],myNode[2],myNode[3]])
			xe.append([x[0],x[1],x[2],x[3]])
			ye.append([y[0],y[1],y[2],y[3]])
			# set derivative
			Xs_temp   = Ns[0]*x[0]+Ns[1]*x[1]+Ns[2]*x[2]+Ns[3]*x[3]
			Xeta_temp = Neta[0]*x[0]+Neta[1]*x[1]+Neta[2]*x[2]+Neta[3]*x[3]
			Ys_temp   = Ns[0]*y[0]+Ns[1]*y[1]+Ns[2]*y[2]+Ns[3]*y[3]
			Yeta_temp = Neta[0]*y[0]+Neta[1]*y[1]+Neta[2]*y[2]+Neta[3]*y[3]
			Xs.append (Xs_temp)
			Xeta.append (Xeta_temp)
			Ys.append (Ys_temp)
			Yeta.append (Yeta_temp)
			# set Jacobian
			Jacobian_temp = Xs_temp*Yeta_temp - Xeta_temp*Ys_temp
			Jacobian.append (Jacobian_temp)
			# append element and coefficient
			elementClass.append(tempLabel)
			q_coefficient.append([q, coefficient_x, coefficient_y])
	return [elementClass,q_coefficient,Xs,Xeta,Ys,Yeta,Jacobian,dA,nodeLabel]

def integralCal(num1,num2,interval,odb,stepName,elementClass,q_coefficient,Xs,Xeta,Ys,Yeta,Jacobian,dA,nodeLabel,initiation_frame):
	# from odbAccess import *
	assemblyName = 'PART-1-1'
	myInstance = odb.rootAssembly.instances[assemblyName]
	Frames = odb.steps[stepName].frames
	# N Shape function coefficient for bilinear 4 node element
	Ns            = [0.25, -0.25, -0.25, 0.25]	# dN/ds
	Neta          = [0.25, 0.25, -0.25, -0.25]	# dN/deta
	ue = [0,0,0,0]		# element x displacement
	ve = [0,0,0,0]		# element y displacement
	# qe = [0,0,0,0]
	#intresets parameter
	f_n       = [] 
	J1_values = []
	J2_values = []
	# tip       = []
	if num2 == 0:
		num1 = 1
		num2 = len(Frames)
	else:
		num2 = num2+1
	frame_num = 0
	# iterate over each frame
	#-----------------20160612 judge the tip initiation--------------#
	# integral_frameNo = [43,89,143,207,268,328,384,447]
	for frame in Frames:
		if frame_num    in initiation_frame:
			J1                  = 0
			J2                  = 0
			displacement_U      = frame.fieldOutputs['U']
			strainEnergyDensity = frame.fieldOutputs['ESEDEN']
			stress_S            = frame.fieldOutputs['S']
			# get field-output
			# Damage_coefficient = frame.fieldOutputs['SDEG']
			# strain_E            = frame.fieldOutputs['E']
			coefficient_index   = 0				# link value back to connectivity list
		
		# Get the tip position
			# for val in Damage_coefficient.values:
			# 	# print val.data
			# 	if val.data != 1:
			# 		mylabel = val.elementLabel
			# 		# print mylabel
			# 		break
			# myNode      = myInstance.getElementFromLabel(mylabel).connectivity[0]
	# print myNode
			# tipPosition = myInstance.getNodeFromLabel(myNode).coordinates[0]
	##------------------interate over element for J integral -------------#
			for myelement in elementClass:
				tempE_density = strainEnergyDensity.getSubset(region = myInstance.getElementFromLabel(myelement),position=WHOLE_ELEMENT).values[0].data
				temp_s11      = stress_S.getSubset(region = myInstance.getElementFromLabel(myelement)).values[0].data[0]
				temp_s22      = stress_S.getSubset(region = myInstance.getElementFromLabel(myelement)).values[0].data[1]
				temp_s12      = stress_S.getSubset(region = myInstance.getElementFromLabel(myelement)).values[0].data[3]
				# temp_e11      = strain_E.getSubset(region = myInstance.getElementFromLabel(myelement)).values[0].data[0]
				# temp_e22      = strain_E.getSubset(region = myInstance.getElementFromLabel(myelement)).values[0].data[1]
				# temp_e12      = strain_E.getSubset(region = myInstance.getElementFromLabel(myelement)).values[0].data[3]
				for i in range (0,4):
					ue[i] = displacement_U.getSubset(region = myInstance.getNodeFromLabel(nodeLabel[coefficient_index][i])).values[0].data[0]
					ve[i] = displacement_U.getSubset(region = myInstance.getNodeFromLabel(nodeLabel[coefficient_index][i])).values[0].data[1]
					# coefficient calculation for each nodes
					# tempX = xe[coefficient_index][i]
					# tempY = ye[coefficient_index][i]
					# tempR = sqrt((tempX-center_x)**2+(tempY-center_y)**2)
					# qe[i] = (tempR-r2)/(r1-r2)
				# print ue
				Us   = Ns[0]*ue[0]+Ns[1]*ue[1]+Ns[2]*ue[2]+Ns[3]*ue[3]
				Ueta = Neta[0]*ue[0]+Neta[1]*ue[1]+Neta[2]*ue[2]+Neta[3]*ue[3]
				Vs   = Ns[0]*ve[0]+Ns[1]*ve[1]+Ns[2]*ve[2]+Ns[3]*ve[3]
				Veta = Neta[0]*ve[0]+Neta[1]*ve[1]+Neta[2]*ve[2]+Neta[3]*ve[3]
				Ux   = (Yeta[coefficient_index]*Us-Ys[coefficient_index]*Ueta)/Jacobian[coefficient_index]
				Vx   = (Yeta[coefficient_index]*Vs-Ys[coefficient_index]*Veta)/Jacobian[coefficient_index]
				# for J-2 calculation
				Uy   = (-Xeta[coefficient_index]*Us+Xs[coefficient_index]*Ueta)/Jacobian[coefficient_index]
				Vy   = (-Xeta[coefficient_index]*Vs+Xs[coefficient_index]*Veta)/Jacobian[coefficient_index]
				# print '(e11 %s, du/dx %s)'%(temp_e11, Ux)
				# print '(e22 %s, dv/dy %s)'%(temp_e22, Vy)
				# print '(e12 %s, (du/dy+dv/dx) %s)'%(temp_e12, (Vx+Uy))
				temp_coeff         = q_coefficient[coefficient_index]
				# temp_J           = (temp_s11*temp_coeff[0]+temp_s12*temp_coeff[1])*temp_e11-tempE_density*temp_coeff[0]
				temp_J             = (temp_s11*Ux+temp_s12*Vx-tempE_density)*temp_coeff[1] +(temp_s22*Vx+temp_s12*Ux)*temp_coeff[2]
				temp_J2            = (temp_s11*Uy+temp_s12*Vy)*temp_coeff[1] +(temp_s22*Vy+temp_s12*Uy-tempE_density)*temp_coeff[2]
				J1                 = J1 + temp_J*dA[coefficient_index]
				J2                 = J2 + temp_J2*dA[coefficient_index]
				coefficient_index += 1
			frame_J = 'Frame%s, J1 = %.3f, J2 = %.3f\n'%(frame_num,J1,J2)
			f_n.append(frame_num)
			J1_values.append(J1)
			J2_values.append(J2)
			#tip.append(tipPosition)
			print frame_J
		frame_num += 1
	return (f_n,J1_values,J2_values)

def initiation_tip(odbName,stepName):
	# This code calculate the total reaction force acting on RVE 
	#during displacement control
	# import re
	# from odbAccess import *
	# initialization of modulus name
	#        =------------default---------------- -= #
	# filePath     = '**'
	# odbName = 'reload_3.odb'
	# stepName = 'Step-2'
	assemblyName = 'PART-1-1'
	# crack_length = 0
	#objective sets
	ob_set = 'cohesive_layer'
	mylabel = []
	#crack_tip = []
	# Open odb file
	odb = openOdb(path = odbName+'.odb')
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
	initiation_frame=[]
	initiation_tipPosition = []
	frame_num = 0
	x_temp = 0
	for frame in Frames:
	#for frame_num in range(0,len(Frames),interval):
	# get field-output
		Damage_coefficient = frame.fieldOutputs['SDEG']
	# Get the tip position
		for label in mylabel:
				# print val.data
			if Damage_coefficient.getSubset(region = myInstance.getElementFromLabel(label)).values[0].data > 0.9999:
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
	#----------20160831 delete for not export multiple file----------#
	# newfilePath='%s_%s_initiationCrack.txt'%(odbName,stepName)
	# newfile=open(newfilePath,'w')
	# newfile.writelines('frame No., tipPosition:\n')
	#----------20160831 delete for not export multiple file----------#
	index = 0
	for num in propagation_frameNo:
		if (num-previous_frame)> 5:# number of frame difference can be changed
			#crack_initiation_frame.append(num)
			#crackAdvance.append(tipPosition[index])
			initiation_frame.append(num)
			initiation_tipPosition.append(tipPosition[index])
			#----------20160831 delete for not export multiple file----------#
			# newfile.writelines('%6d, %6.2f\n'%(num, tipPosition[index]))
			#----------20160831 delete for not export multiple file----------#
		previous_frame = num
		index+=1
	# newfile.close()
	return (initiation_frame,initiation_tipPosition)


#------------MAIN PY--------------#
import re
#		----------redirect to working directory-----------		#
# import os
# os.chdir(r"Z:\\Users\\zehaiwang\\GitHub\\Abaqus_postProcessing\\J_integral") 
# from geometricalSet import Geometrical_set
# from integralCal import integralCal
from odbAccess import *
from math import sqrt

Den_hard = 0.4
Den_trans = 0.1

NumofRealization = 3

for trail in range(NumofRealization):

	odbName  = 'Hetero_%02d_%02d_trail%02d'%(Den_hard*100, Den_trans*100, trail)
	odb = openOdb(path = odbName+'.odb')
	integralSet = 'non_cohesive'
	stepName = 'Step-2'
	# frame output setting
	# num1 start frame 
	num1 = 12
	num2 = 12
	interval = 1
	# manually assign the crack tip at x=0
	tipPosition = 0 
	integralcenter_x = 25
	r1 = 5 # tip from inner radius
	T = 12 # ring thickness
	initiation_frame,tip_x = initiation_tip(odbName,stepName)
	newfilePath='%s_%s_J_integral.txt'%(odbName,stepName)
	newfile=open(newfilePath,'w')
	newfile.writelines('%6s, %6s, %6s:\n'%('frameNo.','J1','J2'))
	# loop over integr
		# newfile.writelines('for integ_x %s:\n'%integralcenter_x)
	# def Geometrical_set (odb, center_x, center_y, t1, ringThickness, tipPosition, IntegralSet):
	elementClass,q_coefficient,Xs,Xeta,Ys,Yeta,Jacobian,dA,nodalLabel = Geometrical_set(odb,integralcenter_x,0,r1,T,tipPosition,integralSet)
	# def integralCal(num1,num2,interval,odb,stepName,elementClass,q_coefficient,Xs,Xeta,Ys,Yeta,Jacobian,dA,nodeLabel):
	fn,J1,J2 = integralCal(num1,num2,interval,odb,stepName,elementClass,q_coefficient,Xs,Xeta,Ys,Yeta,Jacobian,dA,nodalLabel,initiation_frame)
	for i in range(len(fn)):
		temp_print ='frame%s, J1=%s, J2=%s'%(fn[i],J1[i],J2[i])
		newfile.writelines('%6d, %6.2f, %6.4f, %6.4f\n'%(fn[i],tip_x[i],J1[i],J2[i]))
	newfile.close()
