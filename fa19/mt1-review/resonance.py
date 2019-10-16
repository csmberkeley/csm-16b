import numpy as np

R = 500
BW = 8 * 2 * np.pi
center = 10 * 2 * np.pi
L = R / (BW)
C = 1 / (L * (center**2 - (R / (2 * L))**2))

f = 6
omega = 2 * np.pi * f

natural = 1 / np.sqrt(L * C) / 2 / np.pi

RC = R * C
LC = L * C
print("RC: %s" % RC)
print("LC: %s" % LC)

# print("natural frequency: %s" % natural)

def mag(w):
	numer = w * R * C
	denom = np.sqrt((1 - w**2 * L * C)**2 + (w * R * C)**2)
	return numer / denom

def cutoff(R, L, C):
	return -R / (2 * L) + np.sqrt((R / (2 * L))**2 + 1 / (L * C))

def h1(w):
	return w * RC

def h2(w):
	return 1 / np.sqrt((1 - (w**2) * L*C)**2 + (w * R*C)**2)

def h(w):
	return (h1(w) * h2(w))


# omegas = []

# for i in range(1, 20):
# 	omegas.append(mag(i, R, L, C))

# print(omegas)

# print(cutoff(R, L, C))

print("R: %s, L: %s, C: %s" % (R, L, C))



print(mag(omega))

# print(h(60 * np.pi))

