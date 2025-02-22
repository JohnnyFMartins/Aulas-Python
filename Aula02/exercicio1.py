# Criar novo arquivo
# Desenvolver um sistema que recebe
# Valor de A, Valor de B e Valor de C
# Calcular a Bhaskara
# Delta = b² - 4 * a * c
import math
print("Claculadora de Bhaskara")
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

c = float(input("Digite o valor de C: "))

delta = b**2-4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("▲:",delta,"/ X1:",x1,"/ X2:",x2)
elif delta == 0:
    x = -b  / (2 * a)
    print("▲:",delta,"/ X:",x)
else:
    print("a equação não possui raízes reais.")