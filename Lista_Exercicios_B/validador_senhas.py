
def main():

    print(">>>>Validador de Senha<<<<")
    print('''
    Atenção! Sua senha deve conter pelo menos:
    > 8 caracteres
    > uma letra minúscula
    > uma letra maiúscula
    > um caractere especial
    > um número
    ''')

    senha_informada = validacao_senha()
    print("•A senha informada é:", senha_informada)

def tem_minimo(senha: str, tamanho_minimo: int = 8) -> bool:
    return len(senha) >= tamanho_minimo

def tem_minusculo(senha: str) -> bool:
    return any(caractere.islower() for caractere in senha)

def tem_maiusculo(senha: str) -> bool:
    return any(caractere.isupper() for caractere in senha)

def tem_caractere_especial(senha: str) -> bool:
    caracter_especial = "[*!$&?#@%]"
    return (caracter_especial, senha)

def tem_numero(senha: str) -> bool:
    return any(caractere.isdigit() for caractere in senha)

def requisitos(senha: str) -> dict:
    regras = {
        "minimo": tem_minimo(senha),
        "minusculo": tem_minusculo(senha),
        "maiusculo": tem_maiusculo(senha),
        "caractere": tem_caractere_especial(senha),
        "numero": tem_numero(senha)
        
    }
    return regras

def validacao_senha() -> str:
    while True:
        senha = input("Digite sua senha: ")
        validacao = requisitos(senha)

        criterios = all(validacao.values())

        if criterios:
            print("•Senha validada!")
            return senha
        else:
            print("Senha inválida!")
            if not validacao["minimo"]:
                print("> Pelo menos 8 caracteres <")
            if not validacao["minusculo"]:
                print("> Adicione pelo menos uma letra minúscula <")
            if not validacao["maiusculo"]:
                print("> Adicione pelo menos uma letra maiúscula <")
            if not validacao["caractere"]:
                print("> Adicione pelo menos um caractere especial (*, !, $, &, ?, #, @, %) <")
            if not validacao["numero"]:
                print("> Adicione pelo menos um número <")

            
main()