import math
print('=' * 50, 'EQUAÇÃO QUADRÁTICA', '=' * 50)

print('Digite os coeficientes abaixo:')

def perg_coef():
    while True:
        try:
            a1 = float(input('A = '))
        except ValueError:
            print('Digite um número válido!')
            continue
        if a1 == 0:
            print('O coeficiente A não pode ser igual a zero.')
            continue
        break

    while True:
        try:
            b1 = float(input('B = '))
        except ValueError:
            print('Digite um número válido!')
            continue
        break

    while True:
        try:
            c1 = float(input('C = '))
        except ValueError:
            print('Digite um número válido!')
            continue
        break

    dados_ = {
        'a': a1,
        'b': b1,
        'c': c1
    }
    return dados_

def calc(dados):
    delta_ = pow(dados['b'], 2) - 4 * dados['a'] * dados['c']

    if delta_ < 0:
        msg_ = f'A equação não possui raizes reais, pois delta é menor que zero\n delta = {delta_} | (delta < 0)'

        delta_negativo = {
            'delta': delta_,
            'msg': msg_
        }
        return delta_negativo
    elif delta_ == 0:
        msg_ = f'A equação só possui uma raiz real, pois delta é igual a zero\n Delta = {delta_} | (delta = 0)'
        x12_ = (-dados['b']) / (2 * dados['a'])

        x12_msg = {
            'delta': delta_,
            'msg': msg_,
            'x12': x12_
        }
        return x12_msg
    else:
        x1_ = (-dados['b'] + math.sqrt(delta_)) / (2 * dados['a'])
        x2_ = (-dados['b'] - math.sqrt(delta_)) / (2 * dados['a'])

        x1_x2_delta = {
            'delta': delta_,
            'x1': x1_,
            'x2': x2_
        }

        return x1_x2_delta

def resul(calculo):
    if calculo['delta'] > 0:
        print('=' * 50, 'RESULTADOS', '=' * 50)
        print(f'Delta: {calculo['delta']: .2f}')
        print(f'X1: {calculo['x1']: .2f}')
        print(f'X2: {calculo['x2']: .2f}')
    elif calculo['delta'] == 0:
        print('=' * 50, 'RESULTADO', '=' * 50)
        print(calculo['msg'])
        print(f'X1 e X2: {calculo['x12']: .2f}')
    else:
        print('=' * 50, 'RESULTADO', '=' * 50)
        print(calculo['msg'])

dados = perg_coef()
calculo = calc(dados)
resul(calculo)