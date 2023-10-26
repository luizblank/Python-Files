specialchar = "!@#$%¨&*()^~´`[]{}?<>:\/|.+-=_'"""

file = open("nomes.txt", "r") # Lendo arquivo
newfile = open("newnomes.txt", "a") # Criando um arquivo novo que pode ser lido e editado

for line in file.readlines(): # Para cada linha do arquivo
    for char in line: # Para cada caracter da linha
        if not char.isdigit(): # Se não for um dígito(número) 
            if char not in specialchar: # Se o caracter não estiver dentro da "lista" de caracteres especiais
                newfile.write(char) # Escreve no novo arquivo se atender todas as condições
file.close()
newfile.close()