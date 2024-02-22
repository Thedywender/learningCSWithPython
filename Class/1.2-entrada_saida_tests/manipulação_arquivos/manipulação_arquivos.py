with open("arquivo.txt", "w") as file:
    file.write("Maria 45\n")
    file.write("Miguel 33\n")

# escrevendo varias linhas usando a função writelines
    LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
    file.writelines(LINES)

# o file.closed dentro do scopo do open ainda deixa o arquivo aberto
    print(file.closed) 

# somente fora do scopo do open a manipulação é encerrada
print(file.closed)


# para leitura do arquivo se usa a letra r
with open("arquivo.txt", "r") as file:
    for line in file:
        print(line.strip())

# para ler as linhas e retornar em forma de lista se usa o readlines
with open("arquivo.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())