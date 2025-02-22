# Sistema de dessconto de veiculos
# Solicite o nome e o preço do veiculo
# Se o preço > 80k -> 60% de desconto
# Se o preço > 50k -> 30% de desconto
# Se o preço < 50k -> Não existe desconto
# exibir o valor com o desconto

carro = input("Digite o nome do carro: ")
preco = float(input("Digite o valor do carro: "))
desconto = 0


if preco > 80.000:
    desconto = 0.6
elif preco > 50.000 < 80.000:
    desconto =  0.3
    
print("Carro: ",carro)
if preco < 50.000:
    print("Sem desconto")
else:
    print ("Desconto:",desconto * 100,"%")
print("Valor a pagar: R$", preco - (preco * desconto))