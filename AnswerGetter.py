def answerGetter(questionNolist):
    QuestionAnswer = []
    for questionKind in questionNolist:
        for questionNo in questionKind[0]:
            QuestionContent = open(
                'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\' + questionKind[1] + '\\' + str(questionNo) + '.txt',
                'r')
            QuestionAnswer[0].append(QuestionContent.readlines()[-1])
    return QuestionAnswer
