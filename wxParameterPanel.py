#Boa:FramePanel:wxParameterPanel

from wxPython.wx import *
from wxPython.grid import *

[wxID_WXPARAMETERPANEL, wxID_WXPARAMETERPANELPARAMETERFXSPLITTER, 
 wxID_WXPARAMETERPANELPARAMETERSPLITTER, wxID_WXPARAMETERPANELPARAMGRID, 
 wxID_WXPARAMETERPANELPARAMLISTBOX, wxID_WXPARAMETERPANELWINDOW1, 
] = map(lambda _init_ctrls: wxNewId(), range(6))

class wxParameterPanel(wxPanel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxPanel.__init__(self, id=wxID_WXPARAMETERPANEL,
              name='wxParameterPanel', parent=prnt, pos=wxPoint(243, 140),
              size=wxSize(744, 468), style=0)
        self.SetClientSize(wxSize(744, 468))
        self.SetToolTipString('Parameter Panel')
        EVT_SIZE(self, self.OnWxParameterPanelSize)

        self.parameterSplitter = wxSplitterWindow(id=wxID_WXPARAMETERPANELPARAMETERSPLITTER,
              name='parameterSplitter', parent=self, point=wxPoint(0, 0),
              size=wxSize(744, 468), style=wxSP_3D)
        self.parameterSplitter.SetToolTipString('Parameter Splitter')
        self.parameterSplitter.SetMinimumPaneSize(200)

        self.parameterFXSplitter = wxSplitterWindow(id=wxID_WXPARAMETERPANELPARAMETERFXSPLITTER,
              name='parameterFXSplitter', parent=self.parameterSplitter,
              point=wxPoint(2, 2), size=wxSize(200, 100), style=wxSP_3D)
        self.parameterFXSplitter.SetMinimumPaneSize(150)

        self.window1 = wxWindow(id=wxID_WXPARAMETERPANELWINDOW1, name='window1',
              parent=self.parameterSplitter, pos=wxPoint(209, 2),
              size=wxSize(533, 464), style=0)
        self.parameterSplitter.SplitVertically(self.parameterFXSplitter,
              self.window1, 200)

        self.paramListBox = wxListBox(choices=[],
              id=wxID_WXPARAMETERPANELPARAMLISTBOX, name='paramListBox',
              parent=self.parameterFXSplitter, pos=wxPoint(2, 2),
              size=wxSize(196, 150), style=wxLB_SINGLE)

        self.paramGrid = wxGrid(id=wxID_WXPARAMETERPANELPARAMGRID,
              name='paramGrid', parent=self.parameterFXSplitter, pos=wxPoint(2,
              159), size=wxSize(196, 303), style=0)
        self.paramGrid.SetColLabelSize(0)
        self.paramGrid.SetRowLabelSize(100)
        self.paramGrid.SetRowMinimalAcceptableHeight(100)
        self.parameterFXSplitter.SplitHorizontally(self.paramListBox,
              self.paramGrid, 152)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
        
        #TODO: Manage grid control
        self.paramGrid.CreateGrid(2,1)
        self.paramGrid.SetRowLabelValue(0,"hola")
        self.paramGrid.SetRowLabelValue(1,"holita")

    def OnWxParameterPanelSize(self, event):
        panelDC = wxClientDC(self)
        panelSize = panelDC.GetSize()
        self.parameterSplitter.SetSize(panelSize)
        
        event.Skip()
