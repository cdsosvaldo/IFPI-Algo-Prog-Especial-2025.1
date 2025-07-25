def main():

    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mês: "))
    ano = int(input("Informe o ano: "))

    validador = True

    if dia < 1 or dia > 31:
        validador = False
    elif mes < 1 or mes > 12:
        validador = False
    elif mes in [4, 6, 9, 11]:
        if dia < 1 or dia > 30:
            validador = False   
    elif ano < 1:
        validador = False
        
    if validador:
        print(f"•{dia}/{mes}/{ano} é válida!")
    else:
        print(f"•{dia}/{mes}/{ano} não é válida.")


main()