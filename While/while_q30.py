def main():

    print('''       •••• TABELA DE DESCONTOS ••••
    
    > Até 10 unidades: não possui desconto
    > De 11 a 20 unidades: 10% de desconto
    > De 21 a 50 unidades: 20% de desconto
    > A partir de 50 unidades: 25% de desconto
    ''')

    nome_produto = ""

    while nome_produto.upper() != 'FIM':
            
        nome_produto = input("Informe o nome do produto [FIM para encerrar]: ")

        if nome_produto.upper() == 'FIM':
            print("Processo finalizado!")
            break

        preco_unit = float(input(f"Informe o preço do produto: R$ "))

        qtd = int(input(f"Quantidade: "))
        if qtd <= 0:
            print("Quantidade inválida!")
            continue

        valor_bruto = preco_unit * qtd
        desconto = 0.0
        percentual_dscnto = 0

        if qtd <= 10:
            percentual_dscnto = 0
        elif qtd >= 11 and qtd <= 20:
            desconto = valor_bruto * 0.10
            percentual_dscnto = 10
        elif qtd >= 21 and qtd <= 50:
            desconto = valor_bruto * 0.20
            percentual_dscnto = 20
        else:
            desconto = valor_bruto * 0.25
            percentual_dscnto = 25
            
        total_a_pagar = valor_bruto - desconto

        print(f'''
        •Resumo do Produto: {nome_produto}
        •Preço unitário: R$ {preco_unit:.2f}
        •Quantidade: {qtd}
        •Valor bruto: R$ {valor_bruto:.2f}
        •Desconto aplicado ({percentual_dscnto}%): R$ {desconto:.2f}
        •Total a pagar: R$ {total_a_pagar:.2f}
        ''')

    print(">>>FIM<<<")

main()