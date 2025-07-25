def main():

    for tabuada in range(1, 11): 
        print(f"\nTabuada de {tabuada}:") 

        for multiplicador in range(1, 11): 
            resultado = tabuada * multiplicador
            print(f"{tabuada} x {multiplicador} = {resultado}")

main()