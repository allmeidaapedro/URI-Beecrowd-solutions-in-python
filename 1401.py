#modulo itertools -> nativo do python -> iteradores, eficiencia
#iterador permutations -> retorna tuplas com cada permutacao possivel para um objeto iteravel

from itertools import permutations

number_of_strings = int(input())

for i in range(number_of_strings):

    string = input()

    perms = {}

    for element in permutations(string):

        permutation = ''.join(element)

        if permutation not in perms:

            perms[permutation] = 1

    for permutation in sorted(perms):

        print(permutation)

    print()


#OUTRA SOLUÇÃO:

number_of_strings = int(input())

for i in range(number_of_strings):

    string = input()

    all_permutations_sorted = []

    for element in permutations(string):

        permutation = list(element)
        permutation = ''.join(permutation)
        all_permutations_sorted.append(permutation)

    all_permutations_sorted = list(dict.fromkeys(all_permutations_sorted)) #método fromkeys cria um dicionário a partir da lista/sequência f: remove os duplicados, formando chaves únicas com valor none
    all_permutations_sorted.sort()

    print(*all_permutations_sorted, sep='\n')

    print()

#método fromkeys()
#gerar um dicionário a partir das chaves fornecidas (itens de uma seq)
#sintaxe: fromkeys(seq, val)
#parâmetros: seq(sequência a ser transformada em um dicionário)
# val(valores iniciais atribuídos às chaves -> padrão: nenhum
#retorna: dicionário com chaves mapeadas para None se nenhum valor for fornecido
# ou dicionário com chaves mapeadas p valor inicial fornecido
