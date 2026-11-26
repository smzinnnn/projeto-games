Limite = int(input('Limite de Fibonacci: '))

n_2 = 0
n_1 = 1

print(f'\n\n{n_2}\n{n_1}')

while (n_2 + n_1)<=Limite:
    n = n_2 + n_1

    n_2 = n_1
    n_1 = n

    print (n)