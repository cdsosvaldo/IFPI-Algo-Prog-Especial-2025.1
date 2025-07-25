def main():

    num = int(input("Múltiplos - Informe o número: "))
    limite_infer = int(input("Informe o Limite Inferior: "))
    limite_super = int(input("Informe o Limite Superior: "))

    if limite_infer > limite_super:
        print("O Limite Inferior não pode ser maior que o Limite Superior!")
        return

    print(f"Os múltiplos de {num} são:")

    multiplo_valido = 0
        
    if num > 0:
        if limite_infer % num == 0:
            multiplo_valido = limite_infer
        else:
            if num > 0:
                multiplo_valido = (limite_infer // num) * num
                if multiplo_valido < limite_infer:
                    multiplo_valido += num
            else:
                    multiplo_valido = (limite_infer // num) * num
                    if multiplo_valido < limite_infer:
                        multiplo_valido += num
        
    valor = abs(num)

    if limite_infer % valor == 0:
        infer = limite_infer
    else:
        infer = (limite_infer // valor) * valor
        if infer < limite_infer:
            infer += valor

    for multiplo in range(infer, limite_super + 1, valor):
        if num < 0:
            print('>', -multiplo)
        else:
            print('>', multiplo)

main()