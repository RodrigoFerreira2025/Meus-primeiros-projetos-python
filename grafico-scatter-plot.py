import matplotlib.pyplot as plt
import numpy as np

#Dados:
n = 300
x = np.linspace(0,12,n)
y = x + np.random.rand(n)

#Criando o Grafico Scatter Plot
fig = plt.figure()
ax = fig.add_subplot()
im =ax.scatter(x,y,s=300,alpha=0.5,edgecolors='black')
cbar = fig.colorbar(im)
cbar.set_label('Temperatura (°C)')
ax.set_xlabel('Tempo(min)', fontsize=14)
ax.set_ylabel('Bacterias(metros)', fontsize=14)
ax.grid(alpha = 0.25)

#Exibindo o Grafico Scatter Plot
plt.show()
