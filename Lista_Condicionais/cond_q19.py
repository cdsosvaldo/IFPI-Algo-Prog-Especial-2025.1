def main():


    altura = float(input("Informe sua altura (em metros): "))
    peso = float(input("Informe seu peso (Kg): "))

    imc = peso / (altura ** 2)

    print(f"Seu IMC é: {imc:.2f}")

    if imc < 25:
        print("•Tipo: Peso Normal")
    elif imc >= 25 and imc <= 30:
        print("•Tipo: Obeso")
    else:
        print("•Tipo: Obesidade Mórbida")

main()