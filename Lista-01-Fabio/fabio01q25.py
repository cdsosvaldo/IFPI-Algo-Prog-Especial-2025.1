#25. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

#entrada
qtd_metros = int(input('Informe o valor (metros): '))

#processamento
km = qtd_metros // 1000
metros = qtd_metros % 1000

#saída
print ('{} metros = {} quilômetro(s) e {:.0f} metro(s)'.format(qtd_metros, km, metros))