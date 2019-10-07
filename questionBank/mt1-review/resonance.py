import numpy as np

R = 500
C = 3.47e-3
L = 7.95

f = 0.5
omega = 2 * np.pi * f

def mag(w, R, L, C):
	numer = w * R * C
	denom = np.sqrt((1 - w**2 * L * C)**2 + (w * R * C)**2)
	return numer / denom

print(mag(omega, R, L, C))