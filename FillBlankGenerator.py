for i in range(20):
    data = [(str(i) + '+' + str(i) + '是') * ((i + 1)//2), '\n', str(2 * i)]
    directory = 'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\Fill_in_the_blank\\' + str(i) + '.txt'
    fo = open(directory, 'w', encoding='utf-8')
    for line in data:
        fo.write(line)

    fo.close()

# 填空题生成，共两行，第一行为题目，第二行为答案