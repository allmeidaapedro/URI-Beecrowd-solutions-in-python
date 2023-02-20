while True:

    number_of_rankings, players_by_ranking = map(int, input().split())

    if number_of_rankings == players_by_ranking == 0:
        break

    players = {}

    for c in range(number_of_rankings):

        weekly_ranking = list(map(int, input().split()))

        for player in weekly_ranking:

            if player not in players:

                players[player] = 1

            else:
                players[player] += 1

    players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    players = list(filter(lambda p: p[1] == players[1][1], players))

    second = [player[0] for player in players]
    second.sort()
    second.append('')

    print(*second)

