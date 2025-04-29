#1. Média Ponderada. Escreva um programa que calcule a média ponderada de três notas, 
# considerando seus respectivos pesos.

#entrada
nota1 = float(input('Informe a nota 1: '))
peso1 = int(input('Informe o peso: '))
nota2 = float(input('Informe a nota 2: '))
peso2 = int(input('Informe o peso: '))
nota3 = float(input('Informe a nota 3: '))
peso3 = int(input('Informe o peso: '))

#processamento
soma = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
soma_peso = peso1 + peso2 + peso3
divisao = soma / soma_peso

print ('-' * 20)
print (f'A sua média é: {divisao:.1f}')
print ('-' * 20)