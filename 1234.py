while True:
    
    try:
        
        string = input()
        
    except EOFError:
        break
        
    alternator = 0
    
    for character in string:

        if character == ' ':
            print(character, end='') #se for espaço vazio, não muda, apenas repete

        elif alternator == 0:
            print(character.upper(), end='') #alternator alterna de example em example entre maiúsculas e minúsculas, a primeira será sempre maiúscula
            alternator += 1

        else:
            print(character.lower(), end='')
            alternator -= 1  #diminui example a cada loop, promovendo alternância entre maiúsculas e minúsculas

    print()
