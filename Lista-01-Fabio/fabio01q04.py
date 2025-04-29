#4. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

#entrada
cotadolar = float(input('Informe a cotação do dólar: '))
qtddolar = int(input('Informe o valor: '))

#processamento
calculo = cotadolar * qtddolar

#saída
print (f'Total: R${calculo}')