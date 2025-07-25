def main():
   
    numero = int(input("Informe um número inteiro entre 0 e 100: "))


    if  numero == 2 or numero == 3 or numero == 5 or numero == 7 or \
        numero == 11 or numero == 13 or numero == 17 or numero == 19 or \
        numero == 23 or numero == 29 or numero == 31 or numero == 37 or \
        numero == 41 or numero == 43 or numero == 47 or numero == 53 or \
        numero == 59 or numero == 61 or numero == 67 or numero == 71 or \
        numero == 73 or numero == 79 or numero == 83 or numero == 89 or \
        numero == 97:
        print(f"{numero} é primo!")
    else:
        print(f"{numero} não é primo.")
        

main()