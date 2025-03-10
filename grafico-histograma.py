import matplotlib.pyplot as plt
import numpy as np

# Dados
plt.figure(figsize=[10,6])
glucose = [52,63,42,85,46,23,75,96]
pacientes = [25,96,45,74,23,29,63,74] # Removido: dados de pacientes não são usados no histograma
plt.hist(glucose, edgecolor='black')  # Correção: removido o argumento 'pacientes
plt.xlabel('Glucose(mg/dL')
plt.ylabel('Pacientes')
plt.title('Medição de Glicose')

plt.show()