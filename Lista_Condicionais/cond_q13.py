def main():

    num1 = int(input("Informe um número: "))
    num2 = int(input("Informe o 2º número: "))
    num3 = int(input("Informe o 3º número: "))
    num4 = int(input("Informe o 4º número: "))
    num5 = int(input("Informe o 5º número: "))

    
    maior = num1
    menor = num1

    
    if num2 > maior:
        maior = num2
    if num2 < menor:
        menor = num2

    if num3 > maior:
        maior = num3
    if num3 < menor:
        menor = num3

    if num4 > maior:
        maior = num4
    if num4 < menor:
        menor = num4

    if num5 > maior:
        maior = num5
    if num5 < menor:
        menor = num5

    print(f"•{maior} é o maior número.")
    print(f"•{menor} é o menor número.")


main()