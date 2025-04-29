#7. Cálculo do número de latas de tinta - Escreva um programa que calcule quantas 
# latas de tinta são necessárias para pintar uma área.

#entrada
altura = int(input('Informe a altura: '))
largura = int(input('Informe a largura: '))

#processamento
calculo = altura / largura

#saida
print (f'Você vai precisar de {calculo} lata(s) de tinta')