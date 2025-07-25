def obter_inteiro_positivo(prompt: str) -> float:

    while True:
        try:
            valor = input(prompt)
            valor_entrada = float(valor)
            if valor_entrada <= 0:
                print("Erro! Informe um valor positivo maior que zero.")
            else:
                return valor_entrada
        except ValueError:
            print("Entrada inválida. Informe um número válido.")


