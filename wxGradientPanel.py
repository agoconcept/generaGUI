#Boa:FramePanel:wxGradientPanel

from wxPython.wx import *
from struct import *
import pickle
import GradientPy

MAX_COLORS = 128

[wxID_WXGRADIENTPANEL, wxID_WXGRADIENTPANELBUTTONADDCOLOR, 
 wxID_WXGRADIENTPANELBUTTONDELETECOLOR, wxID_WXGRADIENTPANELBUTTONPICKCOLOR, 
 wxID_WXGRADIENTPANELGRADIENT, wxID_WXGRADIENTPANELINTERPOLATIONBOX, 
 wxID_WXGRADIENTPANELLINEARRADIOBUTTON, wxID_WXGRADIENTPANELSLIDERCOLORNUMBER, 
 wxID_WXGRADIENTPANELSLIDERCOLORPOSITION, 
 wxID_WXGRADIENTPANELSPLINERADIOBUTTON, 
] = map(lambda _init_ctrls: wxNewId(), range(10))

class wxGradientPanel(wxPanel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxPanel.__init__(self, id=wxID_WXGRADIENTPANEL, name='wxGradientPanel',
              parent=prnt, pos=wxPoint(309, 361), size=wxSize(490, 320),
              style=wxDOUBLE_BORDER)
        self.SetClientSize(wxSize(490, 320))
        self.SetToolTipString('Gradient panel')
        EVT_SIZE(self, self.OnWxgradientpanelSize)

        #Platform dependent style
        if sys.platform.startswith('win'):
            barStyle = wxSL_HORIZONTAL | wxSL_AUTOTICKS
            topBarStyle = wxSL_TOP | wxSL_HORIZONTAL | wxSL_AUTOTICKS
        else:
            barStyle = wxSL_HORIZONTAL | wxSL_LABELS
            topBarStyle = wxSL_TOP | wxSL_HORIZONTAL | wxSL_LABELS

        self.sliderColorPosition = wxSlider(id=wxID_WXGRADIENTPANELSLIDERCOLORPOSITION,
              maxValue=255, minValue=0, name='sliderColorPosition', parent=self,
              point=wxPoint(0, 8), size=wxSize(488, 35),
              style=barStyle, validator=wxDefaultValidator, value=0)
        self.sliderColorPosition.SetToolTipString('Color position slider')
        self.sliderColorPosition.SetPageSize(16)
        EVT_SCROLL(self.sliderColorPosition, self.OnSlidercolorpositionScroll)

        self.sliderColorNumber = wxSlider(id=wxID_WXGRADIENTPANELSLIDERCOLORNUMBER,
              maxValue=1, minValue=0, name='sliderColorNumber', parent=self,
              point=wxPoint(0, 112), size=wxSize(488, 35),
              style=topBarStyle, validator=wxDefaultValidator, value=0)
        self.sliderColorNumber.SetToolTipString('Color number slider')
        EVT_SCROLL(self.sliderColorNumber, self.OnSlidercolornumberScroll)

        self.gradient = wxWindow(id=wxID_WXGRADIENTPANELGRADIENT,
              name='gradient', parent=self, pos=wxPoint(16, 64),
              size=wxSize(456, 40), style=wxSIMPLE_BORDER)
        self.gradient.SetToolTipString('Gradient')
        EVT_PAINT(self.gradient, self.OnGradientPaint)

        self.buttonAddColor = wxButton(id=wxID_WXGRADIENTPANELBUTTONADDCOLOR,
              label='&Add color', name='buttonAddColor', parent=self,
              pos=wxPoint(40, 160), size=wxSize(80, 32), style=0)
        self.buttonAddColor.SetToolTipString('Add a new color to the gradient')
        EVT_BUTTON(self.buttonAddColor, wxID_WXGRADIENTPANELBUTTONADDCOLOR,
              self.OnButtonaddcolorButton)

        self.buttonDeleteColor = wxButton(id=wxID_WXGRADIENTPANELBUTTONDELETECOLOR,
              label='&Delete color', name='buttonDeleteColor', parent=self,
              pos=wxPoint(200, 160), size=wxSize(80, 32), style=0)
        self.buttonDeleteColor.SetToolTipString('Delete current color from the gradient')
        EVT_BUTTON(self.buttonDeleteColor,
              wxID_WXGRADIENTPANELBUTTONDELETECOLOR,
              self.OnButtondeletecolorButton)

        self.buttonPickColor = wxButton(id=wxID_WXGRADIENTPANELBUTTONPICKCOLOR,
              label='&Pick color', name='buttonPickColor', parent=self,
              pos=wxPoint(360, 168), size=wxSize(80, 32), style=0)
        self.buttonPickColor.SetToolTipString('Pick a color for the current position')
        EVT_BUTTON(self.buttonPickColor, wxID_WXGRADIENTPANELBUTTONPICKCOLOR,
              self.OnButtonpickcolorButton)

        self.interpolationBox = wxStaticBox(id=wxID_WXGRADIENTPANELINTERPOLATIONBOX,
              label='Interpolation', name='interpolationBox', parent=self,
              pos=wxPoint(8, 208), size=wxSize(472, 60), style=0)

        self.linearRadioButton = wxRadioButton(id=wxID_WXGRADIENTPANELLINEARRADIOBUTTON,
              label='Linear', name='linearRadioButton', parent=self,
              pos=wxPoint(96, 232), size=wxSize(94, 24), style=0)
        self.linearRadioButton.SetValue(True)
        self.linearRadioButton.SetToolTipString('Linear interpolation')
        EVT_RADIOBUTTON(self.linearRadioButton,
              wxID_WXGRADIENTPANELLINEARRADIOBUTTON,
              self.OnLinearRadioButtonRadiobutton)

        self.splineRadioButton = wxRadioButton(id=wxID_WXGRADIENTPANELSPLINERADIOBUTTON,
              label='Spline', name='splineRadioButton', parent=self,
              pos=wxPoint(288, 232), size=wxSize(94, 24), style=0)
        self.splineRadioButton.SetValue(False)
        self.splineRadioButton.SetToolTipString('Splineinterpolation')
        EVT_RADIOBUTTON(self.splineRadioButton,
              wxID_WXGRADIENTPANELSPLINERADIOBUTTON,
              self.OnSplineRadioButtonRadiobutton)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)

        #Init variables
        self.numberOfColors = 2
        self.color = [wxColour(), wxColour()]
        self.colorPosition = [0, 255]

        self.colorGradient = GradientPy.Gradient()
        
    def OnWxgradientpanelSize(self, event):
        size = wxSize(self.GetClientSize().GetWidth(), self.GetClientSize().GetHeight())
        yMiddle = size.GetHeight() / 2

        colorPositionPosition = wxPoint(0, yMiddle - 104)
        colorPositionSize = wxSize(size.GetWidth(), 35)
        self.sliderColorPosition.SetPosition(colorPositionPosition)
        self.sliderColorPosition.SetSize(colorPositionSize)

        gradientPosition = wxPoint(16, yMiddle - 64)
        gradientSize = wxSize(size.GetWidth()-32, 40)
        self.gradient.SetPosition(gradientPosition)
        self.gradient.SetSize(gradientSize)
        
        colorNumberPosition = wxPoint(0, yMiddle - 16)
        colorNumberSize = wxSize(size.GetWidth(), 35)
        self.sliderColorNumber.SetPosition(colorNumberPosition)
        self.sliderColorNumber.SetSize(colorNumberSize)

        buttonSize = self.buttonAddColor.GetSize()
        buttonPosition = self.buttonAddColor.GetPosition()
        buttonPosition.x = size.GetWidth()/4 - buttonSize.GetWidth()/2
        buttonPosition.y = yMiddle + 32
        self.buttonAddColor.SetPosition(buttonPosition)

        buttonSize = self.buttonDeleteColor.GetSize()
        buttonPosition = self.buttonDeleteColor.GetPosition()
        buttonPosition.x = size.GetWidth()/2 - buttonSize.GetWidth()/2
        buttonPosition.y = yMiddle + 32
        self.buttonDeleteColor.SetPosition(buttonPosition)

        buttonSize = self.buttonPickColor.GetSize()
        buttonPosition = self.buttonPickColor.GetPosition()
        buttonPosition.x = 3*size.GetWidth()/4 - buttonSize.GetWidth()/2
        buttonPosition.y = yMiddle + 32
        self.buttonPickColor.SetPosition(buttonPosition)
        
        buttonSize = self.interpolationBox.GetSize()
        buttonSize.x = size.GetWidth()-16
        self.interpolationBox.SetSize(buttonSize)
        buttonPosition = self.interpolationBox.GetPosition()
        buttonPosition.x = 8
        buttonPosition.y = yMiddle + 80
        self.interpolationBox.SetPosition(buttonPosition)

        buttonSize = self.linearRadioButton.GetSize()
        buttonPosition = self.linearRadioButton.GetPosition()
        buttonPosition.x = size.GetWidth()/3 - buttonSize.GetWidth()/2
        buttonPosition.y = yMiddle + 104
        self.linearRadioButton.SetPosition(buttonPosition)

        buttonSize = self.splineRadioButton.GetSize()
        buttonPosition = self.splineRadioButton.GetPosition()
        buttonPosition.x = 2*size.GetWidth()/3 - buttonSize.GetWidth()/2
        buttonPosition.y = yMiddle + 104
        self.splineRadioButton.SetPosition(buttonPosition)
        
        #Precalculate lines to draw the gradient
        size = self.gradient.GetClientSize()
        self.lines = []
        self.pens = []
        for i in range(0, size.GetWidth()):
            self.lines.append( (i,0,i,size.GetHeight(),) )
            self.pens.append(wxPen(wxColour(0,0,0), 1, wxSOLID))

        event.Skip()

    def Redraw(self):
        None
        
    def OnButtonaddcolorButton(self, event):
        if self.numberOfColors >= MAX_COLORS:
            return

        currentColor = self.sliderColorNumber.GetValue()

        if currentColor == 0:
            if self.colorPosition[1] > self.colorPosition[0]+1:
                self.numberOfColors += 1
                self.color.insert(1, wxColour())
                newPosition = (self.colorPosition[0] + self.colorPosition[1])/2
                self.colorPosition.insert(1, newPosition)
                currentColor += 1
        else:
            if self.colorPosition[currentColor] > self.colorPosition[currentColor-1]+1:
                self.numberOfColors += 1
                self.color.insert(currentColor, wxColour())
                newPosition = (self.colorPosition[currentColor-1] +\
                               self.colorPosition[currentColor])/2
                self.colorPosition.insert(currentColor, newPosition)
            
        self.sliderColorNumber.SetRange(0, self.numberOfColors-1)
        self.sliderColorNumber.SetValue(currentColor)
        self.sliderColorPosition.SetValue(self.colorPosition[currentColor])

        self.gradient.Refresh()

        event.Skip()        

    def OnButtondeletecolorButton(self, event):
        if self.numberOfColors > 2:
            self.numberOfColors -= 1
            currentColor = self.sliderColorNumber.GetValue()
            del self.color[currentColor]
            del self.colorPosition[currentColor]
            self.sliderColorNumber.SetRange(0, self.numberOfColors-1)
            self.colorPosition[0] = 0
            self.colorPosition[self.numberOfColors-1] = 255
            currentColor = self.sliderColorNumber.GetValue()
            self.sliderColorPosition.SetValue(self.colorPosition[currentColor])
            
            self.gradient.Refresh()

        event.Skip()        

    def OnButtonpickcolorButton(self, event):
        colorNumber = self.sliderColorNumber.GetValue()
        data = wxColourData()
        data.SetChooseFull(true)
        data.SetColour(self.color[colorNumber])
        dlg = wxColourDialog(self, data)
        try:
            if dlg.ShowModal() == wxID_OK:
                data = dlg.GetColourData()
                
                #Update color
                color = data.GetColour()
                self.color[colorNumber] = wxColour(color.Red(),color.Green(),color.Blue())
        finally:
            dlg.Destroy()

        self.gradient.Refresh()

        event.Skip()        

    def OnSlidercolorpositionScroll(self, event):
        colorNumber = self.sliderColorNumber.GetValue()
        if colorNumber == 0:
            self.sliderColorPosition.SetValue(0)
        elif colorNumber == self.sliderColorNumber.GetMax():
            self.sliderColorPosition.SetValue(255)
        else:
            #Check that color position is between right values
            if self.sliderColorPosition.GetValue() <= self.colorPosition[colorNumber-1]:
                self.sliderColorPosition.SetValue(self.colorPosition[colorNumber-1]+1)
            elif self.sliderColorPosition.GetValue() >= self.colorPosition[colorNumber+1]:
                self.sliderColorPosition.SetValue(self.colorPosition[colorNumber+1]-1)
            self.colorPosition[colorNumber] = self.sliderColorPosition.GetValue()
            
            self.gradient.Refresh()

        event.Skip()        

    def OnSlidercolornumberScroll(self, event):
        colorNumber = self.sliderColorNumber.GetValue()
        if colorNumber == 0:
            self.sliderColorPosition.SetValue(0)
        elif colorNumber == self.sliderColorNumber.GetMax():
            self.sliderColorPosition.SetValue(255)
        else:
            self.sliderColorPosition.SetValue(self.colorPosition[colorNumber])

        event.Skip()        

    def OnLinearRadioButtonRadiobutton(self, event):
        self.gradient.Refresh()
        event.Skip()

    def OnSplineRadioButtonRadiobutton(self, event):
        self.gradient.Refresh()
        event.Skip()

    def OnGradientPaint(self, event):
        gradientDC = wxPaintDC(self.gradient)
        size = gradientDC.GetSize()

        self.colorGradient.loadGradient(self.splineRadioButton.GetValue(), 
            self.numberOfColors, self.color, self.colorPosition)

        precalc = 255.0/size.GetWidth()
        
        # Store list of pens
        for i in range(0, size.GetWidth()):
            color = self.colorGradient.getColorAt(i*precalc)
            self.pens[i].SetColour(color)

        gradientDC.BeginDrawing()
        gradientDC.DrawLineList(self.lines, self.pens)
        gradientDC.EndDrawing()

        event.Skip()

    def Save(self, fileName):
        #Pickle gradient
        f = open(fileName + ".grd", "wb")
        pickle.dump(self.splineRadioButton.GetValue(), f)
        pickle.dump(self.numberOfColors, f)
        pickle.dump(self.color, f)
        pickle.dump(self.colorPosition, f)
        f.close()

    def Load(self, fileName):
        #Unpickle gradient
        f = open(fileName, "rb")

        splineSelected = pickle.load(f)
        if splineSelected:
            self.splineRadioButton.SetValue(True)
        else:
            self.linearRadioButton.SetValue(True)

        self.numberOfColors = pickle.load(f)
        self.color = pickle.load(f)
        self.colorPosition = pickle.load(f)
        f.close()

        #Update related controls
        self.sliderColorNumber.SetRange(0, self.numberOfColors-1)
        
    def SaveH(self, f, componentName):
        f.write("\t\t//Gradient name\n")
        f.write("\t\t")
        for i in componentName:
            f.write("'%c'," % (i,))
        f.write("0,\n\n")

        f.write("\t\t//Interpolation and number of colors\n")
        splineSelected = self.splineRadioButton.GetValue()
        f.write("\t\t%d,\n\n" % (splineSelected*128 + self.numberOfColors,))

        for i in range(0, self.numberOfColors):
            f.write("\t\t//Color %d: RGB + Position\n" % (i,))
            f.write("\t\t%d, %d, %d,\n" % (self.color[i].Red(),self.color[i].Green(),self.color[i].Blue(),))
            f.write("\t\t%d,\n\n" % (self.colorPosition[i],))
        
        f.write("\n")

    def GetData(self, componentName):
        # Store gradient name
        output = componentName
        output += pack('B', 0)
        
        # Store interpolation and number of colors
        splineSelected = self.splineRadioButton.GetValue()
        output += pack('B', splineSelected*128 + self.numberOfColors)

        # Store colors and positions
        for i in range(0, self.numberOfColors):
            output += pack('B', self.color[i].Red())
            output += pack('B', self.color[i].Green())
            output += pack('B', self.color[i].Blue())
            output += pack('B', self.colorPosition[i])

        return output
