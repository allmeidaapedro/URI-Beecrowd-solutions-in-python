n = int(input())

captured = []

for i in range(n):

    pokemon = input()
    captured.append(pokemon)

print(f'Falta(m) {151 - len(set(captured))} pokemon(s).')
