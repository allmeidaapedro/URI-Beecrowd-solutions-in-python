n, t = map(int, input().split())

dd = {}

for i in range(n):
    student = input().split()
    student[1] = int(student[1])
    dd[student[1]] = student[0]

length = int(n / t)

teams = {}

for j in range(t):
    teams[j + 1] = []

i = 1

for hab in sorted(dd, reverse=True):
    teams[i].append(dd[hab])
    i += 1
    if i > len(teams):
        i = 1

for team in teams:

    print(f'Time {team}')
    teams[team].sort()

    for student in teams[team]:
        print(student)

    print()

