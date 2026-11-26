

for i in range(3):
    entrada =input('Número: ')

    if entrada.isdecimal():
        num1 = entrada 
        break

    print('\n Tente novamente!')

print(f'\n\n Número: {num1}')
