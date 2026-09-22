import math
print('=' * 50, 'EQUAÇÃO QUADRÁTICA', '=' * 50)

print('Digite os coeficientes abaixo:')

while True:
    try:
        a = float(input('A = '))
    except ValueError:
        print('Digite um número válido!')
        continue
    if a == 0:
        print('O coeficiente A não pode ser igual a zero.')
        continue
    break

while True:
    try:
        b = float(input('B = '))
    except ValueError:
        print('Digite um número válido!')
        continue
    break

while True:
    try:
        c = float(input('C = '))
    except ValueError:
        print('Digite um número válido!')
        continue
    break

delta = pow(b, 2) - 4 * a * b * c

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - (delta)) / (2 * a)

print(f'X1: {x1: .4f}')
print(f'X2: {x2: .4f}')