while True:

    students, dinner = map(int, input().split())

    if students == dinner == 0:

        break

    participate = {}

    for c in range(dinner):

        dinners = list(map(int, input().split()))

        for i in range(len(dinners)):

            p = i + 1

            if p not in participate:

                participate[p] = dinners[i]

            else:

                participate[p] += dinners[i]

    participate = list(filter(lambda p: p[1] == dinner, participate.items()))

    if participate != []:

        print('yes')

    else:
        
        print('no')


