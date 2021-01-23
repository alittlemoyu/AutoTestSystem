import sys

import wx

import GuiCore


def GUI(testName, QuestionNo, QuestionKind, QuestionContent):  # 定义一个GUI的调用入口，向GuiCore传入参数，并接受传出的答案。
    app = wx.App()
    frame = GuiCore.GUI(testName)
    frame.displayQuestionNo(QuestionNo)
    frame.displayQuestionKind(QuestionKind)
    if QuestionKind == 'FillBlank':  # 根据试题类型调用不同的显示过程
        frame.displayQuestionFillBlank(QuestionContent)
    elif QuestionKind == 'SingleChoice':
        frame.displayQuestionSingleChoice(QuestionContent)  # 未定义
    else:
        frame.displayQuestionTrueFalse(QuestionContent)
    frame.displaySizer()
    frame.Show()
    frame.Center()
    return answer  # 未定义
    # sys.exit(app.MainLoop())


def GuiStart(test, questionTotalCount):  # GUI函数与Main函数的中间界面
    inputAnswerList = []
    for question in test.SingleChoiceList + test.FillBlankList + test.TrueFalseList:
        questionTotalCount += 1
        if questionTotalCount <= test.SingleChoiceCount:  # 根据总共显示的题量判断目前题目类型
            QuestionContent = open(
                'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\Single_choice' + str(question) + '.txt', 'r')
            QuestionContentLine = QuestionContent.readline()
            QuestionContentChoice = QuestionContent.readlines()[1:4]
            QuestionContentLine_n_Choice = QuestionContentChoice.insert(0, QuestionContentLine)
            inputAnswerList.append(GUI(test.testName, questionTotalCount, "SingleChoice", QuestionContentLine_n_Choice))
            # 向GUI函数传入一个数据包
        elif questionTotalCount <= test.FillBlankCount + test.SingleChoiceCount:
            QuestionContent = open(
                'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\Fill_in_the_blank' + str(question) + '.txt', 'r')
            QuestionContentLine = QuestionContent.readline()
            inputAnswerList.append(GUI(test.testName, questionTotalCount, "FillBlank", QuestionContentLine))
        else:
            QuestionContent = open(
                'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\True_or_False' + str(question) + '.txt', 'r')
            QuestionContentLine = QuestionContent.readline()
            inputAnswerList.append(GUI(test.testName, questionTotalCount, "TrueFalse", QuestionContentLine))
    return inputAnswerList
