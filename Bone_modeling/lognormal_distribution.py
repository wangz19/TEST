# function is defining a lognormal distribution parameter

import numpy as np
import matplotlib.pyplot as plt

###--------------parameter
sampleSize = 10000 	#total sample point 
mean_E     = 5.8  # mean value of modulus

power_constant = np.log(mean_E)  # to insure mean_value is constant, (mu+(sigma^2)/2)should be constant
print  power_constant

mu = power_constant
count = 0
for count in range(0,10):
	count += 1
	mu = mu - 0.2
	# mean and standard deviation
	sigma = np.sqrt((power_constant-mu)*2.)

	s = np.random.lognormal (mu, sigma, sampleSize)

	print np.mean(s)
	print max(s)
	print min(s)

	count, bins, ignored = plt.hist (s, 500, normed = True, align = 'mid')

	x   = np.linspace(0, 100000, 1000)
	pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
	        / (x * sigma * np.sqrt(2 * np.pi)))

	plt.plot (x, pdf, linewidth = 2)
	plt.axis ([0,100000,0,0.0004])
plt.show()