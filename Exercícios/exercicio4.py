agenda = {}

def incluirNovoNome(nome):
    agenda[nome] = [] # Adiciona um nome no dicionário com o valor de uma lista vazia
    
def excluirNome(nome):
    agenda.pop(nome) # Apaga aquele nome da agenda
    
def incluirTelefone(nome, telefone):
    agenda[nome].append(telefone) # Adiciona um telefone no final da lista presente dentro do nome
    
def excluirTelefone(nome, telefone):
    if(len(agenda[nome]) <= 1): # Verifica se a lista para aquele nome possui apenas um ou nenhum telefone
        agenda.pop(nome) # Apaga aquele nome da agenda
    else:
        indextel = agenda[nome].index(telefone) # Pegando o index do telefone da lista telefonica de um nome
        agenda[nome].pop(indextel) # Apagando o número da lista
        
def consultarTelefone(nome):
    print("Número(s) de", nome, ":", agenda[nome]) # Printa a lista telefonica daquele nome
    
    
