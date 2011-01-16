import wx

class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        
        topsizer = wx.BoxSizer( wx.HORIZONTAL )
        # topsizer = wx.GridSizer(1, 2)

        menusizer = wx.BoxSizer( wx.VERTICAL )
        # menusizer = wx.GridSizer(4, 1)
        contentsizer = wx.BoxSizer( wx.VERTICAL )
        
        self.textbox = wx.TextCtrl(
            self, -1, "",
            wx.DefaultPosition, wx.DefaultSize,
            wx.TE_MULTILINE)
        
        self.textbox.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD))

        button1 = wx.Button(self, 1001, "Say hello")
        button2 = wx.Button(self, 1002, "Say hello again")
        button3 = wx.Button(self, 1003, "Clear")
        button4 = wx.Button(self, 1004, "Quit")
        
        button1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        button2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        button3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))  
        button4.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))

        wx.EVT_BUTTON(self, 1001, self.ButtonOnePressed)
        wx.EVT_BUTTON(self, 1002, self.ButtonTwoPressed)
        wx.EVT_BUTTON(self, 1003, self.ButtonThreePressed)
        wx.EVT_BUTTON(self, 1004, self.ButtonFourPressed)
        
        # topsizer.Add(self.textbox, 2, wx.ALL, 10)
        contentsizer.Add(self.textbox, 1, wx.EXPAND)

        self.label1 = wx.StaticText(self, -1, 'Enter the name of the movie',wx.DefaultPosition, wx.DefaultSize)
        self.searchtextbox = wx.TextCtrl(self, -1, "",wx.DefaultPosition, wx.DefaultSize)
        
        
        # The arg 1 and wx.EXPAND makes the
        # button fill the left-over space.
        menusizer.Add(self.label1,1, wx.EXPAND)
        menusizer.Add(self.searchtextbox,1, wx.EXPAND)
        menusizer.Add(button1, 1, wx.EXPAND)
        menusizer.Add(button2, 1, wx.EXPAND)
        menusizer.Add(button3, 1, wx.EXPAND)
        menusizer.Add(button4, 1, wx.EXPAND)

        topsizer.Add(menusizer, 0)
        topsizer.Add(contentsizer, 1, wx.EXPAND)
        
        self.SetSizer(topsizer)

    def ButtonOnePressed(self, event):
		
        self.textbox.AppendText(self.searchtextbox.GetValue())
        # print "ID is", wx.NewId()
        
    def ButtonTwoPressed(self, event):
        self.textbox.SetValue("Hello again")
        
    def ButtonThreePressed(self, event):
        self.textbox.Clear()
        
    def ButtonFourPressed(self, event):
        # print "Parent", self.GetParent()
        self.GetParent().Close(True)

# Start the program
app = wx.PySimpleApp(0)
frame = wx.Frame(None, -1, "Layout Example")
MyPanel(frame)
frame.Show(True)
frame.SetSize(wx.Size(800, 600))
frame.Move(wx.Point(50,50))
app.MainLoop()
