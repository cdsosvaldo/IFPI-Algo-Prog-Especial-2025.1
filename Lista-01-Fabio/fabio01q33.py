#33. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
#(Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

#entrada
numeros = int(input('Digite uma sequência de três números: '))

#processamento
centena = numeros // 100 #para centena
restocen = numeros % 100 #para dezena
dezena = restocen // 10 #para dezena
restodez = numeros % 10 #para unidade
unidade = restodez // 1 #para unidade
soma = numeros

#saída
print ('O inverso do número informado é: {}{}{}'.format(unidade, dezena, centena))
print ('A soma dos valores é:', soma)

#PARA CONCLUIR