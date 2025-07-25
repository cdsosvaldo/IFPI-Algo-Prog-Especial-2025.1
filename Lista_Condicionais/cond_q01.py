def main():

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    numero3 = int(input("Informe o terceiro número: "))


    if numero1 == numero2 and numero2 == numero3:
        print("Existem 3 números iguais.")
    elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        print("Existem 2 números iguais.")
    else:
        print("Não existem números iguais.")


main()