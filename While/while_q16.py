def main():

    s_devedor = 3000.00
    juro_dia_percen = 0.85
    pagamento_dia = 200.00
    dias_uteis = 0

    print(f'''
    •Empréstimo: R$ {s_devedor:.2f}")
    •Taxa de juros/dia: {juro_dia_percen:.2f}%
    •Pagamento diário: R$ {pagamento_dia:.2f}
''')


    while s_devedor > 0:
        dias_uteis = dias_uteis + 1
        juro_do_dia = s_devedor * (juro_dia_percen / 100)
        s_devedor = s_devedor + juro_do_dia

        if pagamento_dia >= s_devedor:
            s_devedor = 0.0
        else:
            s_devedor = s_devedor - pagamento_dia
            
        print(f"Dia {dias_uteis}: Saldo original = R$ {s_devedor + pagamento_dia - juro_do_dia:.2f} | Juros = R$ {juro_do_dia:.2f} | Total = R$ {pagamento_dia:.2f} | Saldo final = R$ {s_devedor:.2f}")

    print(f"**** Resumo ****")
    print(f"Serão necessários {dias_uteis} dias úteis para quitar o empréstimo.")



main()