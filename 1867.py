def reduce_number(numbers_to_compare):

    for index, number in enumerate(numbers_to_compare):

        sum = 0

        for algarism in number:

            sum += int(algarism)

        numbers_to_compare[index] = str(sum)

    for number in numbers_to_compare:

        if len(number) > 1:

            reduce_number(numbers_to_compare)

    return numbers_to_compare


while True:

    numbers_to_compare = input().split()

    if numbers_to_compare[0] == '0' and numbers_to_compare[1] == '0':
        break

    values = list(map(int, reduce_number(numbers_to_compare)))

    if values[0] > values[1]:
        print(1)
    elif values[0] < values[1]:
        print(2)
    elif values[0] == values[1]:
        print(0)



















