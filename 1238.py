tests = int(input())

for i in range(tests):

    words = input().split()
    tam, bigger = 0, ''

    if len(words[0]) < len(words[1]):

        tam = len(words[0])
        bigger = words[1]

    else:
        tam = len(words[1])
        bigger = words[0]

    final = ''

    for j in range(tam):

        final += words[0][j] + words[1][j]

    final += bigger[tam::]

    print(final)