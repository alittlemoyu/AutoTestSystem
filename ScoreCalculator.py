def scoreCalculator(inputAnswerList, answerList):
    score = 0
    count = 0
    for answer in answerList:
        if answer == inputAnswerList[count]:
            score += 1
    return score
