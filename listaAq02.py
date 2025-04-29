#2. Soma dos primeiros N números naturais
#Escreva um programa que calcule a soma dos primeiros N números naturais.

#entrada
naturais = int(input('Informe qualquer número natural: '))

#processamento
calculo = naturais * (naturais + 1)
divisao = calculo // 2

#saída
print ('Resultado =', divisao)