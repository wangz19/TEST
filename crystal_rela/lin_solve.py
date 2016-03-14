from pNorm_hex import plane_normal_calculation as pc
import numpy as np
import __main__

# giving strain in three lattice plane
def solve_pricipal(st_002,st_210,st_211,st_310):


	b = pc(-0.00386,-0.00255,-0.00326,-0.00172,-0.00244,0)
	db = pc(0.0025,0.0013,0.0009,0.0009,0.0009,0.004)


	a = np.array([[0,0.1e1,0,0,0,0],[0.42857e0,0.57143e0,0,0,0,0.98977e0],[0.35683e0,0.47577e0,0.1674e0,0.56442e0,0.48881e0,0.47577e0],[0.75000e0,0.25000e0,0,0,0,0.86605e0],[0.51923e0,0.48077e0,0,0,0,0.99928e0],[0.17017e0,0.51051e0,0.31933e0,0.80751e0,0.46622e0,0.58948e0]])


	# a = np.array((par_1,par_2,par_3),dtype=float)
	# b = np.array([st_002,st_210,st_310])
	x   = np.linalg.solve(a,b)
	dx  = np.linalg.solve(a,db)

	print x
	print dx

	# check = a3[0]**2*x[0]+a3[1]**2*x[1]+a3[2]**2*x[2]
	# print check
	# if abs((st_211-check)/st_211)<0.05:
	# 	print x,"\ncheck converged"
	# else:
	# 	print x,"\nNOT compatiple with %r discrepancy"%abs((st_211-check)/st_211)

	return x

