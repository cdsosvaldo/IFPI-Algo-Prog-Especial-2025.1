#8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos

#entrada 
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

#processamento
soma = num1 + num2
diferenca = num1 - num2
divisao = soma / diferenca

#saída
print ('-' * 20)
print ('A soma dos números é: {} \nA diferença é: {} \nA divisão é: {:.2f}'. format(soma, diferenca, divisao))
print ('-' * 20)