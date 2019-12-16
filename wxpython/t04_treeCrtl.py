import wx
from xTreeCtrl import CollegeTreeListCtrl

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="vbox",size=(800,600),pos=(10,10))   #继承wx.Frame类
        self.Center()

        self.treeListCtrl = CollegeTreeListCtrl(parent=self, pos=(-1, 39), size=(300, 300))
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnTreeListCtrlClickFunc, self.treeListCtrl)

        self.colleges = {
            u'Beijing': [
                {'collegeName': u'北京大学', 'if_985_type':u'是', 'collegeType':u'综合类'},
                {'collegeName': u'清华大学', 'if_985_type': u'是', 'collegeType': u'理工类'},
                {'collegeName': u'北京邮电大学', 'if_985_type': u'否', 'collegeType': u'理工类'}],
            u'Wuhan':[
                {'collegeName': u'武汉大学', 'if_985_type': u'是', 'collegeType': u'综合类'},
                {'collegeName': u'华中科技大学', 'if_985_type': u'是', 'collegeType': u'理工类'}
            ],
            u'Shanghai': [
                {'collegeName': u'上海交通大学', 'if_985_type': u'是', 'collegeType': u'理工类'},
                {'collegeName': u'复旦大学', 'if_985_type': u'是', 'collegeType': u'综合类'},
                {'collegeName': u'同济大学', 'if_985_type': u'是', 'collegeType': u'综合类'}
            ]
        }

        # TreeCtrl显示数据接口
        self.treeListCtrl.refreshDataShow(self.colleges)

    def OnTreeListCtrlClickFunc(self, event):
        if self.treeListCtrl.GetItemData(event.GetItem()) != None:
            # 当前选中的TreeItemId对象，方便进行删除等其他的操作
            self.currentTreeItemId = event.GetItem()
            cityName, collegeIndex = str(self.treeListCtrl.GetItemData(event.GetItem()).GetData()).split("|")
            collegeObj = self.colleges.get(cityName, [])[int(collegeIndex)]
            print('click: ', cityName +u" de "+collegeObj.get('collegeName', ''))
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

