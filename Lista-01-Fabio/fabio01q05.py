#5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

#entrada
numeros = int(input('Digite uma sequência de três números: '))

#processamento
centena = numeros // 100 #para centena
restocen = numeros % 100 #para dezena
dezena = restocen // 10 #para dezena
restodez = numeros % 10 #para unidade
unidade = restodez // 1 #para unidade

soma = centena + dezena + unidade

#saída
print ('A soma dos números é', soma)