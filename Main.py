import ExamGenerator
import GUI
import AutoTestSystem.AnswerGetter
from AutoTestSystem.ScoreCalculator import scoreCalculator

questionTotalCount = 0

test = ExamGenerator.Test(useCustomizer=False, testScore=35, testName='Test')  # 声明并实例化一个Test对象
inputAnswerList = GUI.GuiStart(test, questionTotalCount)  # 接受GUI传出的答案
questionNoList = [[test.SingleChoiceList, 'Single_choice'], [test.FillBlankList, 'Fill_in_the_blank'],
                  [test.TrueFalseList, 'True_or_False']]  # 打包一个题目表传入答案生成函数

score = scoreCalculator(inputAnswerList, AutoTestSystem.AnswerGetter.answerGetter(questionNoList))  # 计算总分
print(score)