def main():

    hora_inicio = int(input("Informe o horário de início: "))
    minuto_inicio = int(input("Informe o(s) minuto(s) de início: "))

    hora_fim = int(input("Informe o horário do final: "))
    minuto_fim = int(input("Informe o(s) minuto(s) do final: "))

    duracao_h = 0
    duracao_min = 0

    total_min_inicio = hora_inicio * 60 + minuto_inicio
    total_min_fim = hora_fim * 60 + minuto_fim

    if total_min_fim >= total_min_inicio:
        diferenca_min = total_min_fim - total_min_inicio
        duracao_h = diferenca_min // 60
        duracao_min = diferenca_min % 60
    else:
        min_restantes_dia = (24 * 60) - total_min_inicio
        diferenca_min = min_restantes_dia + total_min_fim
        duracao_h = diferenca_min // 60
        duracao_min = diferenca_min % 60

    print(f"•Duração do jogo: {duracao_h} hora(s) e {duracao_min} minuto(s).")


main()