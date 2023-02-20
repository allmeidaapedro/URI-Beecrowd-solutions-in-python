while True:
    nmbr_of_students = int(input())

    if nmbr_of_students == 0:
        break

    original_signs, false_signs = dict(), 0

    for i in range(nmbr_of_students):
        student_original_sign = input().split()
        original_signs[student_original_sign[0]] = student_original_sign[1]

    students_in_class = int(input())

    for j in range(students_in_class):

        students_class_sign = input().split()

        different_letters = 0

        for k in range(len(original_signs[students_class_sign[0]])):
            if original_signs[students_class_sign[0]][k] != students_class_sign[1][k]:
                different_letters += 1
                if different_letters > 1:
                    false_signs += 1
                    break

    print(false_signs)