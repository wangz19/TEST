# modify inp file 
from abaqus import *
from abaqusConstants import *
import __main__

def modinp(filename, modulus_list):

	import numpy as np
	import matplotlib.pyplot as plt

	#input variables
	data_directory= "C:/Temp/Square" # directory of xy data file


	txt = open(data_directory+filename)
	print "%r successfully opened:"%filename

	#seperate two column data in two Thetax2 and Intensity arrays
	eleList = []
	mod_List = modulus_list ## initialize theta and intensity

	for line in txt.readlines():
		thetabyTwos,vals = line.split (" ", 1)
		thetaList.append(float(thetabyTwos))
		intenList.append(float(vals))