#35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. 
# Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

#entrada
numeros = int(input('Digite uma sequência de quatro números: '))

#processamento
milhar = numeros // 1000
resto_milhar = numeros % 1000
centena = resto_milhar // 100
resto_centena = numeros % 100
dezena = resto_centena // 10
resto_dez = numeros % 10
unidade = resto_dez // 1

soma = milhar + centena + dezena + unidade

#saída
print ('{} + {} + {} + {} = {}'.format (milhar, centena, dezena, unidade, soma))