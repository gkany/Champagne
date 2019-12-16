import wx
from xGridTable import StudentInfoGridTable

import wx
# from hzpdata import finddata
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="vbox",size=(800,600),pos=(10,10))   #继承wx.Frame类
        self.Center()
        panel = wx.Panel(parent=self)   #面板

        gridDatas = [
            [u'大仲马', u'男', u'WUST', u'中文', u'研三'],
            [u'牛顿', u'男', u'HUST', u'物理', u'博一'],
            [u'爱因斯坦', u'男', u'HUST', u'物理', u'研一'],
            [u'居里夫人', u'女', u'WUST', u'化学', u'研一'],
        ]
        self.gridTable = wx.grid.Grid(panel, -1, pos=(10, 10), size=(700, 500), style=wx.WANTS_CHARS)
        self.infoTable = StudentInfoGridTable(gridDatas)
        self.gridTable.SetTable(self.infoTable, True)


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

