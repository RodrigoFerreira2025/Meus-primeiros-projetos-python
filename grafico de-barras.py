import matplotlib .pyplot as plt

#Temperaturas
#cidade_a = [33, 34, 35, 36, 37,38]
#cidade_b = [25,26,27,28,29,30]
#cidade_c = [15,16,17,18,19,20]

cidade_a = [6,3,4,5,8,2]
cidade_b = [2,4,6,7,9,8]
cidade_c = [1,7,8,9,5,6]

datas = [5, 10, 15, 20, 25, 30]

#Criar posições distintas para cada  cidade
#posiçoes_a = list(range(len(datas)))
#posiçoes_b = [pos + 0.25 for pos in posiçoes_a]
#posiçoes_c = [pos +0+50 for pos in posiçoes_a]


plt.bar(datas,cidade_a, color= 'r',label = 'Cidade A')
plt.bar(datas,cidade_b, bottom =cidade_a,color='g',label= 'Cidade B')
plt.bar(datas,cidade_c, bottom=[a + b for a ,b in zip(cidade_a,cidade_b)],color='b',label='Cidade C')



plt.legend()
#plt.xticks(ticks=posiçoes_a,label=datas)
plt.xlabel('Datas')
plt.ylabel('Homicídios')
plt.title('Homicídios nas Cidades em Dias Determinados')
plt.savefig('meu-graficos-barras.png')

plt.show()