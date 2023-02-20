while True:

    try:
        q = int(input())

    except EOFError:
        break

    students = []

    for i in range(q):
        student = input().split()
        students.append((int(student[2]), student[1], student[0]))

    students.sort(key=lambda x: (x[0], x[1], x[2]))

    print(*[student[2] for student in students], sep='\n')


