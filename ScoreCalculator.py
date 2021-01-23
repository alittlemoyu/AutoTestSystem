def scoreCalculator(inputAnswerList, answerList):
    score = 0
    count = 0
    for answer in answerList:
        if answer == inputAnswerList[count]:  # 一一对比答题与答案
            score += 1
    return score
