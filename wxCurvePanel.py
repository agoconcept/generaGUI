#Boa:FramePanel:wxCurvePanel

from wxPython.wx import *
from struct import *
import pickle

MAX_POINTS = 128

[wxID_WXCURVEPANEL, wxID_WXCURVEPANELBUTTONDELETE, 
 wxID_WXCURVEPANELBUTTONENDPOINT, wxID_WXCURVEPANELBUTTONREFINE, 
 wxID_WXCURVEPANELBUTTONVISIBLE, wxID_WXCURVEPANELCHECKBOXCONTROLPOINTS, 
 wxID_WXCURVEPANELCHECKBOXNUMBERS, wxID_WXCURVEPANELCHECKBOXTANGENTS, 
 wxID_WXCURVEPANELCURSORPOSITION, wxID_WXCURVEPANELCURVE, 
 wxID_WXCURVEPANELRADIOBUTTONFILLED, wxID_WXCURVEPANELRADIOBUTTONSPLINE, 
 wxID_WXCURVEPANELSPINCTRLSEGMENTS, wxID_WXCURVEPANELSPINCTRLWIDTH, 
 wxID_WXCURVEPANELSTATICBOXMODE, wxID_WXCURVEPANELSTATICBOXPROPERTIES, 
 wxID_WXCURVEPANELSTATICBOXSHOW, wxID_WXCURVEPANELSTATICTEXTHELP, 
 wxID_WXCURVEPANELSTATICTEXTSEGMENTS, wxID_WXCURVEPANELSTATICTEXTWIDTH, 
] = map(lambda _init_ctrls: wxNewId(), range(20))

