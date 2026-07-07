import matplotlib.pyplot as plt 
from math import sqrt

G = 6.67430*(10**-17)
M = 5.9722*(10**24)


r = []
v = []

r = [r for r in range(1,1500000)]



f_r = lambda r: sqrt((G*M)/r)
v.extend(list(map(f_r,r)))

plt.figure(figsize=(12,6))
plt.plot(r,v)

plt.title("velocidade orbital")
plt.xlabel("distância (km)")
plt.ylabel("velocidade (km/s)")
plt.xlim(0,1500000)
plt.ylim(0,700)
plt.show()

