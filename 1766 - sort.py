tests = int(input())
test_case = 1

for i in range(tests):

    total_reindeer, reindeer_sled = map(int, input().split())
    reindeer_sort = []

    for j in range(total_reindeer):

        name_weight_age_height = input().split()
        reindeer_sort.append((name_weight_age_height[0], int(name_weight_age_height[1]), int(name_weight_age_height[2]), float(name_weight_age_height[3])))

    reindeer_sort.sort(key=lambda x: (-x[1], x[2], x[3], x[0]))

    reindeer_sort = reindeer_sort[:reindeer_sled]

    scenario = '{' + str(test_case) + '}'

    print(f'CENARIO {scenario}')

    for k in range(1, reindeer_sled + 1):

        print(f'{k} - {reindeer_sort[k - 1][0]}')

    test_case += 1
