import ExamGenerator
import GUI
from AutoTestSystem.AnswerGetter import answerGetter
from AutoTestSystem.ScoreCalculator import scoreCalculator

questionTotalCount = 0

test = ExamGenerator.Test(useCustomizer=False, testScore=35, testName='Test')
questionNoList = [[test.SingleChoiceList, 'Single_choice'], [test.FillBlankList, 'Fill_in_the_blank'],
                  [test.TrueFalseList, 'True_or_False']]
inputAnswerList = GUI.GuiStart(test, questionTotalCount)
score = scoreCalculator(inputAnswerList, answerGetter(questionNoList))
