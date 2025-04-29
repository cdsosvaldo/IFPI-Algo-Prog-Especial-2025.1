#27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos
#segundos ele corresponde.

#entrada
valor_segundos = int(input('Informe o valor (segundos): '))

#processamento
horas = valor_segundos // 3600 #ok
resto_horas = valor_segundos % 3600
minutos = resto_horas // 60
segundos = resto_horas % 60

#saída
print ('{} segundos = {} hora(s), {} minuto(s) e {} segundo(s)'.format(valor_segundos, horas, minutos, segundos))