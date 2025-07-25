def main():

    print(">Informe a data atual")

    dia_atual = int(input("Dia atual: "))
    mes_atual = int(input("Mês atual: "))
    ano_atual = int(input("Ano atual: "))

    print(">Agora informe a data de nascimento:")

    dia_nasci = int(input("Dia de nascimento: "))
    mes_nasci = int(input("Mês de nascimento: "))
    ano_nasci = int(input("Ano de nascimento: "))

    idade = ano_atual - ano_nasci

    if mes_atual < mes_nasci:
        idade = idade - 1
    elif mes_atual == mes_nasci:
        if dia_atual < dia_nasci:
            idade = idade - 1

    print(f"A idade é: {idade} anos.")

main()