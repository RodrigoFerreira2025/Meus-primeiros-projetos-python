
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,2*np.pi,700)
y = np.cos(4*t)

plt.plot(t,y)
plt.title('Grafico do Cosseno')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')

plt.show()

