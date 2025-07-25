def main():

    n = int(input("Digite um número inteiro (maior ou igual a 1): "))

    print(f"Números de 1 a {n}:")
    for i in range(1, n + 1):
        print('>',i)

main()