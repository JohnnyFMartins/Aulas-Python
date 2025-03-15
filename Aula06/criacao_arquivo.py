import csv

# criar e escrever um arquivo txt
# w -> Write -> Escrita
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome,Idade,Cidade\n")
    arquivo.write("Johnny,30,São Paulo/SP\n")
    arquivo.write("João,23,Jundia/SP\n")
    arquivo.write("Maria,27,Curitiba/PR\n")

# Ler o conteudo
# r -> Read -> Ler
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Conteudo do Arquivo txt:")
    print(arquivo.read())

# Criando arquivo csv
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Carlos", "32", "Santa Isabel"],
    ["Tulio", "53", "Osasco"],
    ["Rafael", "18", "Campinas"]
    
]

# Criar arquivo csv
with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)

# Ler o arquivo csv
with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("n\Conteúdo do arquivo CSV")
    for linha in leitor:
        print(linha)