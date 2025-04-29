#6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

#entrada
kmh = float(input('Informe a velocidade (km/h): '))

#processamento
calculo = kmh / 3.6

#saída
print (f'A velocidade informada representa {calculo:.2f} m/s.')