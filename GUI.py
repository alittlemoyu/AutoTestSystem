import wx
import sys
import GuiCore
from AutoTestSystem import ExamGenerator


def GUI(testName, QuestionNo, QuestionKind, QuestionContent):
    app = wx.App()
    frame = GuiCore.GUI(testName)
    frame.displayQuestionNo(QuestionNo)
    frame.displayQuestionKind(QuestionKind)
    if QuestionKind == 'FillBlank':
        frame.displayQuestionFillBlank(QuestionContent)
    elif QuestionKind == 'SingleChoice':
        frame.displayQuestionSingleChoice(QuestionContent)
    else:
        frame.displayQuestionTrueFalse(QuestionContent)
    frame.displaySizer()
    frame.Show()
    frame.Center()
    return answer

    sys.exit(app.MainLoop())


def GuiStart(test, questionTotalCount):
    inputAnswerList = []
    for question in test.SingleChoiceList + test.FillBlankList + test.TrueFalseList:
        questionTotalCount += 1
        if questionTotalCount <= test.SingleChoiceCount:
            QuestionContent = open(
                'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\Single_choice' + str(question) + '.txt', 'r')
            QuestionContentLine = QuestionContent.readline()
            QuestionContentChoice = QuestionContent.readlines()[1:4]
            QuestionContentLine_n_Choice = QuestionContentChoice.insert(0, QuestionContentLine)
            inputAnswerList.append(GUI(test.testName, questionTotalCount, "SingleChoice", QuestionContentLine_n_Choice))
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
