#40. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma,
#o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

#entrada
anos = int(input('Há quantos anos você fuma? '))
cigarros_dia = int(input('Quantos cigarros por dia você fuma? '))
preco_carteira = int(input('Qual o valor da carteira de cigarros? '))

#processamento
calculo_dia = cigarros_dia / 20
calculo_dia_cart = calculo_dia * preco_carteira
calculo_anos = calculo_dia_cart * 365
total = calculo_anos * anos

#saída
print ('Você já gastou aproximadamente R$', total)
