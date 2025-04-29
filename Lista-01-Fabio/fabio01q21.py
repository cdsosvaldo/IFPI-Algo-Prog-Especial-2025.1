#21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

#entrada
fahrenheit = float(input('Informe a temperatura (°F): '))

#processamento
calculo = (fahrenheit - 32) / 9 * 5

#saída
print ((f'A temperatura informada corresponde a {calculo:.1f}°C'))