while True:
    number = input("Insira um número maior que zero: ") # Input sem conversão para pegar o número como string

    try:
        if int(number) > 0 and number.isdigit(): # Verificando se o número é maior que 0 (usando conversão)
            newnumber = 0;                       # e se ele é realmente é um número
            
            for digit in number: # Para cada digito na string
                newnumber = newnumber + int(digit)
                
            print("A soma dos algarismos é igual a", newnumber)
            
            break # Quebrando o while
        
        else:
            raise Exception # Criando um exception caso não atenda as condições do if
    
    except:
        print("Número inválido! Tente novamente.\n")
    