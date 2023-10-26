# Classe simples

class NomeCompleto():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def printNomeCompleto(self):
        nomesobrenome = self.nome + " " + self.sobrenome
        print(nomesobrenome)
        
# Uso de loop e manipulação de arquivo

specialchar = "!@#$%¨&*()^~´`[]{}?<>:\/|.+-=_'"""
nomescorrigidos = []

file = open("nomes.txt", "r") # Lendo arquivo'
newfile = open("nomesCorretos.txt", "w") # Criando um arquivo novo que pode ser escrito

for line in file.readlines(): # Para cada linha do arquivo
    for char in line: # Para cada caracter da linha
        if not char.isdigit(): # Se não for um dígito(número) 
            if char not in specialchar: # Se o caracter não estiver dentro da "lista" de caracteres especiais
                newfile.write(char) # Escreve no novo arquivo se atender todas as condições

file.close()
newfile.close() # Fechando tudo

newfile = open("nomesCorretos.txt", "r") # Abrindo novamente o arquivo, mas para leitura dessa vez

for line in newfile.readlines():
    nomescorrigidos.append(line) # Adicionando cada linha do arquivo à lista "nomesCorrigidos" (as linhas vão manter o "\n" no final da string)

newfile.close()      

# Atribuindo valores a classe e manipulando strings

for i in range(len(nomescorrigidos)): # Equivalente em c: for(int i = 0; i < sizeof(nomescorrigidos); i++)
    nomescorrigidos[i] = nomescorrigidos[i].title().split(" ", 1) # Vai separar o nome completo a partir do primeiro espaçamento e 
                                                          # atribuir a lista gerada pelo split ao mesmo índice
    
# Depois do split, a lista vai seguir esse padrão: nomesCorrigidos = [["Joao", "Vitor"], ["Matheus", "Silva"], ["Carolina", "Meire"]]

nome1 = NomeCompleto(nomescorrigidos[0][0], nomescorrigidos[0][1]) # Atribuindo os valores da lista a variávies utilizando a classe
nome2 = NomeCompleto(nomescorrigidos[1][0], nomescorrigidos[1][1])
nome3 = NomeCompleto(nomescorrigidos[2][0], nomescorrigidos[2][1])

print("Nome1:", nome1.nome)
print("Sobrenome1:", nome1.sobrenome)

nome2.printNomeCompleto() # Usando a função da classe de printar o nome completo



# Espero que isso aqui ajude de alguma forma, talvez fique meio complicadinho de entender 
# algumas coisas, mas to aqui caso queira tirar qualquer dúvida, te amo muito <3