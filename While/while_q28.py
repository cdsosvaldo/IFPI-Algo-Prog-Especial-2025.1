import random

def main():
    print(" >>>> Número Secreto <<<< ")
    print("Tente adivinhar o número secreto. Dica: está entre 1 e 100.")

    num_secreto = random.randrange(1, 101) 
    
    tentativas = 0
    
    num_usuario = 0 

    while num_usuario != num_secreto:
            tentativas = tentativas + 1
            num_usuario = int(input("Digite o seu palpite: "))

            if num_usuario < num_secreto:
                print("É maior!")
            elif num_usuario > num_secreto:
                print("É menor!")

    print(f">Você acertou! O número secreto é {num_secreto}!")
    print(f">Você realizou {tentativas} tentativa(s) para acertar.")

main()