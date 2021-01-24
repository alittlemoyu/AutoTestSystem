import random

# 自行输入题库的题目数量
SingleChoiceLibCount = 20
FillBlankLibCount = 20
TrueFalseLibCount = 20


def QuestionListGenerator(list_input_raw):  # 根据试卷不同类型的题目数量自动提取题目，保证不重复
    list_input, count, libCount = list_input_raw  # 解包数据
    for i in range(0, count):
        while len(list_input) < count:
            list_input.append(random.randint(1, libCount))
            if list_input.index(list_input[-1]) != len(list_input) - 1:  # 确保每次向list中添加的题号都是首次出现，否则pop弹出
                list_input.pop()


class Error(Exception):
    pass


class GeneratorError(Error):  # 定义错误类
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return repr(self.message)


class Test:  # 定义试卷大类
    def __init__(self, useCustomizer=False, testScore=100, testName='Test'):
        self.testName = testName  # 除试卷名可随时更改外，其余属性均设为私有
        self.__testScore = testScore
        self.__SingleChoiceList = []  # 题号表
        self.__FillBlankList = []
        self.__TrueFalseList = []
        if useCustomizer:  # 定义一个参数，用于告知程序是否需要自定义试卷题目
            self.__testScore = None
            self.__needCustomizer = True
            buffer = eval(input("TestCustomizer start. Input 3 num:"))  # 从键盘获取三种题的数量
            self.testCustomizer(buffer[0], buffer[1], buffer[2])
            self.__testQuestionListGenerator()
        else:
            self.__needCustomizer = False
            self.__testQuestionCountGenerator(self.__testScore)  # 自动生成试卷时，需要根据总分生成题目数量
            self.__testQuestionListGenerator()

# 提供只读的属性
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
            self.__TestScore = self.__SingleChoiceCount * 3 + self.__FillBlankCount * 2 + self.__TrueFalseCount  # 计算总分
            self.__needCustomizer = False

    def __testQuestionCountGenerator(self, score):  # 题目数量计算，接受从10到100的总分
        if score < 10:
            raise GeneratorError("score < 10", "试卷总分太少。给谁考试呢这是？")
        elif score < 20:
            self.__TrueFalseCount = score % 5
            self.__FillBlankCount = self.__SingleChoiceCount = int(score / 5)
        elif score <= 100:
            self.__TrueFalseCount = score % 10 + 10
            self.__FillBlankCount = self.__SingleChoiceCount = int((score - self.__TrueFalseCount) / 5)
        elif score > 100 or score < 0:
            raise GeneratorError("score > 100 or score < 0", "😅")
        self.questionTotalCount = self.__SingleChoiceCount+self.__FillBlankCount+self.__TrueFalseCount

    def __testQuestionListGenerator(self):
        question_list = [[self.__SingleChoiceList, self.__SingleChoiceCount, SingleChoiceLibCount],
                         [self.__FillBlankList, self.__FillBlankCount, FillBlankLibCount],
                         [self.__TrueFalseList, self.__TrueFalseCount, TrueFalseLibCount]]
        # 打包数据提供给QuestionListGenerator使用

        for i in question_list:
            QuestionListGenerator(i)

    def examContentGenerator(self):
        questionNoList = [[self.SingleChoiceList, 'Single_choice'], [self.FillBlankList, 'Fill_in_the_blank'],
                          [self.TrueFalseList, 'True_or_False']]  # 打包一个题目表传入答案生成函数
        questionContent = []
        no=0
        for questionKind in questionNoList:  # questionNolist的结构为List[List[Union[list, str]]]
            for questionNo in questionKind[0]:
                QuestionContent = open(
                    'Database\\' + questionKind[1] + '\\' + str(
                        questionNo) + '.txt',  # questionKind[1]为一个字符串，包含有文件夹的名字
                    'r')
                questionContent[no].append(questionKind[1])
                questionContent[no].append(QuestionContent.readlines()[0])
                questionContent[no].append(QuestionContent.readlines()[1])
                questionContent[no].append(QuestionContent.readlines()[2])
                questionContent[no].append(QuestionContent.readlines()[3])
                questionContent[no].append(QuestionContent.readlines()[4])
                no+=1

        return questionContent
