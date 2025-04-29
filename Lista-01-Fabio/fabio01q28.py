#28. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele
#corresponde.

#entrada
num_horas = int(input('Informe a quantidade (horas): '))

#processamento
semanas = num_horas // 168
horas = num_horas - (semanas * 168)
dias = horas - 24

#saída
print ('{} = {} semana(s), {} dia(s) e {} hora(s).'.format(num_horas, semanas, dias, horas))