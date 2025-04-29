#11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532; inverso = 235)

#entrada
numeros = int(input('Digite uma sequência de três números: '))

#processamento
centena = numeros // 100 #para centena
restocen = numeros % 100 #para dezena
dezena = restocen // 10 #para dezena
restodez = numeros % 10 #para unidade
unidade = restodez // 1 #para unidade


#saída
print ('O inverso do número informado é: {}{}{}'.format(unidade, dezena, centena))