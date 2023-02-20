while True:

    try:

        n, m = map(int, input().split())

    except EOFError:
        break

    counting = 0

    for i in range(n, m + 1):

        answer = False

        for algarism in str(i):

            if str(i).count(algarism) > 1:

                answer = True

        if answer:

            counting += 1

    print((m - n) - counting + 1)
