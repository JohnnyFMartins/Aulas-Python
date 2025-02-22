
palavra = input("Digite a palavra: ").lower().replace(' ','')
if palavra == palavra[::-1]:
    print(palavra,"é um palídromo")
else: print(palavra,"Não é um palídromo")