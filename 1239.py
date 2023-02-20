while True:

    try:

        line = [x for x in input()]

    except EOFError:
        break

    und, ast = 0, 0

    for i, character in enumerate(line):

        if character == '_':
            und += 1

            if und == 1:
                line[i] = '<i>'

            elif und == 2:
                line[i] = '</i>'
                und = 0

        elif character == '*':
            ast += 1

            if ast == 1:
                line[i] = '<b>'

            elif ast == 2:
                line[i] = '</b>'
                ast = 0

    print(''.join(line))
