def main():

    dia_atual = int(input("Informe o dia atual: "))
    mes_atual = int(input("Informe o mês atual: "))
    ano_atual = int(input("Informe o ano atual: "))

    dia_nasci = int(input("Informe o dia de nascimento: "))
    mes_nasci = int(input("Informe o mês de nascimento: "))
    ano_nasci = int(input("Informe o ano de nascimento: "))

    idade_anos = ano_atual - ano_nasci
    idade_meses = mes_atual - mes_nasci
    idade_dias = dia_atual - dia_nasci

    if idade_dias < 0:
        idade_meses = idade_meses - 1
        if mes_atual == 1: 
            idade_dias = idade_dias + 31
        elif mes_atual == 2 or mes_atual == 4 or mes_atual == 6 or \
                mes_atual == 8 or mes_atual == 9 or mes_atual == 11:
            idade_dias = idade_dias + 31
        else:
            idade_dias = idade_dias + 30
        
    if idade_meses < 0:
        idade_anos = idade_anos - 1
        idade_meses = idade_meses + 12
        
    print(f''' 
    As datas informadas correspondem a:
    {idade_anos} ano(s) 
    {idade_meses} mês(es) 
    {idade_dias} dia(s).
    ''')

main()