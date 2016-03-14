# function is defining a gaussian distribution parameter

import numpy as np
import matplotlib.pyplot as plt

###--------------parameter
sampleSize = 1000 	#total sample point 
mean_E     = 50. # mean value of modulus

#####----------------------gaussian distribution -------------------#######

mu, sigma = 0, 11.
E_temp    = mean_E + np.random.normal(mu, sigma, sampleSize)
# delete all the nagative value generated
E = np.array ([num for num in E_temp if num > 0])

print "mean value is %.4f with %.4f percent discrepancy" %(np.mean(E), abs(np.mean(E)-mean_E)/mean_E*100)
print "max = %.4f" %max(E)
print "min = %.4f" %min(E)

count, bins, ignored = plt.hist (E, 20, normed = True, align = 'mid')

x   = np.linspace(min(bins),max(bins),1000)
pdf = np.exp( -(x-np.mean(E))**2 /(2 * sigma**2))/np.sqrt(2*np.pi*sigma**2)

plt.plot(x,pdf,linewidth = 2, color = 'r')
plt.axis ([min(E)*.9,max(E)*1.1,0,max(count)*1.2])
plt.show()



#####----------------------gaussian distribution -------------------#######

#####----------------------lognormal distribution -------------------#######
# power_constant = np.log(mean_E)  # to insure mean_value is constant, (mu+(sigma^2)/2)should be constant
# print  power_constant

# mu = power_constant
# count = 0
# for count in range(0,10):
# 	count += 1
# 	mu = mu - 0.2
# 	# mean and standard deviation
# 	sigma = np.sqrt((power_constant-mu)*2.)

# 	s = np.random.lognormal (mu, sigma, sampleSize)

# 	print np.mean(s)
# 	print max(s)
# 	print min(s)

# 	count, bins, ignored = plt.hist (s, 500, normed = True, align = 'mid')

# 	x   = np.linspace(0, 100000, 1000)
# 	pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
# 	        / (x * sigma * np.sqrt(2 * np.pi)))

# 	plt.plot (x, pdf, linewidth = 2)
# 	plt.axis ([0,100000,0,0.0004])
# plt.show()
#####----------------------lognormal distribution -------------------#######