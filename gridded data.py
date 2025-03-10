import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

#Make data
X,Y = np.meshgrid(np.linspace(-2,4,257),np.linspace(-2,4,256))
Z = (2 - X/2 + X**6 + Y**3)* np .exp(-X**2 - Y**2)
levels = np.linspace(Z.min(), Z.max(), 8)

#Plot
fig,ax= plt.subplots()

ax.contourf(X,Y,Z,levels=levels)

plt.show()