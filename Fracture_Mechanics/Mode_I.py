import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(-np.pi,np.pi,0.1)
S_rr  = 5./4.*np.cos(theta/2)-1./4.*np.cos(3*theta/2)
S_ss  = 3./4.*np.cos(theta/2)+1./4.*np.cos(3*theta/2)
S_sr  = 1./4.*np.sin(theta/2)+1./4.*np.sin(3*theta/2)

sigma_rr, = plt.plot(theta,S_rr,label='$\sigma_{rr}$',linestyle='--')
sigma_tt, = plt.plot(theta,S_ss,"ro",label='$\sigma_{\\theta\\theta}$',linestyle='-')
sigma_rt, = plt.plot(theta,S_sr,label='$\sigma_{r\\theta}$',linestyle='--')
plt.legend()
plt.axis([-np.pi,np.pi,-2.2,2.2])
plt.xlabel('time (s)')
plt.ylabel('theta dependent part')
plt.title('Mode II crack tip field')
plt.grid(True)
plt.savefig("test.png")
plt.show()
