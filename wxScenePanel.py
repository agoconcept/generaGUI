#Boa:FramePanel:wxScenePanel

from wxPython.wx import *

[wxID_WXSCENEPANEL] = map(lambda _init_ctrls: wxNewId(), range(1))

class wxScenePanel(wxPanel):
    def _init_utils(self):
        # generated method, don't edit
        pass

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxPanel.__init__(self, id=wxID_WXSCENEPANEL, name='wxScenePanel',
              parent=prnt, pos=wxPoint(82, 695), size=wxSize(200, 100),
              style=0)
        self._init_utils()
        self.SetClientSize(wxSize(200, 100))
        self.SetToolTipString('Scene Panel')

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
