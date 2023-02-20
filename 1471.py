while True:

    try:

        volunteers_dove, volunteers_returned = map(int, input().split())
        came_back = list(map(int, input().split()))

    except EOFError:
        break

    volunteers = [c + 1 for c in range(volunteers_dove)]

    didnt_came_back = [v for v in volunteers if v not in came_back]
    didnt_came_back.sort()

    if didnt_came_back != []:

        print(*didnt_came_back, '')

    else:

        print('*')

