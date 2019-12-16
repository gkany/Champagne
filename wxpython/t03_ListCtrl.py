#coding=utf-8

import wx
from xListCtrl import CourseListCtrl

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="vbox",size=(500,200),pos=(10,10))   #继承wx.Frame类
        self.Center()

        courseNames = [u'大学物理', u'计算机技术', u'微积分', u'电力电子']
        courseDatas = []
        for index in range(len(courseNames)):
            obj = {}
            obj['name'] = courseNames[index]
            obj['intro'] = courseNames[index]+u'的简介......'
            courseDatas.append(obj)

        self.textFont = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.courseListCtrl = CourseListCtrl(self, courseDatas, size=(70, 50), pos=(10, 10))
        self.courseListCtrl.SetFont(self.textFont)
        self.courseListCtrl.SetBackgroundColour('#ffffff')
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.courseListSelectFunc, self.courseListCtrl)

    def courseListSelectFunc(self, event):
        index = event.GetIndex()
        print(u'select item index: {}'.format(index))
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

