def main():

    numero = int(input("Fatorial - Digite um número inteiro: "))

    if numero == 0 or numero == 1:
        fatorial = 1
    else:
        fatorial = 1 
        for i in range(2, numero + 1): 
            fatorial = fatorial * i 

    print(f"Fatorial de {numero} é: {fatorial}")

main()