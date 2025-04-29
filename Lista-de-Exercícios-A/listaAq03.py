#03. Cálculo de tempo de viagem
#Escreva um programa que calcule quanto tempo levará uma viagem, dado a distância e a velocidade média.

#entrada
distancia = int(input('Informe a distância (Km): '))
velocidade = int(input('Informe a velocidade: '))

#processamento
calculo = distancia / velocidade

#saída
print (f'O tempo total da viagem será de aproximadamente {calculo} hora(s).')