import numpy as np
import matplotlib.pyplot as plt
import re

import os
os.chdir(r"Z:\\Users\\zehaiwang\\GitHub\Periodical_BC")   #change to function directory to souce macro_modeing
from User_defined_func import * # import all the user_defined functions


#default
# Assembly_name ='Part-1-1'
#customized
Assembly_name ='Bone_mesh-1'
#MPC
m=mdb.models['Model-1']
r=m.rootAssembly
node=r.instances[Assembly_name].nodes

#ne 存储所有边界上的单元节点的编号 node ID on the edge
nb=[] #node on the back boundary surface x_min
nf=[] #node on the right boundary surface x_max
nl=[] # node on the left boundary surface y_min
nr=[] #node on the right boundary surface y_max

#reformat the node id, x, y, z postion in an Nx4 array
# as shown          1, 0, 0, 0
node_cell =np.zeros((len(node),4)) 
for i in range(len(node)):
    node_cell[i][1]=node[i].coordinates[0]
    node_cell[i][2]=node[i].coordinates[1]
    node_cell[i][3]=node[i].coordinates[2]
    node_cell[i][0]=node[i].label

print node_cell

# determine the surface position in character coordinates
x_min = np.min(node_cell[:,1])
x_max = np.max(node_cell[:,1])
y_min = np.min(node_cell[:,2])
y_max = np.max(node_cell[:,2])
z_min = np.min(node_cell[:,3])
z_max = np.max(node_cell[:,3])

for i in range(len(node_cell[:,0])):
    if abs(node_cell[i][1]-x_min)<0.001:            # back surface
        nb.append(node_cell[i][0])
    if abs(node_cell[i][1]-x_max)<0.001:          #front surface
        nf.append(node_cell[i][0])
    if abs(node_cell[i][2]-y_min)<0.001:          #left surface
        nl.append(node_cell[i][0])
    if abs(node_cell[i][2]-y_max)<0.001:          #right surface
        nr.append(node_cell[i][0])
# print nl
# print nr

def PBC_constrain (node_cell,node_set_1,node_set_2,coefficient_1,coefficient_2,dof_1,dof_2,dof_3,set_name):
    # pairing nodes in two opposite surface
    # where the node number on the two face need not to be equal
    # number of pair depend on the min node of the two surface
    # m=mdb.models['Model-1']
    # r=m.rootAssembly
    # node=r.instances['Part-1-1'].nodes
    # pair_num = min(len(nb),len(nf))
    # print pair_num
    pair = []    #temp position for front and back surface
    for x in node_set_1:
        mindist     = float("inf")  #initialize distance as infinite large
        for y in node_set_2:
            dist = distance(node_cell, x, y)
            if dist< mindist:
                mindist     = dist  
                nearestpair = (int(x),int(y))   # convert float node label into int for future reference
        pair.append(nearestpair)
    print pair
    # loop over the paired two surface and coupled movement on the paired nodes
    # for example, we want to pair the movement of y direction on front and back surface
    for i in range(len(pair)):
        r.Set(nodes=node[pair[i][0]-1:pair[i][0]],name='set_0'+set_name+str(i+1))  #select pair_fb[i][0], here the node should be given in
                                                                                #tuple form, ie nodes= node[0:1],select node[1]
        r.Set(nodes=node[pair[i][1]-1:pair[i][1]],name='set_1'+set_name+str(i+1))
        #Given the MPC on
        if dof_1 == 1:
            m.Equation(name='con_dof_1_'+set_name+str(i+1),terms=((coefficient_1,'set_0'+set_name+str(i+1),1),(coefficient_2,'set_1'+set_name+str(i+1),1)))
        if dof_2 == 1:
            m.Equation(name='con_dof_2_'+set_name+str(i+1),terms=((coefficient_1,'set_0'+set_name+str(i+1),2),(coefficient_2,'set_1'+set_name+str(i+1),2)))
        if dof_2 == 1:
            m.Equation(name='con_dof_3_'+set_name+str(i+1),terms=((coefficient_1,'set_0'+set_name+str(i+1),3),(coefficient_2,'set_1'+set_name+str(i+1),3)))

#def PBC_constrain (node_cell,nb,nf,coefficient_1,coefficient_2,dof_1,dof_2,dof_3):
PBC_constrain (node_cell,nb,nf,-1,1,1,0,0,'fb')
PBC_constrain (node_cell,nr,nl,-1,1,0,1,0,'rl')

