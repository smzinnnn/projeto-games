fatorial = int(input('Digite o valor da operação: '))

res = 1

for i in range(1, fatorial+1):
    res *= i

print(res)