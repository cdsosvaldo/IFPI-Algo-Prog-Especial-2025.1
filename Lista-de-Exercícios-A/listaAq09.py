#9. Cálculo do valor final de um produto com desconto
# Escreva um programa que aplique um desconto percentual sobre um preço inicial.

#entrada
valor = int(input('Informe o valor (R$): '))
desconto = int(input('Informe o desconto (%): '))

#processamento
calculo = valor * (desconto / 100)
resto = valor - calculo

#saída
print (f'Valor do desconto: R${calculo}')
print (f'Valor final: R${resto}')