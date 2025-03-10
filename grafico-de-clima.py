from matplotlib import pyplot as plt

eixo_x_dias = [1,5,10,15,20,25,30]
eixo_y_temp_max= [28,29,25,32,34,36,30]
eixo_y_temp_min = [20,21,18,23,23,24,19]

plt.title('Temperatura Maxima e Minima em um Mes')
plt.xlabel('Dias')
plt.ylabel('Temperatura')

plt.bar(eixo_x_dias,eixo_y_temp_max,label='Temp Max')
plt.plot(eixo_x_dias,eixo_y_temp_min,color = 'green',label='Temp Min')
plt.legend(loc='best')
#plt.grid(True)
#plt.axis([1,31,5,45])
plt.xlim([1,31])
plt.ylim([5,50])
print(plt.axis())


#plotar grafico da função,como f(x) = x3 +1
#x = range(1,11,1)
# plt.plot (x,[val**3 + 1 ) for val in x])

plt.show()