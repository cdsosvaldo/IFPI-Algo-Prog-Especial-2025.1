def main():

    print('''
    •••• PESQUISA ••••
    Sexo: 1=Feminino, 2=Masculino
    Estado Civil: 1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo
    [SAIR para encerrar]
    ''')

    total_pesquisados = 0

    soma_idades_mulher = 0
    total_mulheres = 0
    soma_idades_homem = 0
    total_homem = 0
    total_homem_solt = 0
    total_mulher_solt = 0
    mulher_divor_mais_30 = 0

    flag_sexo = "" 

    while total_pesquisados < 100 and flag_sexo.upper() != 'SAIR':
        
        print(f"\n--- Informações da Pessoa {total_pesquisados + 1} ---")

        flag_sexo = input("Informe o sexo (1=Feminino, 2=Masculino): ")
            
        if flag_sexo.upper() == 'SAIR':
            print("Pesquisa encerrada!")
            break

        sexo = int(flag_sexo)
        if sexo not in [1, 2]:
            print("Sexo inválido! Parâmetro válido: 1 ou 2.")
            continue

        idade = int(input("Digite a idade: "))
        if idade <= 0 or idade > 110:
            print("Idade inválida! Parâmetro válido: entre 1 e 110.")
            continue 

        estado_civil = int(input("Digite o estado civil (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo): "))
        if estado_civil not in [1, 2, 3, 4]:
            print("Estado civil inválido! Parâmetro válido: 1, 2, 3 ou 4.")
            continue 

        total_pesquisados = total_pesquisados + 1

        if sexo == 1:
            soma_idades_homem += + idade
            total_homem += + 1
            if estado_civil == 2:
                total_homem_solt += + 1
        else:
            soma_idades_mulher += + idade
            total_mulheres += + 1
            if estado_civil == 2:
                total_mulher_solt += + 1
            elif estado_civil == 3 and idade > 30:
                mulher_divor_mais_30 += + 1

    print("--- Resultados ---")

    if total_mulheres > 0:
        media_idade_mulher = soma_idades_mulher / total_mulheres
        print(f"Média de idade das mulheres: {media_idade_mulher:.1f} anos")
    else:
        print("Nenhuma mulher foi informada.")

    if total_homem > 0:
        media_idades_homem = soma_idades_homem / total_homem
        print(f"Média de idade dos homens: {media_idades_homem:.1f} anos")
    else:
        print("Nenhum homem foi informado.")

    if total_homem > 0:
        percentual_homem_solt = (total_homem_solt / total_homem) * 100
        print(f"Percentual de homens solteiros: {percentual_homem_solt:.2f}%")
    else:
        print("Nenhum homem foi informado!")

    if total_mulheres > 0:
        percentual_mulher_solt = (total_mulher_solt / total_mulheres) * 100
        print(f"Percentual de mulheres solteiras: {percentual_mulher_solt:.2f}%")
    else:
        print("Nenhuma mulher foi informada!")

    print(f"Quantidade de mulheres divorciadas + 30 anos: {mulher_divor_mais_30}")
    print('>>>FIM<<<')

main()