class wxCurvePanel(wxPanel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxPanel.__init__(self, id=wxID_WXCURVEPANEL, name='wxCurvePanel',
              parent=prnt, pos=wxPoint(358, 187), size=wxSize(594, 449),
              style=0)
        self.SetClientSize(wxSize(594, 449))
        self.SetToolTipString('Curve panel')
        EVT_SIZE(self, self.OnWxcurvepanelSize)

        self.curve = wxWindow(id=wxID_WXCURVEPANELCURVE, name='curve',
              parent=self, pos=wxPoint(8, 8), size=wxSize(264, 264),
              style=wxSIMPLE_BORDER)
        self.curve.SetToolTipString('Curve editor')
        EVT_LEFT_DOWN(self.curve, self.OnCurveLeftDown)
        EVT_LEFT_UP(self.curve, self.OnCurveLeftUp)
        EVT_RIGHT_DOWN(self.curve, self.OnCurveRightDown)
        EVT_PAINT(self.curve, self.OnCurvePaint)
        EVT_MOTION(self.curve, self.OnCurveMotion)

        self.staticTextHelp = wxStaticText(id=wxID_WXCURVEPANELSTATICTEXTHELP,
              label='Help text', name='staticTextHelp', parent=self,
              pos=wxPoint(280, 8), size=wxSize(304, 264),
              style=wxST_NO_AUTORESIZE)
        self.staticTextHelp.SetToolTipString('Help text')

        self.staticBoxShow = wxStaticBox(id=wxID_WXCURVEPANELSTATICBOXSHOW,
              label='Show', name='staticBoxShow', parent=self, pos=wxPoint(200,
              288), size=wxSize(272, 48), style=0)

        self.radioButtonSpline = wxRadioButton(id=wxID_WXCURVEPANELRADIOBUTTONSPLINE,
              label='&Splines', name='radioButtonSpline', parent=self,
              pos=wxPoint(24, 304), size=wxSize(64, 24), style=0)
        self.radioButtonSpline.SetToolTipString('Show splines')
        EVT_RADIOBUTTON(self.radioButtonSpline,
              wxID_WXCURVEPANELRADIOBUTTONSPLINE,
              self.OnRadioButtonSplineRadiobutton)

        self.radioButtonFilled = wxRadioButton(id=wxID_WXCURVEPANELRADIOBUTTONFILLED,
              label='Filled', name='radioButtonFilled', parent=self,
              pos=wxPoint(112, 304), size=wxSize(56, 24), style=0)
        self.radioButtonFilled.SetToolTipString('Show filled curve')
        EVT_RADIOBUTTON(self.radioButtonFilled,
              wxID_WXCURVEPANELRADIOBUTTONFILLED,
              self.OnRadioButtonFilledRadiobutton)

        self.checkBoxTangents = wxCheckBox(id=wxID_WXCURVEPANELCHECKBOXTANGENTS,
              label='&Tangents', name='checkBoxTangents', parent=self,
              pos=wxPoint(208, 304), size=wxSize(72, 24), style=0)
        self.checkBoxTangents.SetToolTipString('Show tangents')
        EVT_CHECKBOX(self.checkBoxTangents, wxID_WXCURVEPANELCHECKBOXTANGENTS,
              self.OnCheckBoxTangentsCheckbox)

        self.checkBoxNumbers = wxCheckBox(id=wxID_WXCURVEPANELCHECKBOXNUMBERS,
              label='&Numbers', name='checkBoxNumbers', parent=self,
              pos=wxPoint(288, 304), size=wxSize(72, 24), style=0)
        self.checkBoxNumbers.SetToolTipString('Show numbers')
        EVT_CHECKBOX(self.checkBoxNumbers, wxID_WXCURVEPANELCHECKBOXNUMBERS,
              self.OnCheckBoxNumbersCheckbox)

        self.checkBoxControlPoints = wxCheckBox(id=wxID_WXCURVEPANELCHECKBOXCONTROLPOINTS,
              label='&Control points', name='checkBoxControlPoints',
              parent=self, pos=wxPoint(368, 304), size=wxSize(96, 24), style=0)
        self.checkBoxControlPoints.SetToolTipString('Show control points')
        EVT_CHECKBOX(self.checkBoxControlPoints,
              wxID_WXCURVEPANELCHECKBOXCONTROLPOINTS,
              self.OnCheckBoxControlPointsCheckbox)

        self.staticBoxProperties = wxStaticBox(id=wxID_WXCURVEPANELSTATICBOXPROPERTIES,
              label='Properties', name='staticBoxProperties', parent=self,
              pos=wxPoint(8, 344), size=wxSize(464, 48), style=0)

        self.staticTextSegments = wxStaticText(id=wxID_WXCURVEPANELSTATICTEXTSEGMENTS,
              label='Segments/curve', name='staticTextSegments', parent=self,
              pos=wxPoint(24, 360), size=wxSize(96, 24), style=0)

        self.spinCtrlSegments = wxSpinCtrl(id=wxID_WXCURVEPANELSPINCTRLSEGMENTS,
              initial=10, max=100, min=1, name='spinCtrlSegments', parent=self,
              pos=wxPoint(128, 360), size=wxSize(120, 22),
              style=wxSP_ARROW_KEYS)
        self.spinCtrlSegments.SetRange(1, 255)
        self.spinCtrlSegments.SetToolTipString('Segments/curve')
        EVT_SPINCTRL(self.spinCtrlSegments, wxID_WXCURVEPANELSPINCTRLSEGMENTS,
              self.OnSpinCtrlSegmentsSpinctrl)

        self.staticTextWidth = wxStaticText(id=wxID_WXCURVEPANELSTATICTEXTWIDTH,
              label='Line width', name='staticTextWidth', parent=self,
              pos=wxPoint(272, 360), size=wxSize(56, 24), style=0)

        self.spinCtrlWidth = wxSpinCtrl(id=wxID_WXCURVEPANELSPINCTRLWIDTH,
              initial=1, max=100, min=1, name='spinCtrlWidth', parent=self,
              pos=wxPoint(336, 360), size=wxSize(120, 22),
              style=wxSP_ARROW_KEYS)
        self.spinCtrlWidth.SetRange(1, 100)
        self.spinCtrlWidth.SetValue(1)
        self.spinCtrlWidth.SetToolTipString('Line width')
        EVT_SPINCTRL(self.spinCtrlWidth, wxID_WXCURVEPANELSPINCTRLWIDTH,
              self.OnSpinCtrlWidthSpinctrl)

        self.buttonDelete = wxButton(id=wxID_WXCURVEPANELBUTTONDELETE,
              label='&Delete', name='buttonDelete', parent=self, pos=wxPoint(16,
              408), size=wxSize(112, 32), style=0)
        EVT_BUTTON(self.buttonDelete, wxID_WXCURVEPANELBUTTONDELETE,
              self.OnButtonDeleteButton)

        self.buttonRefine = wxButton(id=wxID_WXCURVEPANELBUTTONREFINE,
              label='Re&fine', name='buttonRefine', parent=self,
              pos=wxPoint(128, 408), size=wxSize(112, 32), style=0)
        EVT_BUTTON(self.buttonRefine, wxID_WXCURVEPANELBUTTONREFINE,
              self.OnButtonRefineButton)

        self.buttonVisible = wxButton(id=wxID_WXCURVEPANELBUTTONVISIBLE,
              label='Toggle &visible', name='buttonVisible', parent=self,
              pos=wxPoint(240, 408), size=wxSize(112, 32), style=0)
        EVT_BUTTON(self.buttonVisible, wxID_WXCURVEPANELBUTTONVISIBLE,
              self.OnButtonVisibleButton)

        self.buttonEndpoint = wxButton(id=wxID_WXCURVEPANELBUTTONENDPOINT,
              label='Toggle &endpoint', name='buttonEndpoint', parent=self,
              pos=wxPoint(352, 408), size=wxSize(112, 32), style=0)
        EVT_BUTTON(self.buttonEndpoint, wxID_WXCURVEPANELBUTTONENDPOINT,
              self.OnButtonEndpointButton)

        self.cursorPosition = wxStaticText(id=wxID_WXCURVEPANELCURSORPOSITION,
              label='(0, 0)', name='cursorPosition', parent=self,
              pos=wxPoint(272, 256), size=wxSize(128, 16),
              style=0)

        self.staticBoxMode = wxStaticBox(id=wxID_WXCURVEPANELSTATICBOXMODE,
              label='Mode', name='staticBoxMode', parent=self, pos=wxPoint(8,
              288), size=wxSize(176, 48), style=0)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)

        if sys.platform == 'darwin':
            self.staticTextHelp.SetLabel(\
                'SHIFT + Button: Add a new control point\n\n'\
                'On control point:\n'\
                '     Button: Move\n'\
                '     Command + Button: Delete control point\n'\
                '     ALT + Button: Move whole curve\n'\
                '     CTRL + Button: Select\n\n'\
                'On tangents:\n'\
                '     Button: Move\n'\
                '     SHIFT + Button: Horizontal mirror\n'\
                '     Command + Button: Vertical mirror\n'\
                '     ALT + Button: Mirror\n'\
                )
        else:
            self.staticTextHelp.SetLabel(\
                'SHIFT + Left button: Add a new control point\n\n'\
                'On control point:\n'\
                '     Left button: Move\n'\
                '     CTRL + Left button: Delete control point\n'\
                '     ALT + Left button: Move whole curve\n'\
                '     Right button: Select\n\n'\
                'On tangents:\n'\
                '     Left button: Move\n'\
                '     SHIFT + Left button: Horizontal mirror\n'\
                '     CTRL + Left button: Vertical mirror\n'\
                '     ALT + Left button: Mirror\n'\
                )
            
        self.radioButtonSpline.SetValue(TRUE)
        self.radioButtonFilled.SetValue(FALSE)

        self.checkBoxTangents.SetValue(TRUE)
        self.checkBoxNumbers.SetValue(TRUE)
        self.checkBoxControlPoints.SetValue(TRUE)

        self.spinCtrlSegments.SetValue(4)
        
        #Control points
        self.controlPoint = []
        self.leftTangent = []
        self.rightTangent = []

        self.selected = []
        self.selectedPoints = 0
        
        self.visible = []
        self.endPoint = []

        #Init events
        self.pointClicked = self.leftTangentClicked = self.rightTangentClicked = -1

    def OnWxcurvepanelSize(self, event):
        size = self.GetClientSize()
        
        if size.GetWidth() > (size.GetHeight()-160):
            side = size.GetHeight()-160
            size.SetWidth(side-16)
            size.SetHeight(side-16)
        else:
            side = size.GetWidth()
            size.SetWidth(side-16)
            size.SetHeight(side-16)
        
        self.curve.SetSize(size)
        
        position = self.curve.GetPosition()
        position.x += size.GetWidth()
        position.y += size.GetWidth()-16
        self.cursorPosition.SetPosition(position)

        position = self.staticTextHelp.GetPosition()
        position.x = size.GetWidth()+16
        self.staticTextHelp.SetPosition(position)
        helpSize = wxSize(self.GetClientSize().GetWidth()-position.x-8, size.GetHeight())
        self.staticTextHelp.SetSize(helpSize)
        
        position = self.staticBoxMode.GetPosition()
        position.y = size.GetHeight()+16
        self.staticBoxMode.SetPosition(position)

        position = self.radioButtonSpline.GetPosition()
        position.y = size.GetHeight()+32
        self.radioButtonSpline.SetPosition(position)

        position = self.radioButtonFilled.GetPosition()
        position.y = size.GetHeight()+32
        self.radioButtonFilled.SetPosition(position)
        
        position = self.staticBoxShow.GetPosition()
        position.y = size.GetHeight()+16
        self.staticBoxShow.SetPosition(position)

        position = self.checkBoxTangents.GetPosition()
        position.y = size.GetHeight()+32
        self.checkBoxTangents.SetPosition(position)

        position = self.checkBoxNumbers.GetPosition()
        position.y = size.GetHeight()+32
        self.checkBoxNumbers.SetPosition(position)

        position = self.checkBoxControlPoints.GetPosition()
        position.y = size.GetHeight()+32
        self.checkBoxControlPoints.SetPosition(position)
        
        position = self.staticBoxProperties.GetPosition()
        position.y = size.GetHeight()+72
        self.staticBoxProperties.SetPosition(position)

        position = self.staticTextSegments.GetPosition()
        position.y = size.GetHeight()+88
        self.staticTextSegments.SetPosition(position)

        position = self.spinCtrlSegments.GetPosition()
        position.y = size.GetHeight()+88
        self.spinCtrlSegments.SetPosition(position)

        position = self.staticTextWidth.GetPosition()
        position.y = size.GetHeight()+88
        self.staticTextWidth.SetPosition(position)

        position = self.spinCtrlWidth.GetPosition()
        position.y = size.GetHeight()+88
        self.spinCtrlWidth.SetPosition(position)

        position = self.buttonDelete.GetPosition()
        position.y = size.GetHeight()+136
        self.buttonDelete.SetPosition(position)
        
        position = self.buttonRefine.GetPosition()
        position.y = size.GetHeight()+136
        self.buttonRefine.SetPosition(position)
        
        position = self.buttonVisible.GetPosition()
        position.y = size.GetHeight()+136
        self.buttonVisible.SetPosition(position)
        
        position = self.buttonEndpoint.GetPosition()
        position.y = size.GetHeight()+136
        self.buttonEndpoint.SetPosition(position)
        
        event.Skip()

    def Redraw(self):
        None
        
    def getControlPoint(self, position, size):
        scaleX = (4*256) / float(size.x)
        scaleY = (4*256) / float(size.y)

        for i in range(0,len(self.controlPoint)):
            if position.x >= self.controlPoint[i].x-scaleX and \
               position.x < self.controlPoint[i].x+scaleX and \
               position.y >= self.controlPoint[i].y-scaleY and \
               position.y < self.controlPoint[i].y+scaleY:
                    return i
        
        return -1

    def getLeftTangent(self, position, size):
        scaleX = (4*256) / float(size.x)
        scaleY = (4*256) / float(size.y)

        for i in range(0,len(self.leftTangent)):
            if position.x >= self.leftTangent[i].x-scaleX and \
               position.x < self.leftTangent[i].x+scaleX and \
               position.y >= self.leftTangent[i].y-scaleY and \
               position.y < self.leftTangent[i].y+scaleY:
                    return i
        
        return -1

    def getRightTangent(self, position, size):
        scaleX = (4*256) / float(size.x)
        scaleY = (4*256) / float(size.y)

        for i in range(0,len(self.rightTangent)):
            if position.x >= self.rightTangent[i].x-scaleX and \
               position.x < self.rightTangent[i].x+scaleX and \
               position.y >= self.rightTangent[i].y-scaleY and \
               position.y < self.rightTangent[i].y+scaleY:
                    return i
        
        return -1

    def OnCurveLeftDown(self, event):
        position = event.GetPosition()
        
        curveDC = wxClientDC(self.curve)
        size = curveDC.GetSize()
        
        position = wxPoint((position.x*256) / size.x, (position.y*256) / size.y)

        pointClicked = self.getControlPoint(position, size)
        leftTangentClicked = self.getLeftTangent(position, size)
        rightTangentClicked = self.getRightTangent(position, size)
        if pointClicked > -1 and self.checkBoxControlPoints.GetValue():
            if sys.platform == 'darwin':
                keyPressed = event.MetaDown()
            else:
                keyPressed = event.ControlDown()

            #In Mac, control+mouseLeft = mouseRight emulated
            if keyPressed:
                #Delete point
                del self.controlPoint[pointClicked]
                del self.leftTangent[pointClicked]
                del self.rightTangent[pointClicked]

                if self.selected[pointClicked]:
                    selectedPoints -= 1
                del self.selected[pointClicked]
                
                del self.visible[pointClicked]
                del self.endPoint[pointClicked]

                self.curve.Refresh()
            else:
                self.pointClicked = pointClicked
                self.leftTangentClicked = self.rightTangentClicked = -1

        elif leftTangentClicked > -1 and self.checkBoxTangents.GetValue():
            self.leftTangentClicked = leftTangentClicked
            self.pointClicked = self.rightTangentClicked = -1

        elif rightTangentClicked > -1 and self.checkBoxTangents.GetValue():
            self.rightTangentClicked = rightTangentClicked
            self.pointClicked = self.leftTangentClicked = -1
            
        elif event.ShiftDown() and len(self.controlPoint) < MAX_POINTS:
            self.controlPoint.append(position)
        
            if position.x-15 > 0:
                leftTangent = wxPoint(position.x-15, position.y)
            else:
                leftTangent = wxPoint(0, position.y)
            self.leftTangent.append(leftTangent)
        
            if position.x+15 < 255:
                rightTangent = wxPoint(position.x+15, position.y)
            else:
                rightTangent = wxPoint(255, position.y)
            self.rightTangent.append(rightTangent)
            
            self.pointClicked = pointClicked
            self.leftTangentClicked = self.rightTangentClicked = -1
        
            self.selected.append(false)
            self.visible.append(true)
            self.endPoint.append(false)

            self.curve.Refresh()
        
        event.Skip()

    def OnCurveLeftUp(self, event):
        position = event.GetPosition()
        
        curveDC = wxClientDC(self.curve)
        size = curveDC.GetSize()
        
        position = wxPoint((position.x*256) / size.x, (position.y*256) / size.y)

        if self.pointClicked > -1:
            self.controlPoint[self.pointClicked] = position
            self.curve.Refresh()

        elif self.leftTangentClicked > -1:
            self.leftTangent[self.leftTangentClicked] = position
            self.curve.Refresh()

        elif self.rightTangentClicked > -1:
            self.rightTangent[self.rightTangentClicked] = position
            self.curve.Refresh()
        
        self.pointClicked = self.leftTangentClicked = self.rightTangentClicked = -1

        event.Skip()

    def OnCurveRightDown(self, event):
        position = event.GetPosition()
        
        curveDC = wxClientDC(self.curve)
        size = curveDC.GetSize()
        
        position.x = (position.x*256) / size.x
        position.y = (position.y*256) / size.y

        pointClicked = self.getControlPoint(position, size)
        
        if pointClicked > -1 and self.checkBoxControlPoints.GetValue():
            if not self.selected[pointClicked] and self.selectedPoints == 2:
                dlg = wxMessageDialog(self, 'No more than 2 points can be selected',
                  'Selection error', wxOK | wxICON_INFORMATION)
                try:
                    dlg.ShowModal()
                finally:
                    dlg.Destroy()
            else:
                self.selected[pointClicked] = not self.selected[pointClicked]
                if self.selected[pointClicked]:
                    self.selectedPoints += 1
                else:
                    self.selectedPoints -= 1
                self.curve.Refresh()
        
        event.Skip()

    def OnCurveMotion(self, event):
        position = event.GetPosition()
        
        curveDC = wxClientDC(self.curve)
        size = curveDC.GetSize()
        
        #Calculate real position
        position = wxPoint((position.x*256) / size.x, (position.y*256) / size.y)
        
        #Crop position
        if position.x < 0:
            position.x = 0
        if position.y < 0:
            position.y = 0
        if position.x > 255:
            position.x = 255
        if position.y > 255:
            position.y = 255
        
        #Write cursor position
        self.cursorPosition.SetLabel("(%d, %d)" % (position.x, position.y,))
        
        #Motion control
        pointClicked = self.getControlPoint(position, size)
        leftTangentClicked = self.getLeftTangent(position, size)
        rightTangentClicked = self.getRightTangent(position, size)
        if (pointClicked > -1 and self.checkBoxControlPoints.GetValue()) or\
           (leftTangentClicked > -1 and self.checkBoxTangents.GetValue()) or\
           (rightTangentClicked > -1 and self.checkBoxTangents.GetValue()):
                self.curve.SetCursor(wxStockCursor(wxCURSOR_HAND))
        else:
            self.curve.SetCursor(wxNullCursor)
            
        if self.pointClicked > -1:
            if event.AltDown():
                #Move curve
                delta = position - self.controlPoint[self.pointClicked]
                
                #Find start point and end point for moving
                start = end = self.pointClicked
                while not self.endPoint[start-1] and start > 0:
                    start -= 1
                while not self.endPoint[end] and end < len(self.controlPoint)-1:
                    end += 1
                
                for i in range(start,end+1):
                    self.controlPoint[i].x += delta.x
                    self.controlPoint[i].y += delta.y
                    
                    if self.controlPoint[i].x < 0:
                        self.controlPoint[i].x = 0
                    elif self.controlPoint[i].x > 255:
                        self.controlPoint[i].x = 255
                    if self.controlPoint[i].y < 0:
                        self.controlPoint[i].y = 0
                    elif self.controlPoint[i].y > 255:
                        self.controlPoint[i].y = 255

                    self.leftTangent[i].x += delta.x
                    self.leftTangent[i].y += delta.y

                    if self.leftTangent[i].x < 0:
                        self.leftTangent[i].x = 0
                    elif self.leftTangent[i].x > 255:
                        self.leftTangent[i].x = 255
                    if self.leftTangent[i].y < 0:
                        self.leftTangent[i].y = 0
                    elif self.leftTangent[i].y > 255:
                        self.leftTangent[i].y = 255

                    self.rightTangent[i].x += delta.x
                    self.rightTangent[i].y += delta.y

                    if self.rightTangent[i].x < 0:
                        self.rightTangent[i].x = 0
                    elif self.rightTangent[i].x > 255:
                        self.rightTangent[i].x = 255
                    if self.rightTangent[i].y < 0:
                        self.rightTangent[i].y = 0
                    elif self.rightTangent[i].y > 255:
                        self.rightTangent[i].y = 255

            else:
                #Move only current control point
                self.controlPoint[self.pointClicked] = position
            self.curve.Refresh()
        
        elif self.leftTangentClicked > -1:
            self.leftTangent[self.leftTangentClicked] = position

            if sys.platform == 'darwin':
                keyPressed = event.MetaDown()
            else:
                keyPressed = event.ControlDown()

            if event.ShiftDown():
                #Horizontal Mirror
                delta = position.y - self.controlPoint[self.leftTangentClicked].y
                self.rightTangent[self.leftTangentClicked].x = \
                        self.leftTangent[self.leftTangentClicked].x
                self.rightTangent[self.leftTangentClicked].y = \
                        self.controlPoint[self.leftTangentClicked].y - delta

                if self.rightTangent[self.leftTangentClicked].y < 0:
                    self.rightTangent[self.leftTangentClicked].y = 0
                elif self.rightTangent[self.leftTangentClicked].y > 255:
                    self.rightTangent[self.leftTangentClicked].y = 255

            elif keyPressed:
                #Vertical Mirror
                delta = position.x - self.controlPoint[self.leftTangentClicked].x
                self.rightTangent[self.leftTangentClicked].x = \
                        self.controlPoint[self.leftTangentClicked].x - delta
                self.rightTangent[self.leftTangentClicked].y = \
                        self.leftTangent[self.leftTangentClicked].y

                if self.rightTangent[self.leftTangentClicked].x < 0:
                    self.rightTangent[self.leftTangentClicked].x = 0
                elif self.rightTangent[self.leftTangentClicked].x > 255:
                    self.rightTangent[self.leftTangentClicked].x = 255

            elif event.AltDown():
                #Mirror
                deltaX = position.x - self.controlPoint[self.leftTangentClicked].x
                deltaY = position.y - self.controlPoint[self.leftTangentClicked].y
                self.rightTangent[self.leftTangentClicked].x = \
                        self.controlPoint[self.leftTangentClicked].x - deltaX
                self.rightTangent[self.leftTangentClicked].y = \
                        self.controlPoint[self.leftTangentClicked].y - deltaY

                if self.rightTangent[self.leftTangentClicked].x < 0:
                    self.rightTangent[self.leftTangentClicked].x = 0
                elif self.rightTangent[self.leftTangentClicked].x > 255:
                    self.rightTangent[self.leftTangentClicked].x = 255
                if self.rightTangent[self.leftTangentClicked].y < 0:
                    self.rightTangent[self.leftTangentClicked].y = 0
                elif self.rightTangent[self.leftTangentClicked].y > 255:
                    self.rightTangent[self.leftTangentClicked].y = 255

            self.curve.Refresh()
            
        elif self.rightTangentClicked > -1:
            self.rightTangent[self.rightTangentClicked] = position

            if sys.platform == 'darwin':
                keyPressed = event.MetaDown()
            else:
                keyPressed = event.ControlDown()

            if event.ShiftDown():
                #Horizontal Mirror
                delta = position.y - self.controlPoint[self.rightTangentClicked].y
                self.leftTangent[self.rightTangentClicked].x = \
                        self.rightTangent[self.rightTangentClicked].x
                self.leftTangent[self.rightTangentClicked].y = \
                        self.controlPoint[self.rightTangentClicked].y - delta

                if self.leftTangent[self.rightTangentClicked].y < 0:
                    self.leftTangent[self.rightTangentClicked].y = 0
                elif self.leftTangent[self.rightTangentClicked].y > 255:
                    self.leftTangent[self.rightTangentClicked].y = 255

            elif keyPressed:
                #Vertical Mirror
                delta = position.x - self.controlPoint[self.rightTangentClicked].x
                self.leftTangent[self.rightTangentClicked].x = \
                        self.controlPoint[self.rightTangentClicked].x - delta
                self.leftTangent[self.rightTangentClicked].y = \
                        self.rightTangent[self.rightTangentClicked].y

                if self.leftTangent[self.rightTangentClicked].x < 0:
                    self.leftTangent[self.rightTangentClicked].x = 0
                elif self.leftTangent[self.rightTangentClicked].x > 255:
                    self.leftTangent[self.rightTangentClicked].x = 255

            elif event.AltDown():
                #Mirror
                deltaX = position.x - self.controlPoint[self.rightTangentClicked].x
                deltaY = position.y - self.controlPoint[self.rightTangentClicked].y
                self.leftTangent[self.rightTangentClicked].x = \
                        self.controlPoint[self.rightTangentClicked].x - deltaX
                self.leftTangent[self.rightTangentClicked].y = \
                        self.controlPoint[self.rightTangentClicked].y - deltaY

                if self.leftTangent[self.rightTangentClicked].x < 0:
                    self.leftTangent[self.rightTangentClicked].x = 0
                elif self.leftTangent[self.rightTangentClicked].x > 255:
                    self.leftTangent[self.rightTangentClicked].x = 255
                if self.leftTangent[self.rightTangentClicked].y < 0:
                    self.leftTangent[self.rightTangentClicked].y = 0
                elif self.leftTangent[self.rightTangentClicked].y > 255:
                    self.leftTangent[self.rightTangentClicked].y = 255

            self.curve.Refresh()
            
        event.Skip()

    def OnCurvePaint(self, event):
        curveDC = wxPaintDC(self.curve)
        size = curveDC.GetSize()
        
        curveDC.BeginDrawing()

        pen = wxPen(wxColour(0,0,0), 1, wxSOLID)
        widePen = wxPen(wxColour(0,0,0), (self.spinCtrlWidth.GetValue()*size.x)/256, wxSOLID)
        greenWidePen = wxPen(wxColour(0,255,0), (self.spinCtrlWidth.GetValue()*size.x)/256, wxSOLID)

        whiteBrush = wxBrush(wxColour(255,255,255), wxSOLID)
        blackBrush = wxBrush(wxColour(0,0,0), wxSOLID)
        redBrush = wxBrush(wxColour(255,0,0), wxSOLID)
        greenBrush = wxBrush(wxColour(0,255,0), wxSOLID)
        yellowBrush = wxBrush(wxColour(255,255,0), wxSOLID)

        numberOfPoints = len(self.controlPoint)
        currentlySelected = false
        firstPoint = 0

        controlPoints = []

        for i in range(0, numberOfPoints):
            point = self.controlPoint[i]
            controlPoint = wxPoint((point.x*size.x) / 256, (point.y*size.y) / 256)

            if self.endPoint[i]:
                if self.selected[i]:
                    currentBrush = yellowBrush
                else:
                    currentBrush = redBrush
                j = firstPoint
                firstPoint = i+1
            else:
                if self.selected[i]:
                    currentBrush = greenBrush
                else:
                    currentBrush = whiteBrush
                
                if i+1 < numberOfPoints:
                    j = i+1
                else:
                    j = firstPoint

            curveDC.SetPen(pen)
            if self.checkBoxNumbers.GetValue():
                curveDC.SetTextForeground(wxColour(64,64,255))
                (textWidth, textHeight) = curveDC.GetTextExtent(str(i))
                curveDC.DrawText(str(i),controlPoint.x-textWidth/2, controlPoint.y-6-textHeight)

            if self.checkBoxControlPoints.GetValue():
                curveDC.SetBrush(currentBrush)
                curveDC.DrawRectangle(controlPoint.x-4, controlPoint.y-4, 9, 9)
            
            if self.selected[i] and self.selectedPoints == 2:
                currentlySelected = not currentlySelected

            if self.checkBoxTangents.GetValue():
                curveDC.SetBrush(whiteBrush)

                point = self.leftTangent[i]
                leftTangent = wxPoint((point.x*size.x) / 256, (point.y*size.y) / 256)
                curveDC.DrawLine(leftTangent.x, leftTangent.y, controlPoint.x, controlPoint.y)
            
                point = self.rightTangent[i]
                rightTangent = wxPoint((point.x*size.x) / 256, (point.y*size.y) / 256)
                curveDC.DrawLine(rightTangent.x, rightTangent.y, controlPoint.x, controlPoint.y)
            
                curveDC.DrawCircle(leftTangent.x, leftTangent.y, 4)
                curveDC.DrawCircle(rightTangent.x, rightTangent.y, 4)

            a = self.controlPoint[i]
            b = self.rightTangent[i]
            c = self.leftTangent[j]
            d = self.controlPoint[j]
                
            lastPoint = wxPoint(a.x, a.y)
            lastPoint.x = int(lastPoint.x*size.x/256.0)
            lastPoint.y = int(lastPoint.y*size.y/256.0)
            
            if currentlySelected and self.selectedPoints == 2:
                curveDC.SetPen(greenWidePen)
            else:
                curveDC.SetPen(widePen)
            
            for t in range(0, self.spinCtrlSegments.GetValue()+1):
                aa = float(t)/float(self.spinCtrlSegments.GetValue())
                bb = 1.0 - aa
                    
                b2 = bb*bb
                b3 = b2*bb
                a2 = aa*aa
                a3 = a2*aa
                    
                px = a.x*b3 + 3.0*b.x*b2*aa + 3.0*c.x*bb*a2 + d.x*a3
                py = a.y*b3 + 3.0*b.y*b2*aa + 3.0*c.y*bb*a2 + d.y*a3
                
                if self.radioButtonSpline.GetValue() and self.visible[i]:
                    curveDC.DrawLine(lastPoint.x, lastPoint.y,
                        int(px*size.x/256.0), int(py*size.y/256.0))
                    
                lastPoint.x = int(px*size.x/256.0)
                lastPoint.y = int(py*size.y/256.0)
                    
                if t != self.spinCtrlSegments.GetValue():
                    controlPoints.append(wxPoint(int(px*size.x/256.0), int(py*size.y/256.0)))

        curveDC.SetLogicalFunction(wxINVERT)
        if self.radioButtonFilled.GetValue():
            curveDC.SetPen(wxTRANSPARENT_PEN)
            curveDC.SetBrush(blackBrush)

            numberOfSegments = self.spinCtrlSegments.GetValue()

            listOfPoints = []
            for i in range(0, numberOfPoints):
                listOfPoints.extend(controlPoints[i*numberOfSegments : (i+1)*numberOfSegments])
                if self.endPoint[i]:
                    curveDC.DrawPolygon(listOfPoints)
                    listOfPoints = []
            curveDC.DrawPolygon(listOfPoints)

        curveDC.EndDrawing()
        curveDC.SetPen(wxNullPen)
        
        event.Skip()

    def OnRadioButtonSplineRadiobutton(self, event):
        self.curve.Refresh()
        event.Skip()

    def OnRadioButtonFilledRadiobutton(self, event):
        self.curve.Refresh()
        event.Skip()

    def OnCheckBoxTangentsCheckbox(self, event):
        self.curve.Refresh()
        event.Skip()

    def OnCheckBoxNumbersCheckbox(self, event):
        self.curve.Refresh()
        event.Skip()

    def OnCheckBoxControlPointsCheckbox(self, event):
        self.curve.Refresh()
        event.Skip()

    def OnSpinCtrlSegmentsSpinctrl(self, event):
        self.curve.Refresh()
        event.Skip()

    def OnSpinCtrlWidthSpinctrl(self, event):
        self.curve.Refresh()
        event.Skip()

    def OnButtonDeleteButton(self, event):
        if self.selectedPoints != 2:
            dlg = wxMessageDialog(self, 'Two points must be selected to define a segment',
              'Selection error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            
        #Search beginning of selected segments
        i = 0
        while not self.selected[i]:
            i += 1
        beginning = i
        
        #Search ending of selected segments
        i += 1
        while not self.selected[i]:
            i += 1
        ending = i
        
        del self.controlPoint[beginning+1:ending]
        del self.leftTangent[beginning+1:ending]
        del self.rightTangent[beginning+1:ending]

        self.selected[beginning] = false
        self.selected[ending] = false
        del self.selected[beginning+1:ending]
        self.selectedPoints = 0
                
        del self.visible[beginning+1:ending]
        del self.endPoint[beginning+1:ending]

        self.curve.Refresh()

        event.Skip()

    def OnButtonRefineButton(self, event):
        if self.selectedPoints != 2:
            dlg = wxMessageDialog(self, 'Two points must be selected to define a segment',
              'Selection error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            
        #Search beginning of selected segments
        i = 0
        while not self.selected[i]:
            i += 1
        beginning = i
        
        #Search ending of selected segments
        i += 1
        while not self.selected[i]:
            i += 1
        ending = i
        
        i = beginning
        while i < beginning + (ending-beginning)*2:
            x = (self.controlPoint[i].x + self.controlPoint[i+1].x)/2
            y = (self.controlPoint[i].y + self.controlPoint[i+1].y)/2
            
            self.controlPoint.insert(i+1, wxPoint(x,y))
            self.leftTangent.insert(i+1, wxPoint(x-15,y))
            self.rightTangent.insert(i+1, wxPoint(x+15,y))
            
            self.selected.insert(i+1, false)
            self.visible.insert(i+1, true)
            self.endPoint.insert(i+1, false)
            
            i += 2
        
        #Clear selected points
        for i in range(0,len(self.selected)):
            self.selected[i] = False
        self.selectedPoints = 0

        self.curve.Refresh()

        event.Skip()

    def OnButtonVisibleButton(self, event):
        if self.selectedPoints != 2:
            dlg = wxMessageDialog(self, 'Two points must be selected to define a segment',
              'Selection error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            return
            
        #Search beginning of selected segments
        i = 0
        while not self.selected[i]:
            i += 1
        beginning = i
        
        #Search ending of selected segments
        i += 1
        while not self.selected[i]:
            i += 1
        ending = i
        
        for i in range(beginning, ending):
            self.visible[i] = not self.visible[i]
        
        #Clear selected points
        for i in range(0,len(self.selected)):
            self.selected[i] = False
        self.selectedPoints = 0

        self.curve.Refresh()

        event.Skip()

    def OnButtonEndpointButton(self, event):
        if self.selectedPoints != 1:
            dlg = wxMessageDialog(self, 'Only one point must be selected',
              'Selection error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            
        #Search selected point
        i = 0
        while not self.selected[i]:
            i += 1
        self.endPoint[i] = not self.endPoint[i]
        
        #Clear selected points
        for i in range(0,len(self.selected)):
            self.selected[i] = False
        self.selectedPoints = 0

        self.curve.Refresh()

        event.Skip()

    def Save(self, fileName):
        #Pickle curve
        f = open(fileName + ".crv", "wb")

        pickle.dump(self.radioButtonSpline.GetValue(), f)
        pickle.dump(self.radioButtonFilled.GetValue(), f)
        pickle.dump(self.checkBoxTangents.GetValue(), f)
        pickle.dump(self.checkBoxNumbers.GetValue(), f)
        pickle.dump(self.checkBoxControlPoints.GetValue(), f)
        
        pickle.dump(self.spinCtrlSegments.GetValue(), f)
        pickle.dump(self.spinCtrlWidth.GetValue(), f)

        pickle.dump(self.visible, f)
        pickle.dump(self.endPoint, f)
        pickle.dump(self.selected, f)
        pickle.dump(self.controlPoint, f)
        pickle.dump(self.leftTangent, f)
        pickle.dump(self.rightTangent, f)
        f.close()

    def Load(self, fileName):
        #Unpickle curve
        f = open(fileName, "rb")

        self.radioButtonSpline.SetValue(pickle.load(f))
        self.radioButtonFilled.SetValue(pickle.load(f))
        self.checkBoxTangents.SetValue(pickle.load(f))
        self.checkBoxNumbers.SetValue(pickle.load(f))
        self.checkBoxControlPoints.SetValue(pickle.load(f))

        self.spinCtrlSegments.SetValue(pickle.load(f))
        self.spinCtrlWidth.SetValue(pickle.load(f))

        self.visible = pickle.load(f)
        self.endPoint = pickle.load(f)
        self.selected = pickle.load(f)
        self.controlPoint = pickle.load(f)
        self.leftTangent = pickle.load(f)
        self.rightTangent = pickle.load(f)
        f.close()
        
        #Store number of selected points
        for i in self.selected:
            if i == TRUE:
                self.selectedPoints += 1

        self.GetData(fileName)

    def SaveH(self, f, componentName):
        numberOfPoints = len(self.controlPoint)
        
        f.write("\t\t//Curve name\n")
        f.write("\t\t")
        for i in componentName:
            f.write("'%c'," % (i,))
        f.write("0,\n\n")
        
        f.write("\t\t//Mode (1 bit) + Number of points (7 bits)\n")
        if self.radioButtonFilled.GetValue():
            f.write("\t\t%d,\n\n" % (128 + numberOfPoints,))
        else:
            f.write("\t\t%d,\n\n" % (numberOfPoints,))

        f.write("\t\t//Segments per curve\n")
        f.write("\t\t%d,\n\n" % (self.spinCtrlSegments.GetValue(),))

        f.write("\t\t//Line width\n")
        f.write("\t\t%d,\n\n" % (self.spinCtrlWidth.GetValue(),))

        #Write visible and endpoint bits
        f.write("\t\t//Visible and endpoint bits (1 point per bit)\n")
        
        #Add trailing values, to avoid out of range error
        self.visible.extend([false, false, false, false, false, false, false, false])
        self.endPoint.extend([false, false, false, false, false, false, false, false])
        
        for i in range(0, 1 + (numberOfPoints-1)/8):
            val = self.visible[8*i] +\
                (self.visible[8*i+1]<<1) +\
                (self.visible[8*i+2]<<2) +\
                (self.visible[8*i+3]<<3) +\
                (self.visible[8*i+4]<<4) +\
                (self.visible[8*i+5]<<5) +\
                (self.visible[8*i+6]<<6) +\
                (self.visible[8*i+7]<<7)
            f.write("\t\t%d,\n" % (val,))

            val = self.endPoint[8*i] +\
                (self.endPoint[8*i+1]<<1) +\
                (self.endPoint[8*i+2]<<2) +\
                (self.endPoint[8*i+3]<<3) +\
                (self.endPoint[8*i+4]<<4) +\
                (self.endPoint[8*i+5]<<5) +\
                (self.endPoint[8*i+6]<<6) +\
                (self.endPoint[8*i+7]<<7)
            f.write("\t\t%d,\n\n" % (val,))
        
        #Remove trailing values
        self.visible = self.visible[0:numberOfPoints]
        self.endPoint = self.endPoint[0:numberOfPoints]

        #Write control points, left tangents and right tangents
        f.write("\t\t//Control points, left tangents and right tangents\n")
        for i in range(0, numberOfPoints):
            f.write("\t\t%d, %d,\n" % (self.controlPoint[i].x, self.controlPoint[i].y))
            f.write("\t\t%d, %d,\n" % (self.leftTangent[i].x, self.leftTangent[i].y))
            f.write("\t\t%d, %d,\n" % (self.rightTangent[i].x, self.rightTangent[i].y))

        f.write("\n")

    def GetData(self, componentName):
        numberOfPoints = len(self.controlPoint)

        # Store curve name
        output = componentName
        output += pack('B', 0)
        
        # Store number of points
        if self.radioButtonFilled.GetValue():
            output += pack('B', 128 + numberOfPoints)
        else:
            output += pack('B', numberOfPoints)

        # Store segments per curve
        output += pack('B', self.spinCtrlSegments.GetValue())

        # Store line width
        output += pack('B', self.spinCtrlWidth.GetValue())

        # Add trailing values, to avoid out of range error
        self.visible.extend([false, false, false, false, false, false, false, false])
        self.endPoint.extend([false, false, false, false, false, false, false, false])
        
        # Write visible and endpoint bits
        for i in range(0, 1 + (numberOfPoints-1)/8):
            val = self.visible[8*i] +\
                (self.visible[8*i+1]<<1) +\
                (self.visible[8*i+2]<<2) +\
                (self.visible[8*i+3]<<3) +\
                (self.visible[8*i+4]<<4) +\
                (self.visible[8*i+5]<<5) +\
                (self.visible[8*i+6]<<6) +\
                (self.visible[8*i+7]<<7)
            output += pack('B', val)

            val = self.endPoint[8*i] +\
                (self.endPoint[8*i+1]<<1) +\
                (self.endPoint[8*i+2]<<2) +\
                (self.endPoint[8*i+3]<<3) +\
                (self.endPoint[8*i+4]<<4) +\
                (self.endPoint[8*i+5]<<5) +\
                (self.endPoint[8*i+6]<<6) +\
                (self.endPoint[8*i+7]<<7)
            output += pack('B', val)
        
        # Remove trailing values
        self.visible = self.visible[0:numberOfPoints]
        self.endPoint = self.endPoint[0:numberOfPoints]

        # Write control points, left tangents and right tangents
        for i in range(0, numberOfPoints):
            output += pack('BB', self.controlPoint[i].x, self.controlPoint[i].y)
            output += pack('BB', self.leftTangent[i].x, self.leftTangent[i].y)
            output += pack('BB', self.rightTangent[i].x, self.rightTangent[i].y)

        return output
