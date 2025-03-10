import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

#Criando Dados

x = 0.6 + np.arange(6)
y = [4.9,5.6,3.6,6.6,2.7,3.1]

#plot
fig,ax = plt.subplots()

ax.stem(x,y)
ax.set(xlim=(0, 9), xticks=np.arange(1, 8),
       ylim=(0, 9), yticks=np.arange(1, 8))

plt.show()