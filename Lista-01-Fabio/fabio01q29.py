#29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

#entrada
meses = int(input('Informe a quantidade de meses: '))

#processamento
calculo = meses // 12
resto = meses % 12

#saída
print ('{} mês(es) corresponde(m) a {:.0f} ano(s) e {} mês(es)'.format(meses, calculo, resto))