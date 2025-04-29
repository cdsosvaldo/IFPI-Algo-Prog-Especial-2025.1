#2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

#entrada
horas = int(input('Digite a(s) hora(s): '))
minutos = int(input('Digite o(s) minuto(s): '))

#processamento
calculoh = horas * 60
calculomin = calculoh + minutos

#saída
print (f'O tempo informado corresponde a {calculomin} minutos.')