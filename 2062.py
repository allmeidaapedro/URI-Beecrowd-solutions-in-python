n = int(input())
words = list(input().split())[:n]

for i, word in enumerate(words):

    if len(word) == 3:

        if 'OB' in word:
            words[i] = 'OBI'

        elif 'UR' in word:
            words[i] = 'URI'

print(*words)

#OUTRA SOLUÇÃO:

loops = int(input())
data = input().split()

final = ''

for word in data:

    if word[:2] in ['OB', 'UR'] and len(word) == 3: #verifica se começa com OB ou UR e se tem tamanho 3
        final += word[:2] + 'I' + '' #elimina a ultima letra e poe 'I', separando com espaço p proxima

    else:
        final += word + ''  #mantém a palavra, apenas separando com espaço para a próxima

print(final[:-1]) #remove o último espaço (fatiamento não conta o último índice


