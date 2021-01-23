for j in range(20):
    data = [(str(j) + '+' + str(j) + '是'), str(2 * j) if j % 2 == 0 else str(j), '吗？', '\n', 'T' if j % 2 == 0 else 'F']
    directory = 'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\True_or_False\\' + str(j) + '.txt'
    fo = open(directory, 'w', encoding='utf-8')
    for line in data:
        fo.write(line)

    fo.close()
