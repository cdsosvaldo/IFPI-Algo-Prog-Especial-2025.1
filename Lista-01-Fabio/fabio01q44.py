#44. Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a 
# quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.

#entrada
latao = float(input('Informe a quantidade (kg): '))

#processamento
cobre = latao * (70 / 100)
zinco = latao % cobre

#saída
print ('O valor informado corresponde a {:.3F} gramas de cobre e {:.3F} gramas de zinco.'.format(cobre, zinco))
