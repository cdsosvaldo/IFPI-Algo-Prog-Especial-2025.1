def main():

    print("•••• Audiência de TV ••••")
    print("[Canais válidos: 2, 4, 5, 7, 10]")

    audiencia_canal = {
        2: 0,
        4: 0,
        5: 0,
        7: 0,
        10: 0
    }
    total_telespectador = 0
    canal = -1 

    while canal != 0:
        
        canal = int(input(">Informe o número do canal [0 para finalizar]: "))

        if canal == 0:
            print("Pesquisa finalizada!")
            break

        if canal not in audiencia_canal:
            print("Canal não registrado! Digite um canal válido.")
            continue

        pe_assistindo = int(input(f">Quantas pessoas estão assistindo a esse canal? "))
            
        audiencia_canal[canal] += pe_assistindo
        total_telespectador += pe_assistindo
    
    print(f'''          ____Resultado____''')

    for c, pessoas in audiencia_canal.items():
        if total_telespectador > 0:
            percentual = (pessoas / total_telespectador) * 100
            print(f"    •Audiência Canal {c}: {percentual:.2f}% ({pessoas} pessoas)")
        else:
            print(f"    •Audiência Canal {c}: 0.00% ({pessoas} pessoas)")

    print(f"    •Total de pessoas que estavam assistindo: {total_telespectador}")
    

main()