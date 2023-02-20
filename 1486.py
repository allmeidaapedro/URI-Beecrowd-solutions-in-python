def count_sticks(transposed_matrix, minimum_length):

    bigger = 0

    for line in transposed_matrix:

        count = 0

        for i in range(len(line)):

            if line[i] == 1:

                count += 1

            else:

                if count >= minimum_length:

                    bigger += 1

                count = 0

        if count >= minimum_length:

            bigger += 1

    return bigger


while True:

    points, measurements, minimum_length = map(int, input().split())

    if points == measurements == minimum_length == 0:
        break

    vector = []

    for k in range(measurements):

        digits = list(map(int, input().split()))
        vector.append(digits)

    # montando uma transposta da matriz -> i. coluna fixo, variando i. linhas

    transposed_matrix = list(map(list, zip(*vector)))

    sticks = count_sticks(transposed_matrix, minimum_length)

    print(sticks)

