# Oerdem de precedência dos operadores:
# 1 Parênteses
# 2 Potenciação
# 3 Multiplicação / Divisão
# 4 Soma / Subtração
# "Esquerda para direita"

x = y = z = 0

x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))

z = x + y

print('A soma dos dois valores =', z)