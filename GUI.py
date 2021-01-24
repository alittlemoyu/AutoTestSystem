# import sys
#
# import wx
#
# import GuiCore
#
#
# def GUI(testName, QuestionNo, QuestionKind, QuestionContent):  # 定义一个GUI的调用入口，向GuiCore传入参数，并接受传出的答案。
#     app = wx.App()
#     frame = GuiCore.GUI(testName)
#     frame.displayQuestionNo(QuestionNo)
#     frame.displayQuestionKind(QuestionKind)
#     if QuestionKind == 'FillBlank':  # 根据试题类型调用不同的显示过程
#         frame.displayQuestionFillBlank(QuestionContent)
#     elif QuestionKind == 'SingleChoice':
#         frame.displayQuestionSingleChoice(QuestionContent)  # 未定义
#     else:
#         frame.displayQuestionTrueFalse(QuestionContent)
#     frame.displaySizer()
#     frame.Show()
#     frame.Center()
#     return answer  # 未定义
#     # sys.exit(app.MainLoop())
#
#
# def GuiStart(test, questionTotalCount):  # GUI函数与Main函数的中间界面
#     inputAnswerList = []
#     for question in test.SingleChoiceList + test.FillBlankList + test.TrueFalseList:
#         questionTotalCount += 1
#         if questionTotalCount <= test.SingleChoiceCount:  # 根据总共显示的题量判断目前题目类型
#             QuestionContent = open(
#                 'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\Single_choice' + str(question) + '.txt', 'r')
#             QuestionContentLine = QuestionContent.readline()
#             QuestionContentChoice = QuestionContent.readlines()[1:4]
#             QuestionContentLine_n_Choice = QuestionContentChoice.insert(0, QuestionContentLine)
#             inputAnswerList.append(GUI(test.testName, questionTotalCount, "SingleChoice", QuestionContentLine_n_Choice))
#             # 向GUI函数传入一个数据包
#         elif questionTotalCount <= test.FillBlankCount + test.SingleChoiceCount:
#             QuestionContent = open(
#                 'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\Fill_in_the_blank' + str(question) + '.txt', 'r')
#             QuestionContentLine = QuestionContent.readline()
#             inputAnswerList.append(GUI(test.testName, questionTotalCount, "FillBlank", QuestionContentLine))
#         else:
#             QuestionContent = open(
#                 'C:\\Users\\holyCRAP\\OneDrive\\Python\\AutoTestSystem\\Database\\True_or_False' + str(question) + '.txt', 'r')
#             QuestionContentLine = QuestionContent.readline()
#             inputAnswerList.append(GUI(test.testName, questionTotalCount, "TrueFalse", QuestionContentLine))
#     return inputAnswerList
import operator
import sys
import time

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from AutoTestSystem.ScoreCalculator import scoreCalculator


