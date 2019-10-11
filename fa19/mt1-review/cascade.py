import numpy as np


f = 20

omega = 2 * np.pi * f 

R = 3300
C = 2.41e-6

def mag(w):
	return 1 / np.sqrt(1 + (omega* R * C)**2)

print(mag(omega))