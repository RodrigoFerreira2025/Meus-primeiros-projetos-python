import matplotlib.pyplot as plt
import numpy as np

#Inserindo os Dados do Grafico Boxplot
idades = [13,15,17,20,29,14,20,26,74,30,14,20,47,30,45,20,74,62,10,20,29,28]

#Criando o Grafico-Boxplot
plt.boxplot(idades)
plt.ylabel('Idade')
plt.title('Idade dos alunos do Terceiro')


#Exibindo o Grafico-Boxplot

plt.show()


