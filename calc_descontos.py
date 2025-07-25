def main():

    print(">>>>Calculadora de Descontos<<<<")

    preco_original = obter_inteiro_float("Informe o preço original do produto: R$ ")

    base_desconto = valores_descontos(preco_original)

    eh_aniversariante = obter_boolean("É aniversariante?")
    eh_vip = obter_boolean("É VIP?")

    desconto_adicional = calc_desconto_adicional(eh_vip, eh_aniversariante)
    desconto_total = base_desconto + desconto_adicional

    preco_final = calculo_final(preco_original, desconto_total)
    porcentagem_desconto = desconto_total * 100

    print(f"•Preço original: R$ {preco_original:.2f}")
    print(f"•Desconto total aplicado: {porcentagem_desconto:.2f}%")
    print(f"•Preço final com desconto: R$ {preco_final:.2f}")

def valores_descontos(preco: float) -> float:
    if preco > 500.00:
        return 0.15
    elif 200.00 <= preco <= 500.00:
        return 0.10
    elif 100.00 <= preco <= 199.99:
        return 0.05
    else:
        return 0.00

def calc_desconto_adicional(vip: bool, aniversariante: bool) -> float:
    desconto_adicional = 0.0
    if vip:
        desconto_adicional += 0.05
    if aniversariante:
        desconto_adicional += 0.03
    return desconto_adicional

def calculo_final(preco_original: float, desconto_total: float) -> float:
    desconto = preco_original * desconto_total
    preco_final = preco_original - desconto
    return (preco_final)

def obter_inteiro_float(prompt: str) -> float:
    while True:
        try:
            valor_entrada = input(prompt)
            valor = float(valor_entrada)
            if valor <= 0:
                print("Informe um valor positivo maior que 0.")
            else:
                return valor
        except ValueError:
            print("Inválido! Digite um número válido.")

def obter_boolean(prompt: str) -> bool:
    while True:
        resposta_boolean = input(f"{prompt} (sim/nao): ").lower()
        if resposta_boolean == "sim":
            return True
        elif resposta_boolean == "nao":
            return False
        else:
            print("Inválido! Digite apenas 'sim' ou 'nao'")


main()