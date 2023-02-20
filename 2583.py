tests = int(input())

for i in range(tests):

    uses = int(input())
    dd = {'chirrin': [], 'chirrion': []}

    for j in range(uses):

        thing_option = input().split()

        if thing_option[1] == 'chirrion' and thing_option[0] in dd['chirrin']:
            dd['chirrin'].remove(thing_option[0])

        elif thing_option[1] == 'chirrin' and thing_option[0] not in dd['chirrin']:
            dd['chirrin'].append(thing_option[0])

    print('TOTAL')

    for thing in sorted(dd['chirrin']):
        print(thing)
