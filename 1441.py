while True:

    initial = int(input())

    if initial == 0:
        break

    sequence = [initial]

    i = 1

    while True:

        if sequence[i - 1] == 1:
            break

        elif sequence[i - 1] % 2 == 0:
            sequence.append(int(sequence[i - 1] / 2))

        else:
            sequence.append(3 * sequence[i - 1] + 1)

        i += 1

    print(max(sequence))
