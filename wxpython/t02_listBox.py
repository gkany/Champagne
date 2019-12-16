import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="vbox",size=(800,600),pos=(10,10))   #继承wx.Frame类
        self.Center()

        panel = wx.Panel(self)
        self.textFont = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        listDatas = [u'ListBox是简单的列表', u'TreeCtrl是树状文件目录机构', u'ListCtrl复杂的列表',
                    u'RadioButton是单选项', u'CheckBox为多选项', u'StaticText显示静态文本', u'test 2019-12-15 20:18:27']
        self.listBox = wx.ListBox(panel, -1, pos=(10, 10), size=(300, 120), choices=listDatas, style=wx.LB_SINGLE)
        self.listBox.SetFont(self.textFont)
        self.Bind(wx.EVT_LISTBOX, self.listCtrlSelectFunc, self.listBox)

    def listCtrlSelectFunc(self, event):
        indexSelected = event.GetEventObject().GetSelection()
        print('select item index: {}'.format(indexSelected))
        pass

class App(wx.App):
    def OnInit(self):    #进入
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):   #退出
        print("tuichu")
        return 0

if __name__ == '__main__':
    app=App()
    app.MainLoop()

