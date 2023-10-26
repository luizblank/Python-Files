times = ['1_palmeiras', '2_coritiba', '1_corinthias', '3_juventude',
         '2_fluminense', '3_bahia', '1_cuiaba', '2_cascavel', '3_ponte preta',
         '2_parana clube', '3_volta redonda']

# Criando uma lista para cada divisão
primeira = []
segunda = []
terceira = []

for time in times:
    if time[0] == "1":
        newname = time.split("_") # Separando o nome do time da divisão
                                  # (O split cria uma lista assim --> ['1', 'palmeiras'])
                                  
        primeira.append(newname[1].capitalize()) # Pegando o nome do time, formatando e
                                                 # colocando na sua lista própria  
    elif time[0] == "2":
        newname = time.split("_")     
        segunda.append(newname[1].capitalize())
        
    else:
        newname = time.split("_")     
        terceira.append(newname[1].capitalize())
        
print("Primeira divisão:", primeira)
print("Segunda divisão:", segunda)
print("Terceira divisão", terceira)