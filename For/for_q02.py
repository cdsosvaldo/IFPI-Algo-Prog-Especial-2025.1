def main():

    n = int(input("Digite um número inteiro (maior ou igual a 1): "))

    print(f"Números pares:")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print('>',i)

main()