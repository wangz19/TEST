import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(-np.pi,np.pi,0.01)
S_11  = -5./4.*np.sin(theta/2)+3./4.*np.sin(3*theta/2)
S_22  = -3./4.*np.sin(theta/2)-3./4.*np.sin(3*theta/2)
S_12  = 1./4.*np.cos(theta/2)+3./4.*np.cos(3*theta/2)

vc = np.array([0.2,0.3,0.4,0.5])
#for plane strain
for v in vc:
	S_33 = (S_11+S_22)*v
	von_mesis= abs((S_11-S_22)**2+(S_22-S_33)**2+(S_11-S_33)**2+6*S_12**2)

	ax = plt.subplot (111, projection='polar')
	VM, = ax.plot(theta,von_mesis,label='v is %.2f'%v,linestyle='--')
	
#             
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=1)
plt.savefig("test.png")
plt.show()
