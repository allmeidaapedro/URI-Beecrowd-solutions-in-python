#operador in em sets -> tempo constante (mais eficiente)
#operador in em listas -> tempo linear (menos eficiente)

# using sets

while True:

    number_of_numbers = int(input())

    if number_of_numbers == 0:
        break

    numbers = list(map(int, input().split()))

    no_pair = set()

    for nmbr in numbers:
        if nmbr in no_pair:
            no_pair.remove(nmbr)
        else:
            no_pair.add(nmbr)

    print(list(no_pair)[0])

# using dictionaries


while True:

    nmbr_of_numbers = int(input())

    if nmbr_of_numbers == 0:
        break

    numbers = list(map(int, input().split()))

    pair_record = dict()

    for nmbr in numbers:
        if nmbr not in pair_record:
            pair_record[nmbr] = 1
        else:
            pair_record[nmbr] += 1

    for nmbr in pair_record:
        if (pair_record[nmbr] % 2) != 0:
            print(nmbr)
            break

