#45. Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para
#decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o saque. 
#Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor disponíveis 
#fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de notas de R$ 50, de R$ 10, 
#de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria indicar uma nota de R$ 50, três notas
#de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que receba o valor da quantia solicitada e
#retorne a distribuição das notas de acordo com o critério da distribuição ótima.

#entrada
valor = int(input('Informe o valor: '))

#processamento
notas_50 = valor // 50 # para notas de 50
resto_notas_50 = valor % 50 # para notas de 10
notas_10 = resto_notas_50 // 10 # para notas de 10
resto_10 = valor % 10 # para notas de 5
notas_5 = resto_10 // 5 # para notas de 5
resto_notas_5 = valor % 5 # para notas de 1
notas_1 = resto_notas_5 // 1 # para notas de 1


#saída
print ('{} nota(s) de R$50, {} nota(s) de R$10, {} nota(s) de R$5 e {} nota(s) de R$1'.format(notas_50, notas_10, notas_5, notas_1))