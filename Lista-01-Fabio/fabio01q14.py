#14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

#entrada
nota1 = float(input('Informe a nota 1: '))
peso1 = int(input('Informe o peso: '))
nota2 = float(input('Informe a nota 2: '))
peso2 = int(input('Informe o peso: '))
nota3 = float(input('Informe a nota 3: '))
peso3 = int(input('Informe o peso: '))

#processamento
calculo_nota1 = nota1 * peso1
calculo_nota2 = nota2 * peso2
calculo_nota3 = nota3 * peso3

soma_notas = calculo_nota1 + calculo_nota2 + calculo_nota3
soma_pesos = peso1 + peso2 + peso3

divisao = soma_notas / soma_pesos

#saída
print ('Sua média é:', divisao)