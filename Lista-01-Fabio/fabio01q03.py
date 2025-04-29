#3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

#entrada
tempo = int(input('Informe o tempo (em minutos): '))

#processamento
horas = tempo // 60
minutos = tempo % 60

#saída
print (f'{tempo} minutos equivalem a {horas:.0f} hora(s) e {minutos} minuto(s))')