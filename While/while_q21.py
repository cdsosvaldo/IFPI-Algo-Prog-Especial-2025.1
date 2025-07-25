def main():

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))

    resultado = 0
        
    num1_abs = abs(numero1)
    num2_abs = abs(numero2)

    contador = 0
    while contador < num1_abs:
        resultado = resultado + num2_abs
        contador = contador + 1

    print(f"•Multiplicando {numero1} por {numero2} o resultado é: {resultado}")

main()