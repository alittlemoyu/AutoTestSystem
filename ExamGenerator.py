import random

SingleChoiceLibCount = 20
FillBlankLibCount = 20
TrueFalseLibCount = 20


def QuestionListGenerator(list_input_raw):
    list_input, count, libCount = list_input_raw
    for i in range(0, count):
        while len(list_input) < count:
            list_input.append(random.randint(1, libCount))
            if list_input.index(list_input[-1]) != len(list_input) - 1:
                list_input.pop()


class Error(Exception):
    pass


class GeneratorError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr(self.message)


class Test:
    def __init__(self, useCustomizer=False, testScore=100, testName='Test'):
        self.testName = testName
        self.__testScore = testScore
        self.__SingleChoiceList = []
        self.__FillBlankList = []
        self.__TrueFalseList = []
        if useCustomizer:
            self.__testScore = None
            self.__needCustomizer = True
            buffer = eval(input("TestCustomizer start. Input 3 num:"))
            self.testCustomizer(buffer[0], buffer[1], buffer[2])
            self.__testQuestionListGenerator()
        else:
            self.__testQuestionCountGenerator(testScore)
            self.__testQuestionListGenerator()

    @property
    def FillBlankCount(self):
        if self.__needCustomizer:
            raise GeneratorError("needCustomizer = True", "试卷类型为自定义，需要进行题目定制才能获取填空题数量。")
        else:
            return self.__FillBlankCount

    @property
    def FillBlankList(self):
        if self.__needCustomizer:
            raise GeneratorError("needCustomizer = True", "试卷类型为自定义，需要进行题目定制才能获取填空题题号。")
        else:
            return self.__FillBlankList

    @property
    def SingleChoiceCount(self):
        if self.__needCustomizer:
            raise GeneratorError("needCustomizer = True", "试卷类型为自定义，需要进行题目定制才能获取选择题数量。")
        else:
            return self.__SingleChoiceCount

    @property
    def SingleChoiceList(self):
        if self.__needCustomizer:
            raise GeneratorError("needCustomizer = True", "试卷类型为自定义，需要进行题目定制才能获取选择题题号。")
        else:
            return self.__SingleChoiceList

    @property
    def TrueFalseCount(self):
        if self.__needCustomizer:
            raise GeneratorError("needCustomizer = True", "试卷类型为自定义，需要进行题目定制才能获取判断题数量。")
        else:
            return self.__TrueFalseCount

    @property
    def TrueFalseList(self):
        if self.__needCustomizer:
            raise GeneratorError("needCustomizer = True", "试卷类型为自定义，需要进行题目定制才能获取判断题题号。")
        else:
            return self.__TrueFalseList

    @property
    def testScore(self):
        if self.__needCustomizer:
            raise GeneratorError("needCustomizer = True", "试卷类型为自定义，需要进行题目定制才能获取试卷总分。")
        else:
            return self.__testScore

    def testCustomizer(self, FillBlank, SingleChoice, TrueFalse):
        if not self.__needCustomizer:
            raise GeneratorError("needCustomizer = False", "试卷类型为默认。")
        else:
            self.__FillBlankCount = FillBlank
            self.__SingleChoiceCount = SingleChoice
            self.__TrueFalseCount = TrueFalse
            self.__TestScore = self.__SingleChoiceCount * 3 + self.__FillBlankCount * 2 + self.__TrueFalseCount
            self.__needCustomizer = False

    def __testQuestionCountGenerator(self, score):
        if score < 10:
            raise GeneratorError("score < 10", "试卷总分太少。给谁考试呢这是？")
        elif score < 20:
            self.__TrueFalseCount = score % 5
            self.__FillBlankCount = self.__SingleChoiceCount = score / 5
        elif score <= 100:
            self.__TrueFalseCount = score % 10 + 10
            self.__FillBlankCount = self.__SingleChoiceCount = (score - self.__TrueFalseCount / 5)
        elif score > 100 or score < 0:
            raise GeneratorError("score > 100 or score < 0", "😅")

    def __testQuestionListGenerator(self):
        question_list = [[self.__SingleChoiceList, self.__SingleChoiceCount, SingleChoiceLibCount],
                         [self.__FillBlankList, self.__FillBlankCount, FillBlankLibCount],
                         [self.__TrueFalseList, self.__TrueFalseCount, TrueFalseLibCount]]
        for i in question_list:
            QuestionListGenerator(i)
