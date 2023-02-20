dd = {'ABC': '2', 'DEF': '3', 'GHI': '4', 'JKL': '5', 'MNO': '6',
      'PQRS': '7', 'TUV': '8', 'WXYZ': '9'}

while True:

    try:
        number = [x for x in input() if x.isalpha() or x.isnumeric() or x == '*' or x == '#']
        number = list(map(lambda c: c.upper() if c.isalpha() else c, number))

    except EOFError:
        break

    for i, character in enumerate(number):
        for k in dd:
            if character.isalpha() and character in k:
                number[i] = dd[k]

    print(''.join(number))


