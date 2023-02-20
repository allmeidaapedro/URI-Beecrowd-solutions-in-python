while True:
    alice_cards, beatriz_cards = map(int, input().split())

    if alice_cards == beatriz_cards == 0:
        break

    alice = [int(x) for x in input().split()]
    beatriz = [int(x) for x in input().split()]

    setA, setB = set(alice), set(beatriz)
    setAux = setB #evitar o uso de mais de um "if"

    if len(setA) < len(setB):

        setAux = setA
        setA = setB

    setAux = [x for x in setAux if x not in setA]

    print(len(setAux))