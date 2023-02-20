while True:

    try:
        word = input()

    except EOFError:
        break

    characters = []

    for c in word:
        characters.append(c)

    length, spaces = len(word), 0

    while length >= 0:

        print(spaces * ' ', end='')
        print(*characters[:length])

        length -= 1
        spaces += 1