import math
import numpy as np


def plane_normal_calculation (h,k,l):

	m = np.array([h,k,l])

	ratio_a_c = 1/0.73

	x = 2*h+k
	y = h+2*k
	z = l*(3/2)*ratio_a_c**2

	a = x/np.sqrt(x**2+y**2+z**2)
	b = y/np.sqrt(x**2+y**2+z**2)
	c = z/np.sqrt(x**2+y**2+z**2)

	n = np.array([a,b,c])

	# print "normal dirction to plane %r is %r" %(m,n)

	return n

