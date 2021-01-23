import random

for k in range(20):
    liebiao = [0, 0, 0, 0]
    count = 1
    for i in range(0, 4):  # 该四位数去重乱序算法实现使用了一个较为笨重的实现方式，但符合直觉。较好的实现方式已经在ExamGenerator中加载。
        while True:
            liebiao[i] = random.randint(1, 4)
            print("Generating")
            print("i=", liebiao[i])
            print('Count = ', count)
            print(liebiao)
            if count == 1:
                count += 1
                break
            elif count == 2:
                if liebiao[0] != liebiao[1]:
                    count += 1
                    break
            elif count == 3:
                if liebiao[1] != liebiao[2] != liebiao[0]:
                    count += 1
                    break
            else:
                if liebiao[2] != liebiao[3] != liebiao[1] and liebiao[3] != liebiao[0]:
                    print("Pass!")
                    break
    choiceDataRaw = [k - random.randint(0, k), k + random.randint(0, k - 1 if k - 1 >= 0 else k), 2 * k, int(1.5 * k)]
    # 选项生成

    choiceData = [0, 0, 0, 0]
    for a in range(0, 4):
        choiceData[a] = choiceDataRaw[liebiao[a] - 1]
    data = [(str(k) + '+' + str(k) + '是多少呢？'), '\n', 'A.', str(choiceData[0]), '\n', 'B.', str(choiceData[1]),
            '\n' 'C.',
            str(choiceData[2]), '\n' 'D.', str(choiceData[3]), '\n']
    directory = 'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\Single_choice\\' + str(k) + '.txt'
    fo = open(directory, 'w', encoding='utf-8')
    for line in data:
        fo.write(line)
    answer = ["A", "B", "C", "D"]
    fo.write(answer[liebiao.index(3)])
    fo.close()
