import wx


class GUI(wx.Frame):
    def __init__(self, examTitle):
        super().__init__(parent=None, title=examTitle, size=wx.Size(1280, 600))
        self.panel = wx.Panel(self)
        self.titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.ContentSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.AllSizer = wx.BoxSizer(wx.VERTICAL)

    def displayQuestionNo(self, questionNo):
        No = wx.StaticText(self.panel, 0, label=questionNo, style=wx.TE_LEFT)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        No.SetFont(font)
        self.titleSizer.Add(No, 0, flag=wx.ALL, border=15)

    def displayQuestionKind(self, questionKind):
        kind = wx.StaticText(self.panel, 0, label=questionKind, style=wx.TE_LEFT)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        kind.SetFont(font)
        self.titleSizer.Add(kind, 1, flag=wx.EXPAND | wx.ALL, border=15)

    def displayQuestionFillBlank(self, questionContent):
        tips = wx.StaticText(self.panel, 0, label="题目：", style=wx.TE_LEFT)
        content = wx.StaticText(self.panel, 0, label=questionContent, style=wx.TE_LEFT)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        content.SetFont(font)
        content.Wrap(0)
        tips.SetFont(font)
        self.ContentSizer.Add(tips, 0, wx.ALL, 15)
        self.ContentSizer.Add(content, 1, wx.EXPAND | wx.ALL, 15)

    def displayQuestionTrueFalse(self, questionContent):
        tips = wx.StaticText(self.panel, 0, label="题目：", style=wx.TE_LEFT)
        content = wx.StaticText(self.panel, 0, label=questionContent, style=wx.TE_LEFT)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        content.SetFont(font)
        content.Wrap(0)
        tips.SetFont(font)
        self.ContentSizer.Add(tips, 0, wx.ALL, 15)
        self.ContentSizer.Add(content, 1, wx.EXPAND | wx.ALL, 15)

    def displaySizer(self):
        self.AllSizer.Add(self.titleSizer, 0, flag=wx.ALL, border=5)
        self.AllSizer.Add(self.ContentSizer, 1, flag=wx.ALL, border=5)
        self.panel.SetSizer(self.AllSizer)
