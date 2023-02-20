good_kids = []

while True:

    try:

        good_kid = input()

    except EOFError:
        break

    good_kids.append([good_kid.lower(), good_kid])

good_kids.sort(key=lambda x: x[0], reverse=True)

print(good_kids[0][1])


