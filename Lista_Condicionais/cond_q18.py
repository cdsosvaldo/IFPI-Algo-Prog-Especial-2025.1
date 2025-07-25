def main():

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    print('''
    Escolha a operação:
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    ''')
       
    operacao = int(input("Informe o número da operação: "))

    resultado = 0.0

    if operacao == 1:
        resultado = valor1 + valor2
        print(f"Resultado: {valor1} + {valor2} = {resultado:.2f}")
    elif operacao == 2:
        resultado = valor1 - valor2
        print(f"Resultado: {valor1} - {valor2} = {resultado:.2f}")
    elif operacao == 3:
        resultado = valor1 * valor2
        print(f"Resultado: {valor1} * {valor2} = {resultado:.2f}")
    elif operacao == 4:
        if valor2 != 0:
            resultado = valor1 / valor2
            print(f"Resultado: {valor1} / {valor2} = {resultado:.2f}")
    else:
        print("Não é possível dividir por zero!")
  

main()