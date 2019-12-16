import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="vbox",size=(800,600),pos=(10,10))   #继承wx.Frame类
        self.Center()

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

