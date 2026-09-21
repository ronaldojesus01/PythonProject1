import math
print('=' * 50, 'EQUAÇÃO QUADRÁTICA', '=' * 50)

print('Digite os coeficientes abaixo:')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

delta = math.sqrt(pow(b, 2) - 4 * a * b * c)
x1 = (-b + (delta)) / (2 * a)
x2 = (-b - (delta)) / (2 * a)

print(f'X1: {x1: .4f}')
print(f'X2: {x2: .4f}')