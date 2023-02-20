while True:

    height, width = map(int, input().split())

    if width == height == 0:
        break

    all = []

    for i in range(width):

        draw = input()
        all.append(draw)

    new_height, new_width = map(int, input().split())

    for pos, e in enumerate(all):

        final = ''

        for chr in e:

            if len(final) == new_width:
                break

            final += chr * int((new_width / width))
            all[pos] = final

    reps = int(new_height / height)

    for i in range(len(all)):

        for k in range(reps):

            print(all[i], sep='\n')

    print()

