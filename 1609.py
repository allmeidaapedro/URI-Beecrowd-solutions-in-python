tests = int(input())

for i in range(tests):

    little_sheep = int(input())
    sequence = list(map(int, input().split()))[:little_sheep]
    
    print(len(set(sequence)))

