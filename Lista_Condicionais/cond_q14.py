def main():

    num1 = int(input("Informe um número: "))
    num2 = int(input("Informe o 2º número: "))
    num3 = int(input("Informe o 3º número: "))
    num4 = int(input("Informe o 4º número: "))
    num5 = int(input("Informe o 5º número: "))


    soma = num1 + num2 + num3 + num4 + num5
    media = soma / 5.0

    print(f"•A média dos números é: {media:.2f}")
    print("•Os números maiores que a média são:")

    if num1 > media:
        print('>',num1)
    if num2 > media:
        print('>',num2)
    if num3 > media:
        print('>',num3)
    if num4 > media:
        print('>',num4)
    if num5 > media:
        print('>',num5)


main()