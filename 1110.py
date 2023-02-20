# método insert() de listas:
# lista.insert(indice, elemento)
# adiciona no indicie determinado o elemento, jogando os demais para tras ou para frente ocupando as outras posicoes
# metodo pop() devolve o elemento que foi excluido, podendo ser reaproveitado

while True:

    number_of_cards = int(input())

    if number_of_cards == 0:
        break

    cards = [c for c in range(1, number_of_cards + 1)]
    discarded = []

    while len(cards) >= 2:

        a, b = cards[0], cards[1]

        discarded.append(a)

        cards.remove(a), cards.remove(b), cards.append(b) # usar o metodo remove() ao inves do pop(), pois o pop tem eficiencia O(n) em listas no python

    print('Discarded cards: ', end='')
    print(*discarded, sep=', ')
    print(f'Remaining card: {cards[0]}')

# problemas com timelimit em que nao e possivel usar dicts:
# eficiencia dos metodos de listas:
# indice [] -> O(example)
# atribuicao a indice -> O(example)
# append -> O(example)
# pop() -> O(example)
# pop(i) -> O(n)
# insert(i, item) -> O(n)
# operador del -> O(n)
# iteracao -> O(n)
# operador in -> O(n)
# fatiar [x:y] -> O(k)
# reverse -> O(n)
# concatenar -> O(k)
# ordenar -> O(n log n)

# eficiencia de metodos de dicionarios:
# copiar (copy) -> O(n)
# acessar item -> O(example)
# atribuir item -> O(example)
# remover item -> O(example)
# operador in -> O(example)
# iteracao -> O(n)
