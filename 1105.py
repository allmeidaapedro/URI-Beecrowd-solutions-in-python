while True:

    banks, debentures = map(int, input().split())

    if banks == debentures == 0:
        break

    reservations = [int(x) for x in input().split()]
    reservations_dictionary = {}

    for index, reservation in enumerate(reservations):

        reservations_dictionary[str(index + 1)] = reservation

    for j in range(debentures):

        debtor, creditor, value = input().split()

        reservations_dictionary[debtor] -= int(value)
        reservations_dictionary[creditor] += int(value)

    possible = list(filter(lambda x: x[1] < 0, reservations_dictionary.items()))

    if possible == []:
        print('S')
    else:
        print('N')

