def main():

    limite_infer = int(input("Informe o Limite Inferior: "))
    limite_super = int(input("Informe o Limite Superior: "))

    if limite_infer > limite_super:
        print("Limite inferior não pode ser maior que o Limite Superior!")
        return

    print(f"Os números pares são:")

    start_for = limite_infer
    if limite_infer % 2 != 0: 
        start_for = limite_infer + 1

    for numero_par in range(start_for, limite_super + 1, 2):
        print('>', numero_par)

main()