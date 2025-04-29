#32. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

#entrada
numeros = int(input('Número: '))

#processamento
centena = numeros // 100
resto = numeros % 100
dezena = resto // 10
unidade = resto % 10

inverso = unidade*100 + dezena*10 + centena

soma = numeros + inverso

#saida
#print (f'C = {centena}')
#print (f'D = {dezena}')
#print (f'U = {unidade}')

print (numeros, inverso, soma,)