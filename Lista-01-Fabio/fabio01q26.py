#26. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

#entrada
num_dias = int(input('Informe o número de dias: '))

#processamento
semanas = num_dias // 7
dias = num_dias % 7

#saída
print ('{} dias = {} semana(s) e {} dia(s).'.format(num_dias, semanas, dias))