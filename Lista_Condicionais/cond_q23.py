def main():
        
    dia1 = int(input("Data 1 - Informe o dia: "))
    mes1 = int(input("Data 1 - Informe o mês: "))
    ano1 = int(input("Data 1 - Informe o ano: "))

    dia2 = int(input("Data 2 - Informe o dia: "))
    mes2 = int(input("Data 2 - Informe o mês: "))
    ano2 = int(input("Data 2 - Informe o ano: "))

    if ano1 > ano2:
        print(f">{dia1}/{mes1}/{ano1} é a data mais recente.")
    elif ano2 > ano1:
        print(f">{dia2}/{mes2}/{ano2} é a data mais recente.")
    else:
        if mes1 > mes2:
            print(f">{dia1}/{mes1}/{ano1} é a data mais recente.")
        elif mes2 > mes1:
            print(f">{dia2}/{mes2}/{ano2} é a data mais recente.")
        else:
            if dia1 > dia2:
                print(f">{dia1}/{mes1}/{ano1} é a data mais recente.")
            else: 
                dia2 > dia1
                print(f">{dia2}/{mes2}/{ano2} é a data mais recente.")
                


main()