import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(-np.pi,np.pi,0.01)
S_rr  = -5./4.*np.sin(theta/2)+3./4.*np.sin(3*theta/2)
S_ss  = -3./4.*np.sin(theta/2)-3./4.*np.sin(3*theta/2)
S_sr  = 1./4.*np.cos(theta/2)+3./4.*np.cos(3*theta/2)

pressure = -2.*np.sin(theta/2)/3

sigma_rr, = plt.plot(theta,S_rr,"b",label='$\sigma_{rr}$',linestyle='-')
sigma_tt, = plt.plot(theta,S_ss,"ro",label='$\sigma_{\\theta\\theta}$',linestyle='-')
sigma_rt, = plt.plot(theta,S_sr,"g",label='$\sigma_{r\\theta}$',linestyle='-')
sigma_pressure, = plt.plot(theta,pressure,"k",label='pressure',linestyle='--')
plt.legend()
plt.axis([-np.pi,np.pi,-2.5,2.5])
plt.xlabel('theta (rad)')
plt.ylabel('theta dependent part')
plt.title('Mode II crack tip field')
plt.grid(True)


# find the local maxima
m = (np.diff(np.sign(np.diff(S_ss)))<0).nonzero()[0]+1
n = (np.diff(np.sign(np.diff(S_ss)))>0).nonzero()[0]+1

max_x_norm = theta[m]
max_y_norm = S_ss[m]
min_x_norm = theta[n]
min_y_norm= S_ss[n]
# Adding anotations
plt.annotate('local maxima normal stress \napproximately %d degree'%(max_x_norm/np.pi*180), xy =(max_x_norm, max_y_norm), 
			xytext=(max_x_norm+0.5, max_y_norm+0.7),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
plt.annotate('local macima normal stress \napproximately %d degree'%(min_x_norm/np.pi*180-1), xy =(min_x_norm, min_y_norm), 
			xytext=(min_x_norm-0.5, min_y_norm-0.7),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
# plt.annotate('max pressure', xy =(max_x_pressure, max_y_pressure), xytext=(max_x_pressure+1, max_y_pressure+0.5),
#             arrowprops=dict(facecolor='black', shrink=0.1),
#             )
plt.savefig("test.png")
plt.show()
