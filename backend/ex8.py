Duplo_fatorial = int(input('Digite o valor da operação: '))

res = 1

for i in range(Duplo_fatorial, 0, -2):
    res *= i
    print(f'i={1}')


print(res)