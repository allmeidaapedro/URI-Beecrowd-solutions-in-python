while True:

    sweepstakes, bet_numbers, maximum_value = map(int, input().split())

    if sweepstakes == bet_numbers == maximum_value == 0:
        break

    drawn_numbers = {}

    for j in range(maximum_value):

        drawn_numbers[j + 1] = 0

    for i in range(sweepstakes):

        bet = list(map(int, input().split()))

        for number in bet:

            drawn_numbers[number] += 1

    drawn_numbers = sorted(drawn_numbers.items(), key=lambda x: x[1])
    drawn_numbers = list(filter(lambda x: x[1] == drawn_numbers[0][1], drawn_numbers))
    less = [x[0] for x in drawn_numbers]

    print(*sorted(less))
