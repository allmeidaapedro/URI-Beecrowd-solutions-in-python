while True:

    try:

        loops = int(input())

    except EOFError:
        break

    for i in range(loops):

        expr = input()

        stack = []

        for j in range(len(expr)):

            if j == len(expr) / 2:

                while stack:

                    print(stack.pop(), end='')

            stack.append(expr[j])

        while stack:

            print(stack.pop(), end='')

        print()




