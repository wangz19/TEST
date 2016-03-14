import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(-np.pi,np.pi,0.01)
S_11  = 0
S_22  = 0
S_12  = 0
S_13  = np.cos(theta/2)
S_23  = np.sin(theta/2)
#for plane strain
v    = 0.3
S_33 = (S_11+S_22)*v


von_mesis= ((S_11-S_22)**2+(S_22-S_33)**2+(S_11-S_33)**2+6*(S_12**2+S_23**2+S_13**2))

ax = plt.subplot (111, projection='polar')
VM, = ax.plot(theta,von_mesis,"r",label='Plastic_Zone',linestyle='--')
ax.legend()

plt.savefig("test1.png")
plt.show()
