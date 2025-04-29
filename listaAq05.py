#5. Troco com notas de 50 e 10
#Escreva um programa que determine a quantidade de notas de 50 e 10 necessárias para um determinado valor.

#entrada
notas = int(input('Informe o total de notas: '))

#processamento
calculo_notas = notas // 50
resto_notas = notas % 50
notas_10 = resto_notas // 10

#saída
print (f'O troco deve ser em "{calculo_notas}" nota(s) de 50 e "{notas_10}" nota(s) de 10.')