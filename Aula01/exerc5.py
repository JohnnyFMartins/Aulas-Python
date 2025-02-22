# Numeros Pares em um Intervalo

""" Solicite dois numeros interiros ao usuario
Representando o inicio e o fim de um intervalo
Mostre todos os numeros pares nesse intervalo
(incluindo limite inicial e final, se forem pares) """

num1 = int(input("Digite o 1º Numero: "))
num2 = int(input("Digite o 2º Numero: "))

for resultado in range(num1, num2 + 1):
    if resultado % 2 == 0:
        print(resultado)
  




""" 
for y in range(10):
    print(y)

# range(valor inicial, final, e quanto diminui)
for y in range(10, -1, -1):
    print(y)
    if y == 0:
        print("booom") """