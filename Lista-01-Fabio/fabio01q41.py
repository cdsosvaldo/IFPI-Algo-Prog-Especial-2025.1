#entrada

custo_fabrica = float(input('Custo de fábrica: '))
percentual_impostos = int(input('Impostos: '))
percentual_distribuidor = int(input('Distribuidor: '))

#processamento
impostos = custo_fabrica * (percentual_impostos/100)
distribuidor = (custo_fabrica + impostos) * (percentual_distribuidor/100)

valor_carro = custo_fabrica + impostos + distribuidor

#saida (f-string)
print (f'O valor do carro é R$ {valor_carro: 2f}')
