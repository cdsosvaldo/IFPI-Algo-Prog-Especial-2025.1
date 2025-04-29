#7. Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

#entrada
numero1 = int(input('Digite um número menor que 10: '))
numero2 = int(input('Digite um segundo número: '))
numero3 = int(input('Digite um terceiro número: '))

#processamento
soma = numero1 + numero2
diferenca = numero2 - numero3


#saída
print (f'A soma dos dois primeiros números é "{soma}" e a diferença dos dois últimos número é "{diferenca}".')