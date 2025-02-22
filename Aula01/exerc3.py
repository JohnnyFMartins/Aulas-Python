# Calculadora de IMC

""" Solicite o peso em kg e altura do usuario em metros
calcule o IMC (indice de massa corporal)
peso / (altura * Altura)
exibir o IMC """

print("Calculadora de IMC")
peso = float(input("Digite seu peso em Kg:  "))
altura = float(input("Digite sua altura em metros: " ))

imc = peso / (altura * altura)



if imc <= 18.5:
    print("IMC: {:.2f}".format(imc), "( Magreza )")
elif imc > 18.5 and imc < 25:
    print("IMC: ", imc, "( Normal )")
elif imc >= 25 and imc < 30:
    print("IMC: ", imc, "( Sobrepeso )")
elif imc >= 30 and imc < 35:
    print("IMC: ", imc, "( Obesidade grau I )")
elif imc >= 35 and imc < 40:
    print("IMC: ", imc, "( Obesidade grau II )")
else: 
    print("IMC: ", imc, "( Obesidade grau III )")
