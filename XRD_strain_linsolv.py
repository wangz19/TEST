
import numpy as np
import math

# # compare before and after
# b  = np.array([-0.00386,-0.00255,-0.00326,-0.00172,-0.00244,0])
# db = np.array([0.0025,0.0013,0.0009,0.0009,0.0009,0.003])

# # comparizon after with standard card
guess = 0.001
b  = np.array([-0.00302,0,-0.01038,-0.0547,-0.002155,0])
db = np.array([0.000372,guess,0.0009,0.00074,0.00064,guess])


a = np.mat([[0,0,1,0,0,0],[0.3e1 / 0.7e1,0.4e1 / 0.7e1,0,0,0,0.4e1 / 0.7e1 * math.sqrt(0.3e1)],[0.356829e0,0.475772e0,0.1674e0,0.564425e0,0.488807e0,0.475772e0],[0.3e1 / 0.4e1,0.1e1 / 0.4e1,0,0,0,math.sqrt(0.3e1) / 0.2e1],[0.27e2 / 0.52e2,0.25e2 / 0.52e2,0,0,0,0.15e2 / 0.26e2 * math.sqrt(0.3e1)],[0.170169e0,0.510506e0,0.319326e0,0.807509e0,0.466215e0,0.589481e0]])


# m=np.power(10.0,-10)
# a_add=a+np.eye(a.shape[1])*m
# print a_add

x  = np.linalg.solve(a,b)
dx = np.linalg.solve(a,db)

y = np.mat([[x[0],x[5],x[4]],[x[5],x[1],x[3]],[x[4],x[3],x[2]]])

w,v = np.linalg.eig(y)


print "b is", x

print "db is", dx

print "pricipal strain", w

dilatation_strain = np.array([-0.001,-0.001,0.001,0,0,0])

devitoric_strain = np.array([0,0,0,0.001,0.001,0.001])

# check the result
check = np.dot(a,dilatation_strain)
# check = np.dot(a,devitoric_strain)
print check





# #test matrix order
# b  = np.array([5,11])
# a = np.mat([[3,2],[5,6]],dtype=float)


# x  = np.linalg.solve(a,b)


# print "b is", x
