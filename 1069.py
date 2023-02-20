tests = int(input())

for c in range(tests):
    
    line = input()
    total = lower = 0
    
    for i in range(len(line)):
        
        if line[i] == '<':

            lower += 1

        elif line[i] == '>' and lower > 0:

            total += 1
            lower -= 1 #a cada par formado, subtraímos. Outro par formado assim que outro lower é encontrado e logo depois, um maior

    print(total)
