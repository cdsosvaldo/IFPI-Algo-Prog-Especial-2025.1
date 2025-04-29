#29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

#entrada
meses = int(input('Quantidade: '))

#processamento
anos = meses // 12
meses_sobra = meses % 12

#saida
print (f'{meses} meses equivalem a {anos} ano(s) e {meses_sobra} mes(es)')