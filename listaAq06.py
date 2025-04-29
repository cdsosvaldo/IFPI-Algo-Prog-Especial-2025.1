#6. Número invertido de três dígitos - Escreva um programa que receba
# um número de três dígitos e exiba ele invertido.

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