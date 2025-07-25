
def main():
    id = input('ID: ')
    maior_peso = 0.0
    maior_id = ''
    menor_peso = 1000000
    menor_id = ''
    
    while id != '0':
        peso = float(input('Peso (kg): '))

        if peso > maior_peso:
            maior_peso = peso
            maior_id = id
        
        if peso < menor_peso:
            menor_peso = peso
            menor_id = id



        id = input('ID: ')

    print(f'''
    •Maior peso: {maior_peso}kg
    •ID: {maior_id}
    ------
    •Menor peso: {menor_peso}kg
    •ID: {menor_id} 
''')
  
    print('FIM')


main()