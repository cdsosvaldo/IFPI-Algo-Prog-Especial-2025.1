def main():

    while True:
        numero = int(input("Informe um número: "))
            
        if numero == 0:
            print("Encerrado!")
            break

        if numero < 0:
            print("Informe um número inteiro (0 para sair).")
            continue

        print(f"Número: {numero}")

        divisores = "" 
        divisor = True 

        for i in range(1, numero + 1):
            if numero % i == 0:
                if not divisor:
                    divisores = divisores + ", "
                divisores = divisores + str(i)
                divisor = False
            
        print(f">Divisores: {divisores}")

main()