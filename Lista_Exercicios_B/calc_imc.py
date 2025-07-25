from utils import obter_inteiro_positivo

def main():

    print(">>>>Calculadora de IMC<<<<")

    altura = obter_inteiro_positivo("Digite sua altura (metros): ")
    peso = obter_inteiro_positivo("Digite seu peso (Kg): ")

    imc = calcular_imc(peso, altura)
    tipo = parametros(imc)

    print(f"•Seu IMC é: {imc:.2f}")
    print(f"•Classificação: {tipo}")
    print(">>FIM<<")

    
def calcular_imc(peso: float, altura: float) -> float:
  
    return peso / (altura ** 2)

def parametros(imc: float) -> str:

    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade grau 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade grau 2"
    else: 
        return "Obesidade grau 3"


main()