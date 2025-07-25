def main():

    num_eleitores = int(input("Quantidade de eleitores: "))

    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    votos_nulos = 0
    votos_branco = 0

    print('''
    | Códigos de Votação |
    1, 2, 3 = voto para os candidatos
    9 = voto nulo
    0 = voto em branco
    ''')

    for i in range(1, num_eleitores + 1):
        voto = int(input(f"Eleitor {i}: Digite o código do candidato: "))

        if voto == 1:
            candidato1 = candidato1 + 1
        elif voto == 2:
            candidato2 = candidato2 + 1
        elif voto == 3:
            candidato3 = candidato3 + 1
        elif voto == 9:
            votos_nulos = votos_nulos + 1
        elif voto == 0:
            votos_branco = votos_branco + 1
        else:
            print("Voto inválido!")

    print(F'''
    | Apuração |
    Total de votos para o Candidato 1: > {candidato1}
    Total de votos para o Candidato 2: > {candidato2}
    Total de votos para o Candidato 3: > {candidato3}
    Votos nulos: > {votos_nulos}
    Votos em branco: > {votos_branco}
    ''')

    print("> Vencedor:")

    maior_votos = candidato1
    if candidato2 > maior_votos:
        maior_votos = candidato2
    if candidato3 > maior_votos:
        maior_votos = candidato3

    if maior_votos == 0:
        print("Nenhum candidato recebeu votos válidos!")
    elif (candidato1 == maior_votos and candidato2 == maior_votos) or \
            (candidato1 == maior_votos and candidato3 == maior_votos) or \
            (candidato2 == maior_votos and candidato3 == maior_votos):
        print(">> EMPATE TÉCNICO <<")
    if candidato1 == maior_votos:
        print("•Candidato 1")
    if candidato2 == maior_votos:
        print("•Candidato 2")
    if candidato3 == maior_votos:
        print("•Candidato 3")
    elif candidato1 == maior_votos:
        print("Candidato 1 = VENCEDOR!")
    elif candidato2 == maior_votos:
        print("Candidato 2 - VENCEDOR!")
    else:
        print("Candidato 3 - VENCEDOR!")

main()