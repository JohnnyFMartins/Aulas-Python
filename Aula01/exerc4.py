""" Solicite ao usuario para fornecer uma temperatura 
em graus Celsiu e converta para Fahrenheit """


""" tempC = float(input("Digite a temperatura em °C: "))

tempF = tempC * 1.8 + 32

print("{:.2f}".format(tempF), "°F")
 """

print("Conversor de Temperatura")

print("1- Celsius \n2- Fahrenheit \n3- Kelvin")
opcao = int(input("Qual a temperatura que voce deseja converter?: "))

if opcao == 1:
    c = float (input("Digite o valor em °C: "))
elif opcao == 2:
    f = float (input("Digite o valor em °F: "))
elif opcao == 3:
    k = float (input("Digite o valor em K: "))
else:
    print("Opcão invalida")

opcao = int(input("Para qual a temperatura que voce deseja converter?: "))

if opcao == 1:
    print(c)
if opcao == 2:
    f = c * 1.8 + 32
    print("temperatura em °F: ", f)
elif opcao == 3:
    k = c + 273,15
    print("temperatura em K: ", f)
else:
    print("Opcão invalida")

