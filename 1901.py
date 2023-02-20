forest_size = int(input())
species_cell_total, visited = [], []

for i in range(forest_size):

    species_cell = list(map(int, input().split()))
    species_cell_total.append(species_cell)

for j in range(forest_size * 2):

    visited_1, visited_2 = map(int, input().split())
    visited.append(species_cell_total[visited_1 - 1][visited_2 - 1])

print(len(set(visited)))
