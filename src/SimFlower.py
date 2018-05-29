import wx
import SimFlowerPanel
'''
Start  : 2017.05.13
Update : 2018.05.13a
'''

SW_TITLE = "SimFlower V0627.0530a"

class SimFlowerFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(SimFlowerFrame, self).__init__(*args, **kw)

        ctrl_Q_Id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onClose, id=ctrl_Q_Id)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('Q'), ctrl_Q_Id )])
        self.SetAcceleratorTable(accel_tbl)

        self.SimFlowerPanel = SimFlowerPanel.SimFlowerPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.SimFlowerPanel, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def onFind(self, event):
        dlg = wx.TextEntryDialog(None, 'Input keyword','Find')
        dlg.SetValue("")

        if dlg.ShowModal() == wx.ID_OK:
            keyword = dlg.GetValue()
            #self.SimFlowerPanel.onFind(keyword)
        dlg.Destroy()

    def onClose(self, event):
        self.Close()

def main(): 
    app = wx.App()
    frm = SimFlowerFrame(None, title=SW_TITLE, size=(600,800))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()