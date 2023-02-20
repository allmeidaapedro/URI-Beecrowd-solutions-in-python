while True:

    try:
        number = input()

    except EOFError:
        break

    algarism_frequency = {}

    for algarism in number:

        if algarism not in algarism_frequency:
            algarism_frequency[algarism] = 1

        else:
            algarism_frequency[algarism] += 1

    algarism_frequency = sorted(algarism_frequency.items(), key=lambda x: x[1], reverse=True)
    algarism_frequency = list(filter(lambda x: x[1] == algarism_frequency[0][1], algarism_frequency))

    if len(algarism_frequency) == 1:

        print(algarism_frequency[0][0])

    else:

        algarism_frequency = sorted(algarism_frequency, key=lambda x: int(x[0]), reverse=True)
        print(algarism_frequency[0][0])

