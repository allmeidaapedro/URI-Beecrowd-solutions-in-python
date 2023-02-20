while True:

    try:
        name, nmbr_of_gifts = input().split()

    except EOFError:
        break

    final_list = []

    for i in range(int(nmbr_of_gifts)):
        gift_name = input()
        price, preference = map(float, input().split())
        final_list.append((int(preference), price, gift_name))


    final_list.sort(key=lambda x: (-x[0], x[1], x[2]))

    print(f'Lista de {name}')
    for gift in final_list:
        print(f'{gift[2]} - R${gift[1]:.2f}')

    print()