# This function assign Hard and soft particles to the affected area
# hard 40% 80GPa
# soft 60% 6GPa

# transform it into a function to generate the INP file 
# input values are /eta and relization name

#--------------------Input variables-------------------------#
Den_hardParticle = 0.4  # density of hard particle
Den_transform = 0.1  # Particles transformed into bilinear plastic material

import random
import re

myfile_down=open('down.inp','r')
myfile_up=open('up.inp','r')

Hard_element = []
Soft_element = []
Transformed_element = [] #Transformed particle list

# Related to symmetrical assignment of hyterogeneity
Element_up = []      # Element upper side of the model
Element_down = []	#Element lower side of the model

Collumn_NO = 16 # number of collumn
population = range(4800) # number of element in up/down area
# print population

for line in myfile_up:
			# read the node list
			# for y >0, y-2
			# for y <0, y+2
	currentline=list(map(float,line.split(',')))
	for i in range(Collumn_NO):
		Element_up.append(currentline[i])
# print Element_up

for line in myfile_down:
			# read the node list
			# for y >0, y-2
			# for y <0, y+2
	currentline=list(map(float,line.split(',')))
	for i in range(Collumn_NO):
		Element_down.append(currentline[i])
# print Element_down

index = sorted(random.sample(population, int(len(population)*Den_hardParticle)))
# print index
# print len(index)

for i in index:
	Hard_element.append(int(Element_up[i]))
	Hard_element.append(int(Element_down[i]))
# print Hard_element

newfilePath='hard_new.inp'
newfile=open(newfilePath,'w')
for i in range(len(Hard_element)):
	i = i+1
	if i == len(Hard_element):
		temp = '%6d'%Hard_element[i-1]
		newfile.write(temp)
	elif i%Collumn_NO == 0:
		temp = '%6d\n'%Hard_element[i-1]
		newfile.write(temp)
	else:
		temp = '%6d,'%Hard_element[i-1]
		newfile.write(temp)

# All the particle not included in the hard_particle set Z
index_difference = list(set(population).difference(set(index)))

#Select 
# print index_difference
for i in index_difference:
	Soft_element.append(int(Element_up[i]))
	Soft_element.append(int(Element_down[i]))
# print Soft_element
newfilePath='soft_new.inp'
newfile=open(newfilePath,'w')
for i in range(len(Soft_element)):
	i = i+1
	if i == len(Soft_element):
		temp = '%6d'%Soft_element[i-1]
		newfile.write(temp)
	elif i%Collumn_NO == 0:
		temp = '%6d\n'%Soft_element[i-1]
		newfile.write(temp)
	else:
		temp = '%6d,'%Soft_element[i-1]
		newfile.write(temp)


