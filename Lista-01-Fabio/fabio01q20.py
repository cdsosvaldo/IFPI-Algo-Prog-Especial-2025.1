#20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

#entrada
celcius = float(input('Informe a temperatura (°C): '))

#processamento
calculo = (celcius * 1.8) + 32

#saída
print (f'A temperatura informada corresponde a {calculo:.1f}°F')