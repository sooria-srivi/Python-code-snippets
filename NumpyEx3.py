import numpy as np
import matplotlib.pyplot as plt
#linspace

a1 = np.linspace(10,20,5)
print(a1)

a1 = np.linspace(10,20,10)
print(a1)

#plot using matplot

x = np.linspace(0,2*np.pi,10)
y = np.sin(x)

#plt.ioff()
plt.plot(x,y)
plt.show()
