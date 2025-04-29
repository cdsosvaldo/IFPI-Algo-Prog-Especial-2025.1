#23. Leia um valor em kg (quilograma), calcule e escreva o equivalente em g (grama)

#entrada
quilog = float(input('Informe a quantidade (kg): '))

#processamento
calculo = quilog * 1000

#saída
print (f'A quantidade informada aquivale a {calculo:.0f} grama(s).')