def main():

    print("Jogador 1 - Digite 1")
    print("Jogador 2 - Digite 2")

    p_jogador1 = 0
    p_jogador2 = 0
    partida_finalizada = False

    while not partida_finalizada:
        p_ganhador = int(input("Quem fez o ponto? "))

        if p_ganhador == 1:
            p_jogador1 = p_jogador1 + 1
        elif p_ganhador == 2:
            p_jogador2 = p_jogador2 + 1
        else:
            print("Inválido! Digite apenas 1 ou 2")
            continue

        print(f"•Placar atual: Jogador 1 = {p_jogador1} | Jogador 2 = {p_jogador2}")

        diferenca_pontos = abs(p_jogador1 - p_jogador2)

        if (p_jogador1 >= 21 and diferenca_pontos >= 2) or \
            (p_jogador2 >= 21 and diferenca_pontos >= 2):
            partida_finalizada = True
    

    print("***PARTIDA FINALIZADA***")
    if p_jogador1 > p_jogador2:
        print(f"VENCEDOR -> Jogador 1 | {p_jogador1} a {p_jogador2}")
    else:
        print(f"VENCEDOR -> Jogador 2 | {p_jogador2} a {p_jogador1}")
    
main()