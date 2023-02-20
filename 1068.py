while True:

    try:

        expr = input()

    except EOFError:
        break

    a = expr.count('(')
    b = expr.count(')')

    if expr[0] == ')':
        print('incorrect')

    elif expr[-1] == '(':
        print('incorrect')

    elif a != b:
        print('incorrect')

    else:
        print('correct')


