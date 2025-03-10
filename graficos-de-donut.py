import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=[10,9])
autos = ["Kia","Toyota","Nissan","Suzuki","Audi"]
vendas = [10.6,15.4,14.3,16.1,9.9]
destacar = (0.2,0,0,0,0)
plt.style.use("ggplot")
plt.title("Vendas de Carros no US")
plt.pie(x=vendas,explode=destacar,labels=autos,autopct='%.2f%%',shadow=True,startangle=22)
plt.axis=('equal')
plt.legend(loc='best')

circle=plt.Circle(xy=(0,0),radius=0.75,facecolor='white')
plt.gca().add_artist(circle)

plt.show()