def main():

    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))

    if num1 <= 0 or num2 <= 0:
        print("Inválido! Digite apenas números inteiros positivos.")
        return

    mdc = calcular_mdc(num1, num2)

    print(f">O MDC é: {mdc}")

def calcular_mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


main()