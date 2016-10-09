import wx
app = wx.App()
windows = wx.Frame(None, title='Tic Tac Top', size=(400, 400))
panel = wx.Panel(windows, size=(300, 300), pos=(50, 50))


class Squares(wx.Button):
    def __init__(self, parent, ii, jj):
        wx.Button.__init__(self, parent, 1, '', size=(100, 100), pos=(50+100*(jj-1), 25+100*(ii-1)))
        self.chess = 0
        self.Bind(wx.EVT_BUTTON, self.click)

    def click(self, e):
        global t
        t += 1
        print t

        if t % 2 == 0:
            self.chess = 2
            self.BackgroundColour = 'red'
            print self.chess
        else:
            self.chess = 1
            self.BackgroundColour = 'blue'
            print self.chess
t = 0
for i in range(1, 4):
    for j in range(1, 4):
        square = Squares(panel, i, j)

windows.Show(True)
app.MainLoop()
