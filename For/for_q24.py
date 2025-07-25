def main():

    num_habitantes = int(input("Quantidade de participantes? "))

    soma_salarios = 0.0
    soma_filhos = 0
    contador_salario_mil = 0

    for i in range(1, num_habitantes + 1):
        print(f"-> Participante {i}:")

        salario = float(input("Informe o salário (R$): "))
        num_filhos = int(input("Informe a quantidade de filhos: "))

        soma_salarios = soma_salarios + salario
        soma_filhos = soma_filhos + num_filhos

        if salario <= 1000.00:
            contador_salario_mil = contador_salario_mil + 1

    media_salario = soma_salarios / num_habitantes
    media_filhos = soma_filhos / num_habitantes

    if num_habitantes > 0:
        percentual_salario_mil = (contador_salario_mil / num_habitantes) * 100

    print(f'''
            >>> Planilha <<<
•Média de salário da população: R${media_salario:.2f}
•Média de número de filhos: {media_filhos:.2f}
•Percentual de pessoas com salário de até R$1.000,00: {percentual_salario_mil:.2f}%
''')

main()