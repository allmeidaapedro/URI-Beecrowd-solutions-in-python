medal_board = {}

while True:

    try:

     sport = input()
     gold_country = input()
     silver_country = input()
     bronze_country = input()

    except EOFError:
        break

    if gold_country not in medal_board:
        medal_board[gold_country] = [1, 0, 0]

    else:
        medal_board[gold_country][0] += 1

    if silver_country not in medal_board:
        medal_board[silver_country] = [0, 1, 0]

    else:
        medal_board[silver_country][1] += 1

    if bronze_country not in medal_board:
        medal_board[bronze_country] = [0, 0, 1]

    else:
        medal_board[bronze_country][2] += 1

medal_board = sorted(medal_board.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))

print('Quadro de Medalhas')

for country in medal_board:
    print(country[0], *country[1])
