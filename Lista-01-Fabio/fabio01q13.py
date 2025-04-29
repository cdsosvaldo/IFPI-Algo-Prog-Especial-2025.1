#13. Leia um valor em real (R$), calcule e escreva 70% deste valor.

#entrada
real = float(input('Insira um valor (R$): '))

#processamento
calculo = real * (70 / 100)
resto = calculo + real

#saída
print (f'70% de R${real} é {calculo:.2f}')