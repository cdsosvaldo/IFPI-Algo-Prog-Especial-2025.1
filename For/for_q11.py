def main():

    limite_infer = int(input("Informe o Limite Inferior: "))
    limite_super = int(input("Informe o Limite Superior: "))

    if limite_infer > limite_super:
        print("Limite inferior não pode ser maior que o Limite Superior!")
        return
    
    print(f"Os números primos são:")

    for numero in range(limite_infer, limite_super + 1):
            eh_primo = True
            if numero <= 1:
                eh_primo = False
            elif numero <= 3:
                eh_primo = True
            elif numero % 2 == 0 or numero % 3 == 0:
                eh_primo = False
            else:
                i = 5
            for divisor in range(2, int(numero**0.5) + 1):
                    if numero % divisor == 0:
                        eh_primo = False
                        break
            if eh_primo:
                print('>', numero)

main()