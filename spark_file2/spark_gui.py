import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)
        self.check1_ok=0
        self.check2_ok=0
        self.check3_ok=0
        self.InitUI()
        self.Centre()

    def InitUI(self):
        
        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel)
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('ssw.png'))
        sizer.Add(icon, pos=(0, 2), flag=wx.LEFT|wx.CENTRE,border=30)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="예            산")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        self.tc1 = wx.TextCtrl(panel)
        sizer.Add(self.tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
        text4 = wx.StaticText(panel, label="지            역")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

        self.combo = wx.ComboBox(panel,choices=
        ['서울-강북지역','서울-강남지역','경기','인천',
        '부산','대구','광주','대전','울산','세종','강원',
        '충북','충남','전북','전남','경북','경남','제주']
        )
        sizer.Add(self.combo, pos=(4, 1), span=(1, 3),
            flag=wx.TOP|wx.EXPAND, border=5)
        self.Bind(wx.EVT_COMBOBOX,self.OnSelect,self.combo);
        sb = wx.StaticBox(panel, label="옵    션")

        self.check1 = wx.CheckBox(panel,-1,"김")
        self.check2 = wx.CheckBox(panel,-1,"이")
        self.check3 = wx.CheckBox(panel,-1,"주")
        self.Bind(wx.EVT_CHECKBOX,self.OnCheck1,self.check1)
        self.Bind(wx.EVT_CHECKBOX,self.OnCheck2,self.check2)
        self.Bind(wx.EVT_CHECKBOX,self.OnCheck3,self.check3)
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(self.check1,flag=wx.LEFT, border=5)
        boxsizer.Add(self.check2,flag=wx.LEFT, border=5)
        boxsizer.Add(self.check3,flag=wx.LEFT|wx.BOTTOM, border=5)
            
        sizer.Add(boxsizer, pos=(5, 0), span=(1, 5),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        button3 = wx.Button(panel, label='Help')
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)

        self.button4 = wx.Button(panel, label="Ok")
        sizer.Add(self.button4, pos=(7, 3))
        self.Bind(wx.EVT_BUTTON,self.OnOkButton,self.button4)
        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(7, 4), span=(1, 1),
            flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)

    def OnSelect(self,event):
        self.region=self.combo.GetValue()
        print(self.region)
    def OnCheck1(self,event):
        self.check1_ok=int(self.check1.GetValue())
        print(self.check1_ok)
    def OnCheck2(self,event):
        self.check2_ok=int(self.check2.GetValue())
        print(self.check2_ok)
    def OnCheck3(self,event):
        self.check3_ok=int(self.check3.GetValue())
        print(self.check3_ok)
    def OnOkButton(self,event):
        self.yesan=self.tc1.GetValue()
        print("예산 : %s 지역 : %s 옵션 : %d %d %d"%(self.yesan,self.region,self.check1_ok,self.check2_ok,self.check3_ok))
        import j_m
        j_m.run()
class MyApp(wx.App):
    def OnInit(self):
        self.frame = Example(None, "select the option")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()

# def main():
#     app = wx.App()
#     ex = Example(None, title="Prediction")
#     ex.Show()
#     app.MainLoop()

# if __name__ == '__main__':
#     main()