# this function is suitable for "symmetric_hetero_toughening"
# TO flip the affected_up and affected_down element list with symmetric feature

# Test with Test_raw.inp
# effect to 1,2,3,4
#			5,6,7,8
#			9,10,11,12
# Flip to   9,10,11,12
#			5,6,7,8
#			1,2,3,4

# # ----------------- Example--------------------#
# import random
# import re

# myfile=open('Test_raw.inp','r')

# newfilePath='Test_new.inp'
# newfile=open(newfilePath,'w')

# Collumn_NO = 4 # number of collumn

# Element_raw = [] # element list without flipping

# for line in myfile:
# 			# read the node list
# 			# for y >0, y-2
# 			# for y <0, y+2
# 	currentline=list(map(float,line.split(',')))
# 	for i in range(Collumn_NO):
# 		Element_raw.append(currentline[i])

# print Element_raw

# Row_NO = len(Element_raw)/Collumn_NO

# Element_new = []
# for j in range(Row_NO):
# 	for i in range(Collumn_NO):
# 		Element_new.append(Element_raw.pop(-Collumn_NO+i))
# 	j+=1

# print Element_new

# for i in range(len(Element_new)):
# 	i = i+1
# 	if i == len(Element_new):
# 		temp = '%6d'%Element_new[i-1]
# 		newfile.write(temp)
# 	elif i%Collumn_NO == 0:
# 		temp = '%6d\n'%Element_new[i-1]
# 		newfile.write(temp)
# 	else:
# 		temp = '%6d,'%Element_new[i-1]
# 		newfile.write(temp)

# # ----------------- Code-------------------#

import random
import re

myfile=open('down_raw.inp','r')

newfilePath='Test_new.inp'
newfile=open(newfilePath,'w')

Collumn_NO = 16 # number of collumn

Flip_NO = 48# number of element per line need to be flipped


Element_raw = [] # element list without flipping

for line in myfile:
			# read the node list
			# for y >0, y-2
			# for y <0, y+2
	currentline=list(map(float,line.split(',')))
	for i in range(Collumn_NO):
		Element_raw.append(currentline[i])

print Element_raw


Row_NO = len(Element_raw)/Flip_NO

Element_new = []
for j in range(Row_NO):
	for i in range(Flip_NO):
		Element_new.append(Element_raw.pop(Flip_NO-i-1))
	j+=1

print Element_new

for i in range(len(Element_new)):
	i = i+1
	if i == len(Element_new):
		temp = '%6d'%Element_new[i-1]
		newfile.write(temp)
	elif i%Collumn_NO == 0:
		temp = '%6d\n'%Element_new[i-1]
		newfile.write(temp)
	else:
		temp = '%6d,'%Element_new[i-1]
		newfile.write(temp)

