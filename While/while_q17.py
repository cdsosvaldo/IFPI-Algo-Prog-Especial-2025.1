def main():

    mais_alta_nome = ""
    mais_alta_altura = 0.0

    mais_baixa_nome = ""
    mais_baixa_altura = float('inf')

    mais_gorda_nome = ""
    mais_gorda_peso = 0.0

    mais_magra_nome = ""
    mais_magra_peso = float('inf')

    primeira_candidata_lida = False

    while True:
            nome_candidata = input(">Nome da candidata ('FIM' para finalizar): ")

            if nome_candidata.upper() == 'FIM':
                print("Programa encerrado!")
                break

            altura = float(input(">Altura da candidata (em metros): "))

            peso = float(input(">Peso da candidata (Kg): "))

            if not primeira_candidata_lida:
                mais_alta_nome = nome_candidata
                mais_alta_altura = altura
                mais_baixa_nome = nome_candidata
                mais_baixa_altura = altura
                
                mais_gorda_nome = nome_candidata
                mais_gorda_peso = peso
                mais_magra_nome = nome_candidata
                mais_magra_peso = peso
                
                primeira_candidata_lida = True
            else:
                if altura > mais_alta_altura:
                    mais_alta_altura = altura
                    mais_alta_nome = nome_candidata
                
                if altura < mais_baixa_altura:
                    mais_baixa_altura = altura
                    mais_baixa_nome = nome_candidata
                
                if peso > mais_gorda_peso:
                    mais_gorda_peso = peso
                    mais_gorda_nome = nome_candidata
                
                if peso < mais_magra_peso:
                    mais_magra_peso = peso
                    mais_magra_nome = nome_candidata

    print(f'''
    **** Resultado ****
  
    •Por peso:
    Candidata mais magra: {mais_magra_nome} ({mais_magra_peso:.2f} kg)
    Candidata mais gorda: {mais_gorda_nome} ({mais_gorda_peso:.2f} kg)

    •Por altura:
    Candidata mais alta: {mais_alta_nome} ({mais_alta_altura:.2f} m)
    Candidata mais baixa: {mais_baixa_nome} ({mais_baixa_altura:.2f} m)


    ''')


main()