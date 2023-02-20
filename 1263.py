#verificar em uma phrase o numero de alliterations
#repeticao da letra inicial em phrases consecutivas

while True:

    try:

        phrase = input().lower().split()

    except EOFError:
        break

    alliterations = y = 0  # sera o contador do numero de alliterations e y sera 0 quando for diferente para começar outra analise

    for i, v in enumerate(phrase):

        phrase[i] = v[0] # reformando a lista "phrase": cada elemento vai receber sua primeira letra apenas agora

        if phrase[i] == phrase[i - 1] and y == 0:  # para verificacao de consecutivos em listas, usar [i] == [i - example] (nao dara o erro de indexacao na lista)

            y = 1
            alliterations += 1

        elif phrase[i] != phrase[i - 1]:

            y = 0

    print(alliterations)