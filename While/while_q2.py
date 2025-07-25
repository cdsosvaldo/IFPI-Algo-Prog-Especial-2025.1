def main():

    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))

    if num1 <= 0 or num2 <= 0:
        print("Inválido! Digite apenas números inteiros positivos.")
        return

    if num1 == 1:
        mmc = num2
    elif num2 == 1:
        mmc = num1
    elif num1 == 0 or num2 == 0:
        mmc = 0
    else:
        mdc_result = calcular_mdc(num1, num2)
        mmc = (num1 * num2) // mdc_result

    print(f">O MDC é: {mmc}")

def calcular_mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


main()