class examPaper(PyQt5.QtWidgets.QMainWindow):
    def __init__(self,test):
        super().__init__()
        self.questionNum = [self.test.SingleChoiceCount, self.test.FillBlankCount, self.test.TrueFalseCount]
        # self.Generator = generator(self.questionNum)
        # self.questionContent = self.Generator.generate()
        self.inputAnswerList = []
        self.startTime = 0
        self.nowTime = 0
        self.timeAll = 1
        self.remainTime = self.timeAll
        self.test = test


        for i in range(self.questionNum[0]):
            self.inputAnswerList.append(-1)
        for i in range(self.questionNum[0], self.questionNum[0] + self.questionNum[1]):
            self.inputAnswerList.append([False, False, False, False])
        for i in range(self.questionNum[0] + self.questionNum[1],
                       self.questionNum[0] + self.questionNum[1] + self.questionNum[2]):
            self.inputAnswerList.append(-100000)
        self.id = 0
        self.initUI()
        self.questionContent=test.examContentGenerator()


    def initWindow(self):
        self.setGeometry(100, 100, 1080, 720)
        self.setWindowTitle("Exam")
        self.setWindowIcon(QIcon(r"icon.png"))
        self.status = self.statusBar()
        self.status.showMessage('小学生考试系统 作者：孙琦睿')
        self.status.setFont(QFont("Roman times", 20, QFont.Bold))
        self.view = QGraphicsView(self)
        self.view.setGeometry(30, 50, 720 + 10, 480 + 10)

        self.label1 = QtWidgets.QLabel(self)
        self.label2 = QtWidgets.QLabel(self)
        self.label3 = QtWidgets.QLabel(self)
        self.label4 = QtWidgets.QLabel(self)
        # self.labelTheme.setGeometry(100, 100, 500, 500)
        self.label1.setText("小学入学考试——加法考试")
        self.label1.setFixedWidth(400)
        self.label1.move(220, 120)
        self.label1.setFont(QFont("Roman times", 20, QFont.Bold))

        self.label2.setText("小明考生，你好！按下下一题则考试开始")
        self.label2.setFixedWidth(800)
        self.label2.move(100, 220)
        self.label2.setFont(QFont("Roman times", 20, QFont.Bold))

        self.label3.setText("你将有%d分钟时间完成该试卷" % self.timeAll)
        self.label3.setFixedWidth(800)
        self.label3.move(300, 380)
        self.label3.setFont(QFont("Roman times", 10, QFont.Bold))

        self.label4.setText("剩余考试时间为:%d分钟" % self.remainTime)
        self.label4.setFixedWidth(800)
        self.label4.move(100, 480)
        self.label4.setFont(QFont("Roman times", 10, QFont.Bold))

        self.labelTitle = PyQt5.QtWidgets.QLabel(self)
        self.labelQuestion1 = PyQt5.QtWidgets.QLabel(self)
        self.labelQuestion2 = PyQt5.QtWidgets.QLabel(self)
        self.labelQuestion3 = PyQt5.QtWidgets.QLabel(self)
        self.labelQuestion4 = PyQt5.QtWidgets.QLabel(self)

        self.labelFill = PyQt5.QtWidgets.QLabel(self)
        self.edit = PyQt5.QtWidgets.QLineEdit(self)
        self.edit.hide()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_remain_time(self.test))
        self.timer.start()

    def show_remain_time(self,test):
        if (self.nowTime - self.startTime) > self.timeAll * 60:
            score = scoreCalculator(self.inputAnswerList, self.answerGetter(self.questionNoList))
            for i in range(self.questionNum[0] + self.questionNum[1]):
                self.A[i].hide()
                self.B[i].hide()
                self.C[i].hide()
                self.D[i].hide()
            self.labelQuestion1.hide()
            self.labelQuestion2.hide()
            self.labelQuestion3.hide()
            self.labelQuestion4.hide()
            self.edit.hide()

            self.labelFill.hide()
            self.labelTitle.hide()
            self.label1.setText("考试时间到，你的成绩是：")
            self.nextButton.hide()

            self.label1.move(220, 220)
            self.label1.show()
            self.label2.setText("%d" % int(score))
            self.label2.move(300, 300)
            self.label2.show()

        if self.startTime != 0:
            self.nowTime = time.time()

        if self.startTime != 0 and self.nowTime != 0:
            self.label4.setText("剩余考试时间为:%d分钟" % int(self.remainTime - (self.nowTime - self.startTime) / 60))

    def initUI(self):
        self.initWindow()
        self.viewWindow()
        self.commandButton()

    def viewWindow(self):
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

    def commandButton(self):
        self.exitCommand()
        self.nextQuestionCommand()
        self.choiceCommand()

    def choiceCommand(self):
        self.A = []
        self.B = []
        self.C = []
        self.D = []
        for i in range(self.questionNum[0]):
            self.A.append(PyQt5.QtWidgets.QRadioButton('A.', self))
            self.B.append(PyQt5.QtWidgets.QRadioButton('B.', self))
            self.C.append(PyQt5.QtWidgets.QRadioButton('C.', self))
            self.D.append(PyQt5.QtWidgets.QRadioButton('D.', self))
            self.A[i].setGeometry(100, 215, 45, 40)
            self.B[i].setGeometry(100, 255, 45, 40)
            self.C[i].setGeometry(100, 295, 45, 40)
            self.D[i].setGeometry(100, 335, 45, 40)
            self.A[i].setFont(QFont("Roman times", 15, QFont.Bold))
            self.B[i].setFont(QFont("Roman times", 15, QFont.Bold))
            self.C[i].setFont(QFont("Roman times", 15, QFont.Bold))
            self.D[i].setFont(QFont("Roman times", 15, QFont.Bold))

            self.A[i].setCheckable(True)
            self.B[i].setCheckable(True)
            self.C[i].setCheckable(True)
            self.D[i].setCheckable(True)

            self.A[i].toggled.connect(lambda: self.recordAnswer('A'))
            self.B[i].toggled.connect(lambda: self.recordAnswer('B'))
            self.C[i].toggled.connect(lambda: self.recordAnswer('C'))
            self.D[i].toggled.connect(lambda: self.recordAnswer('D'))

            self.A[i].hide()
            self.B[i].hide()
            self.C[i].hide()
            self.D[i].hide()

        for i in range(self.questionNum[0], self.questionNum[0] + self.questionNum[1]):
            self.A.append(PyQt5.QtWidgets.QCheckBox('A.', self))
            self.B.append(PyQt5.QtWidgets.QCheckBox('B.', self))
            self.C.append(PyQt5.QtWidgets.QCheckBox('C.', self))
            self.D.append(PyQt5.QtWidgets.QCheckBox('D.', self))
            self.A[i].setGeometry(100, 215, 45, 40)
            self.B[i].setGeometry(100, 255, 45, 40)
            self.C[i].setGeometry(100, 295, 45, 40)
            self.D[i].setGeometry(100, 335, 45, 40)
            self.A[i].setFont(QFont("Roman times", 15, QFont.Bold))
            self.B[i].setFont(QFont("Roman times", 15, QFont.Bold))
            self.C[i].setFont(QFont("Roman times", 15, QFont.Bold))
            self.D[i].setFont(QFont("Roman times", 15, QFont.Bold))
            self.A[i].setCheckable(True)
            self.B[i].setCheckable(True)
            self.C[i].setCheckable(True)
            self.D[i].setCheckable(True)
            self.A[i].toggled.connect(lambda: self.recordAnswer(0))
            self.B[i].toggled.connect(lambda: self.recordAnswer(1))
            self.C[i].toggled.connect(lambda: self.recordAnswer(2))
            self.D[i].toggled.connect(lambda: self.recordAnswer(3))
            self.A[i].hide()
            self.B[i].hide()
            self.C[i].hide()
            self.D[i].hide()

        # self.A.move(120, 220)

    def answerGetter(self,questionNolist):
        QuestionAnswer = []
        for questionKind in questionNolist:  # questionNolist的结构为List[List[Union[list, str]]]
            for questionNo in questionKind[0]:
                QuestionContent = open(
                    'Database\\' + questionKind[1] + '\\' + str(
                        questionNo) + '.txt',  # questionKind[1]为一个字符串，包含有文件夹的名字
                    'r')
                QuestionAnswer[0].append(QuestionContent.readlines()[-1])
        return QuestionAnswer

    def recordAnswer(self, choice):

        if ((self.id - 1 )< self.questionNum[0]):
            self.inputAnswerList[self.id - 1] = choice
        else:
            self.inputAnswerList[self.id - 1][choice] = not self.inputAnswerList[self.id - 1][choice]

    def calculateAnswer(self,inputAnswerList, answerList):
        # yesNumber = 0
        # allNumber = len(self.inputAnswerList)
        #
        # for i in range(self.questionNum[0] + self.questionNum[1]):
        #     if (operator.eq(self.inputAnswerList[i], self.questionContent[i]["answer"])):
        #         yesNumber += 1
        # for i in range(self.questionNum[0] + self.questionNum[1],
        #                self.questionNum[0] + self.questionNum[1] + self.questionNum[2] - 1):
        #
        #     if (operator.eq(int(self.inputAnswerList[i]), int(self.questionContent[i]["answer"]))):
        #         yesNumber += 1
        #
        # score = yesNumber / allNumber * 100
        score = 0
        count = 0
        for answer in answerList:
            if answer == inputAnswerList[count]:  # 一一对比答题与答案
                score += 1
        return score

    def exitCommand(self):
        exitButton = PyQt5.QtWidgets.QPushButton("退出考试", self)
        exitButton.move(900, 650)

        exitButton.clicked[bool].connect(QCoreApplication.instance().quit)

    def nextQuestionCommand(self):
        self.nextButton = PyQt5.QtWidgets.QPushButton("下一题", self)
        self.nextButton.move(600, 450)
        self.nextButton.clicked[bool].connect(self.nextQuestion)

    def nextQuestion(self):
        # 考试结束
        self.label1.hide()
        self.label2.hide()
        self.label3.hide()
        if self.id == 0:
            self.startTime = time.time()
            # self.nowTime = self.startTime

        if 0 < self.id < self.questionNum[0] + self.questionNum[1] + 1:
            # print(self.A[0].isDown())
            self.A[self.id - 1].hide()
            self.B[self.id - 1].hide()
            self.C[self.id - 1].hide()
            self.D[self.id - 1].hide()

        if (self.id > self.questionNum[0] + self.questionNum[1] and self.id <= self.questionNum[0] + self.questionNum[
            1] + self.questionNum[2]):
            self.inputAnswerList[self.id - 1] = self.edit.text()
            self.edit.setText('')

        if self.id == self.questionNum[0] + self.questionNum[1] + self.questionNum[2] - 1:
            self.nextButton.setText("提交")

        if self.id == self.questionNum[0] + self.questionNum[1] + self.questionNum[2]:
            self.nextButton.hide()
            self.edit.hide()
            self.labelFill.hide()
            self.labelTitle.hide()
            self.label1.setText("考试结束，你的成绩是：")
            # print(self.inputAnswerList)
            score = self.calculateAnswer(self.inputAnswerList,self.answerGetter(self.questionNoList))
            self.label1.move(220, 220)
            self.label1.show()
            self.label2.setText("%d" % int(score))
            self.label2.move(300, 300)
            self.label2.show()
            return

        theme = self.questionContent[self.id][0]
        if theme == "Single_choice":
            title = str(self.id + 1) + '.' + self.questionContent[self.id][1]
            self.labelQuestion1.setText(self.questionContent[self.id][2])
            self.labelQuestion1.setFixedWidth(800)
            self.labelQuestion1.move(160, 220)
            self.labelQuestion1.setFont(QFont("Roman times", 15, QFont.Bold))

            self.labelQuestion2.setText(self.questionContent[self.id][3])
            self.labelQuestion2.setFixedWidth(800)
            self.labelQuestion2.move(160, 260)
            self.labelQuestion2.setFont(QFont("Roman times", 15, QFont.Bold))

            self.labelQuestion3.setText(self.questionContent[self.id][4])
            self.labelQuestion3.setFixedWidth(800)
            self.labelQuestion3.move(160, 300)
            self.labelQuestion3.setFont(QFont("Roman times", 15, QFont.Bold))

            self.labelQuestion4.setText(self.questionContent[self.id][5])
            self.labelQuestion4.setFixedWidth(800)
            self.labelQuestion4.move(160, 340)
            self.labelQuestion4.setFont(QFont("Roman times", 15, QFont.Bold))
            self.A[self.id].show()
            self.B[self.id].show()
            self.C[self.id].show()
            self.D[self.id].show()


        elif (theme == "True_or_False"):
            title = str(self.id + 1) + '.'"以下答案错误的是"
            self.labelQuestion1.setText(self.questionContent[self.id]["question"][0])
            self.labelQuestion2.setText(self.questionContent[self.id]["question"][1])
            self.A[self.id].show()
            self.B[self.id].show()
            self.C[self.id].show()
            self.D[self.id].show()


        elif (theme == "Fill_in_the_blank"):
            title = str(self.id + 1) + '.'"请填上正确答案(填空)"
            self.labelQuestion1.hide()
            self.labelQuestion2.hide()
            self.labelQuestion3.hide()
            self.labelQuestion4.hide()
            self.labelFill.setText(self.questionContent[self.id]["question"])

            self.labelFill.setFixedWidth(800)
            self.labelFill.move(140, 250)
            self.labelFill.setFont(QFont("Roman times", 15, QFont.Bold))
            self.edit.move(350, 300)
            self.edit.show()

        self.labelTitle.setText(title)
        self.labelTitle.setFixedWidth(800)
        self.labelTitle.move(100, 120)
        self.labelTitle.setFont(QFont("Roman times", 20, QFont.Bold))

        self.id += 1
        pass


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)

    window = examPaper()
    window.setObjectName("MainWindow")
    window.setStyleSheet("#MainWindow{border-image:url(background.jpg);}")
    window.show()

    sys.exit(app.exec_())
