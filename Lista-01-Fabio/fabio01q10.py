#10. Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.

#entrada
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

#processamento
quociente = num1 // num2
multiplica = num2 * quociente
resto = num1 - multiplica


#saída
print ('O quociente é: {} e o resto é: {}'.format(quociente, resto))