#Boa:FramePanel:wxDemoPanel

from wxPython.wx import *

[wxID_WXDEMOPANEL] = map(lambda _init_ctrls: wxNewId(), range(1))

class wxDemoPanel(wxPanel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxPanel.__init__(self, id=wxID_WXDEMOPANEL, name='wxDemoPanel',
              parent=prnt, pos=wxPoint(444, 305), size=wxSize(556, 243),
              style=0)
        self.SetClientSize(wxSize(556, 243))
        self.SetToolTipString('Demo panel')

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
