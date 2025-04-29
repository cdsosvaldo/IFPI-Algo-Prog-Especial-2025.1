#8. Cálculo do IMC - Escreva um programa que calcule o Índice de Massa Corporal (IMC), dado o peso e a altura.

#entrada
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

#processamento
calculo = altura ** 2
calculo2 = peso / calculo

#saída
print (f'Seu IMC é: {calculo2:.6f}')