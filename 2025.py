number_of_lines = int(input())

for i in range(number_of_lines):

    text_line = input().split()

    index_list = []

    for index, word in enumerate(text_line):

        if '.' in word:
            text_line[index] = word[:-1]
            index_list.append(index)

    for index, word in enumerate(text_line):

        if word[1:len(word) - 1] == 'oulupukk':
            text_line[index] = 'Joulupukki'

    for index in index_list:
        text_line[index] += '.'

    print(*text_line)


