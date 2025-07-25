def main():

    numero = float(input("Digite um número: "))

    if numero <= 0:
        print("Inválido! Digite um número positivo.")
        return

    resultado = dividir_menor_um(numero)

    print(f"Última divisão efetuada - Resultado: {resultado:.4f}")

def dividir_menor_um(numero_inicial):
    if numero_inicial <= 0:
        return None 

    resultado_atual = float(numero_inicial)

    while resultado_atual >= 1:
        resultado_atual = resultado_atual / 2

    return resultado_atual


main()