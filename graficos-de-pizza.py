import matplotlib.pyplot as plt
from fontTools.ttLib.woff2 import bboxFormat

# Serie de dados
marcas = ['Ford','Chevrolet','Toyota','Hyundai','Volkwagen']
vendas = [500,600,700,300,100]

explode= [0, 0.1,0,0,0]
cores= ['skyblue','lightgreen', 'coral', 'gold', 'lightpink']
fig = plt.figure(figsize=(9,4)), #Ajustar o tamanho  figura




plt.pie(vendas,
        labels=marcas,
        autopct='%1.1f%%',
        explode=explode,
        shadow=True,
        colors=cores,
        startangle=90)


plt.legend(marcas,title='Marcas',loc='upper right', bbox_to_anchor=(1.6,1))

plt.title('Vendas Anuais de Veiculos por Marca')


plt.show()