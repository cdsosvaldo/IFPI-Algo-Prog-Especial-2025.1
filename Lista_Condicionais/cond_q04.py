def main():

    numero = int(input("Digite um número de dois dígitos: "))

    if 10 <= numero <= 99 or -99 <= numero <= -10:
        if numero >= 10:
            dezena = numero // 10
            unidade = numero % 10  
        else:
            dezena = (numero) // 10
            unidade = (numero) % 10

        if dezena == unidade:
            print(f"O algarismo da dezena ({dezena}) é igual ao algarismo da unidade ({unidade}).")
        else:
            print(f"O algarismo da dezena ({dezena}) é diferente do algarismo da unidade ({unidade}).")

main()