murders, all_dead = dict(), set()

while True:

    try:

        murderer, dead = input().split()

    except EOFError:
        break

    all_dead.add(dead)

    if murderer not in murders:
        murders[murderer] = 1

    else:
        murders[murderer] += 1

print('HALL OF MURDERERS')

for murderer in sorted(murders):

    if murderer not in all_dead:
        print(murderer, murders[murderer])
