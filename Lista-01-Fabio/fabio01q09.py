#9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).

#entrada
numeros = int(input('Digite uma sequência de dois números: '))

#processamento
valor_a = numeros // 10
resto_a = valor_a % numeros

valor_b = (numeros - valor_a) // 10 + 1
resto_b = valor_b % numeros

#saída
print(f'A ordem inversa é {resto_b}{valor_a}')