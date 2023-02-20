n = int(input())

ranking = []

for i in range(n):

    data = input().split()
    ranking.append((int(data[1]), int(data[2]), int(data[3]), data[0]))

ranking.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

for country in ranking:
    print(f'{country[-1]} {country[0]} {country[1]} {country[2]}')
