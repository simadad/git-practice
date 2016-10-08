import wx
app = wx.App()
windows = wx.Frame(None, title='Tic Tac Top', size=(400, 400))
panel = wx.Panel(windows)
# box = wx.BoxSizer(wx.HORIZONTAL)
# butts = []
wx.Button(panel, -1, '0')
wx.Button(panel, 1, '1')
# box.Add(butts[i])
# windows.Show(True)
word = wx.StaticText(panel, label='hallo world', pos=(150, 150))
windows.Show(True)
app.MainLoop()
