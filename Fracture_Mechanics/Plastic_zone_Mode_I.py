import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(-np.pi,np.pi,0.1)
S_11  = 5./4.*np.cos(theta/2)-1./4.*np.cos(3*theta/2)
S_22  = 3./4.*np.cos(theta/2)+1./4.*np.cos(3*theta/2)
S_12  = 1./4.*np.sin(theta/2)+1./4.*np.sin(3*theta/2)

# for plane strain
v=0.3
S_33 = (S_11+S_22)*v
S_23 =0
S_13 =0

von_mesis= np.sqrt((S_11-S_22)**2+(S_22-S_33)**2+(S_11-S_33)**2+6*(S_12**2+S_23**2+S_13**2))

ax = plt.subplot (111, projection='polar')
VM, = ax.plot(theta,von_mesis,"r",label='Plastic_Zone',linestyle='--')
ax.legend()

plt.savefig("test.png")
plt.show()
