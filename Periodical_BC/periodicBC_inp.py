import numpy as np
import matplotlib.pyplot as plt
import re
from User_defined_func import * # import all the user_defined functions

#input variables
data_directory = "/Users/zehaiwang/GitHub/Periodical_BC/" # directory of xy data file
filename       = "node_list"
newfile       = filename+"_new"

txt = open(data_directory+filename+".inp",'r')
print "%r successfully opened:"%filename
newfile = open(data_directory+newfile+".inp",'w')

#seperate two column data in two Thetax2 and Intensity arrays
node_cell = np.empty((0,4))


# read the node list ID and coordinates from node_list
i=0
for line in txt.readlines():
	newfile.write(line)
	# reformat node and coordinates in node_cell
	[nodeID,x,y,z] = [float(i) for i in line.split (', ')]
	# node_cell[i][0]=nodeID
	# node_cell[i][1]=x
	# node_cell[i][2]=y
	# node_cell[i][3]=z
	node_cell = np.append(node_cell,[[nodeID,x,y,z]],axis=0)

# print node_cell [:,0]

# determine the surface position in character coordinates
x_min = min(node_cell[:,1])
x_max = max(node_cell[:,1])

# initialization the surface group
nf = [] # front surface where X is max
nb = []  # back surface where X is min

for i in range(len(node_cell[:,0])):
	if (node_cell[i][1]-x_min)<0.001:			# back surface
		nb.append(node_cell[i][0])
	elif (node_cell[i][1]-x_max)<0.001:			#front surface
		nf.append(node_cell[i][0])

# reform node list in np array
nf = np.array(nf)
nb = np.array(nb)

# pairing nodes in two opposite surface
# where the node number on the two face need not to be equal
# number of pair depend on the min node of the two surface
pair_num = min(len(nb),len(nf))
print pair_num
pair_fb = []	#temp position for front and back surface
for x in np.nditer(nb):
	mindist     = float("inf")  #initialize distance as infinite large
	for y in np.nditer(nf):
		dist = distance(node_cell, x, y)
		if dist< mindist:
			mindist     = dist 	
			nearestpair = (x,y)
	pair_fb.append(nearestpair)

print pair_fb


# print distance(node_cell, nf[1],nb[2])






