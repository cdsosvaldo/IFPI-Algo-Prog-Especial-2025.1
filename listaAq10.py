#10. Cálculo do juros simples
#Escreva um programa que calcule o montante final em uma aplicação financeira com juros simples.

#entrada
valor = int(input('Insira o valor (R$): '))
juros = int(input('Insira o valor da taxa(%): '))
parcelas = int(input('Número de parcelas: '))

#processamento
calculo = valor * (juros / 100)  * parcelas
resultado = valor + calculo

#saída
print (f'O valor final é R${resultado}')