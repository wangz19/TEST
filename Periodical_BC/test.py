import numpy as np


m=mdb.models['Model-1']
r=m.rootAssembly
node=r.instances['Part-1-1'].nodes

#ne 存储所有边界上的单元节点的编号 node ID on the edge
nl=[] #node on the left boundary surface
nr=[] #node on the right boundary surface

#reformat the node id, x, y, z postion in an Nx4 array
node_cell =np.zeros((len(node),4)) 
for i in range(len(node)):
    node_cell[i][1]=node[i].coordinates[0]
    node_cell[i][2]=node[i].coordinates[1]
    node_cell[i][3]=node[i].coordinates[2]

print "total node number is", len(node)

x_min = np.min(node_cell[:][1])
x_max = np.max(node_cell[:][1])
y_min = np.min(node_cell[:][2])
y_max = np.max(node_cell[:][2])
z_min = np.min(node_cell[:][3])
z_max = np.max(node_cell[:][3])


# find the left and right surface
for i in range(len(node)):     #找出四个顶点
    x    = node_cell[i][1]
    if abs(x-x_min) < 0.0001:
        nl.append(i)
    elif abs(x-x_max) < 0.0001:
        nr.append(i)

print x_max,x_min