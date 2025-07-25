def main():

    n = int(input("Informe um número inteiro: "))

    soma = 0 

    for i in range(1, n + 1): 
        soma = soma + i      

    print(f"A soma dos números é: {soma}")


main()