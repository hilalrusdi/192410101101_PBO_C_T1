import wx
import noname

app = wx.App()
login = noname.MyFrame2(parent=None)
login.Show()
app.MainLoop()
