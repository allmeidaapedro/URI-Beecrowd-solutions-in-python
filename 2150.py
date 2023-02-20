while True:

    try:

        vowels = input()
        phrase = input()

    except EOFError:
        break

    cont = 0

    for letter in vowels:

        cont += phrase.count(letter)

    print(cont)