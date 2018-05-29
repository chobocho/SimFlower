import wx
import FlowerParser
import FlowerParser2

class SimFlowerPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(SimFlowerPanel, self).__init__(*args, **kw)
        self.drawUI()

    def onClearOrder(self, evt):
        print ("onClearOrder")
        self.orderText.SetValue("")
        self.orderName.SetValue("")
        self.orderPhone.SetValue("")
        self.RecvName.SetValue("")
        self.RecvPhone.SetValue("")
        self.RecvDate.SetValue("")
        self.RecvTime.SetValue("")
        self.RecvMsg.SetValue("")
        self.PresentName.SetValue("")
        self.Product.SetValue("")
        self.Address.SetValue("")

    def onParsing(self, evt):
        orderData = self.orderText.GetValue()
        if (orderData.find("1. 보내시는분") != -1):
            self.onParingType2(orderData)
        else:
            self.onParingType1(orderData)


    def onParingType1(self, orderText):
        print ("onParsing1")
        flowerParser = FlowerParser.FlowerParser()
        order = flowerParser.parse(orderText)
        print (order)
        self.orderName.SetValue(order[0])
        self.orderPhone.SetValue(order[1])
        self.RecvName.SetValue(order[2])
        self.RecvPhone.SetValue(order[3])
        self.RecvDate.SetValue(order[4])
        self.RecvTime.SetValue(order[5])
        self.RecvMsg.SetValue(order[6])
        self.PresentName.SetValue(order[7])
        self.Product.SetValue(order[8])
        self.Address.SetValue(order[9])

    def onParingType2(self, orderText):
        print ("onParsing2")
        flowerParser = FlowerParser2.FlowerParser2()
        order = flowerParser.parse(orderText)

        print (order)
        self.orderName.SetValue(order[0])
        self.orderPhone.SetValue(order[1])
        self.RecvName.SetValue(order[2])
        self.RecvPhone.SetValue(order[3])
        self.RecvDate.SetValue(order[4])
        self.RecvTime.SetValue(order[5])
        self.RecvMsg.SetValue(order[6])
        self.PresentName.SetValue(order[7])
        self.Address.SetValue(order[9])


    def onCopyOrderName(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.orderName.GetValue()
        print ("onCopyOrderName " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyOrderPhone(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.orderPhone.GetValue()
        print ("onCopyOrderPhone " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyRecvName(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.RecvName.GetValue()
        print ("onCopyRecvName " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyRecvPhone(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.RecvPhone.GetValue()
        print ("onCopyRecvPhone " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyRecvDate(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.RecvDate.GetValue()
        print ("onCopyRecvDate " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyRecvTime(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.RecvTime.GetValue()
        print ("onCopyRecvTime " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyRecvMsg(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.RecvMsg.GetValue()
        print ("onCopyRecvMsg " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyPresentName(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.PresentName.GetValue()
        print ("onCopyPresentName " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyProduct(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.Product.GetValue()
        print ("onCopyProduct " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def onCopyAddress(self, evt):
        wx.TheClipboard.Open()
        selectedData = self.Address.GetValue()
        print ("onCopyAddress " + selectedData)
        wx.TheClipboard.SetData(wx.TextDataObject(selectedData))
        wx.TheClipboard.Close()

    def drawUI(self):
        print ("drawUI")
        sizer = wx.BoxSizer(wx.VERTICAL)

        ##
        OrderBox = wx.BoxSizer(wx.VERTICAL)

        self.orderText = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER | wx.TE_MULTILINE,size=(500,300))
        self.orderText.Bind(wx.EVT_TEXT_ENTER, self.onParsing)
        self.orderText.SetValue("")
        OrderBox.Add(self.orderText, 1, wx.EXPAND)
        sizer.Add(OrderBox, 1, wx.EXPAND)

        ##
        orderBtnBox = wx.BoxSizer(wx.HORIZONTAL)

        self.parseBtn = wx.Button(self, 10, "분석", size=(30,30))
        self.parseBtn.Bind(wx.EVT_BUTTON, self.onParsing)
        orderBtnBox.Add(self.parseBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.clearBtn = wx.Button(self, 10, "Clear", size=(30,30))
        self.clearBtn.Bind(wx.EVT_BUTTON, self.onClearOrder)
        orderBtnBox.Add(self.clearBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(orderBtnBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        #orderName
        orderNameBox = wx.BoxSizer(wx.HORIZONTAL)

        self.orderName = wx.TextCtrl(self, size=(470,25))
        orderNameBox.Add(self.orderName, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.orderNameCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.orderNameCCBtn.Bind(wx.EVT_BUTTON, self.onCopyOrderName)
        orderNameBox.Add(self.orderNameCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(orderNameBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        #orderPhone
        orderPhoneBox = wx.BoxSizer(wx.HORIZONTAL)

        self.orderPhone = wx.TextCtrl(self, size=(470,25))
        orderPhoneBox.Add(self.orderPhone, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.orderPhoneCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.orderPhoneCCBtn.Bind(wx.EVT_BUTTON, self.onCopyOrderPhone)
        orderPhoneBox.Add(self.orderPhoneCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(orderPhoneBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
      
        #RecvName   
        RecvNameBox = wx.BoxSizer(wx.HORIZONTAL)

        self.RecvName = wx.TextCtrl(self, size=(470,25))
        RecvNameBox.Add(self.RecvName, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.RecvNameCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.RecvNameCCBtn.Bind(wx.EVT_BUTTON, self.onCopyRecvName)
        RecvNameBox.Add(self.RecvNameCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(RecvNameBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
      
        #RecvPhone  
        RecvPhoneBox = wx.BoxSizer(wx.HORIZONTAL)

        self.RecvPhone = wx.TextCtrl(self, size=(470,25))
        RecvPhoneBox.Add(self.RecvPhone, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.RecvPhoneCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.RecvPhoneCCBtn.Bind(wx.EVT_BUTTON, self.onCopyRecvPhone)
        RecvPhoneBox.Add(self.RecvPhoneCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(RecvPhoneBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        #RecvDate   
        RecvDateBox = wx.BoxSizer(wx.HORIZONTAL)

        self.RecvDate = wx.TextCtrl(self, size=(470,25))
        RecvDateBox.Add(self.RecvDate, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.RecvDateCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.RecvDateCCBtn.Bind(wx.EVT_BUTTON, self.onCopyRecvDate)
        RecvDateBox.Add(self.RecvDateCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(RecvDateBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        #RecvTime   
        RecvTimeBox = wx.BoxSizer(wx.HORIZONTAL)

        self.RecvTime = wx.TextCtrl(self, size=(470,25))
        RecvTimeBox.Add(self.RecvTime, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.RecvTimeCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.RecvTimeCCBtn.Bind(wx.EVT_BUTTON, self.onCopyRecvTime)
        RecvTimeBox.Add(self.RecvTimeCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(RecvTimeBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        #RecvMsg    
        RecvMsgBox = wx.BoxSizer(wx.HORIZONTAL)

        self.RecvMsg = wx.TextCtrl(self, size=(470,25))
        RecvMsgBox.Add(self.RecvMsg, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.RecvMsgCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.RecvMsgCCBtn.Bind(wx.EVT_BUTTON, self.onCopyRecvMsg)
        RecvMsgBox.Add(self.RecvMsgCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(RecvMsgBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        #PresentName
        PresentNameBox = wx.BoxSizer(wx.HORIZONTAL)

        self.PresentName = wx.TextCtrl(self, size=(470,25))
        PresentNameBox.Add(self.PresentName, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.PresentNameCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.PresentNameCCBtn.Bind(wx.EVT_BUTTON, self.onCopyPresentName)
        PresentNameBox.Add(self.PresentNameCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(PresentNameBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        #Product    
        ProductBox = wx.BoxSizer(wx.HORIZONTAL)

        self.Product = wx.TextCtrl(self, size=(470,25))
        ProductBox.Add(self.Product, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.ProductCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.ProductCCBtn.Bind(wx.EVT_BUTTON, self.onCopyProduct)
        ProductBox.Add(self.ProductCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(ProductBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        #Address    
        AddressBox = wx.BoxSizer(wx.HORIZONTAL)

        self.Address = wx.TextCtrl(self, style = wx.TE_MULTILINE, size=(470,50))
        AddressBox.Add(self.Address, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.AddressCCBtn = wx.Button(self, 10, "Copy", size=(30,25))
        self.AddressCCBtn.Bind(wx.EVT_BUTTON, self.onCopyAddress)
        AddressBox.Add(self.AddressCCBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(AddressBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        ##
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
