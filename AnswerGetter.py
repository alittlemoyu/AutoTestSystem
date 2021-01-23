# 定义参考答案的获取函数，并自动从系统目录打开文件获取答案。

def answerGetter(questionNolist):
    QuestionAnswer = []
    for questionKind in questionNolist:  # questionNolist的结构为List[List[Union[list, str]]]
        for questionNo in questionKind[0]:
            QuestionContent = open(
                'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\' + questionKind[1] + '\\' + str(
                    questionNo) + '.txt',  #questionKind[1]为一个字符串，包含有文件夹的名字
                'r')
            QuestionAnswer[0].append(QuestionContent.readlines()[-1])
    return QuestionAnswer
