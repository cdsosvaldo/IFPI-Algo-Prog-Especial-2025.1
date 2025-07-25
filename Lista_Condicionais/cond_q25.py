def main():

    senha_fornecida = int(input("Digite a senha: "))
    
    CODIGO = 1234

    if senha_fornecida == CODIGO:
        print(">>> ACESSO PERMITIDO <<<")
    else:
        print(">>> ACESSO NEGADO <<<")


main()