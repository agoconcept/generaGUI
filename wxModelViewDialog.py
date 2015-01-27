#Boa:Dialog:wxModelViewDialog

from wxPython.wx import *

def create(parent):
    return wxModelViewDialog(parent)

[wxID_WXMODELVIEWDIALOG, wxID_WXMODELVIEWDIALOGBUTTONSAVEJPG, 
 wxID_WXMODELVIEWDIALOGBUTTONSAVEPNG, wxID_WXMODELVIEWDIALOGSTATICBITMAPTILEDLAYER, 
] = map(lambda _init_ctrls: wxNewId(), range(4))

class wxModelViewDialog(wxDialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxDialog.__init__(self, id=wxID_WXMODELVIEWDIALOG, name='wxModelViewDialog',
              parent=prnt, pos=wxPoint(208, 128), size=wxSize(800, 600),
              style=wxDEFAULT_DIALOG_STYLE, title='Tiled layer')
        self.SetClientSize(wxSize(800, 600))
        self.SetToolTipString('Tiled layer')

        self.buttonSavePNG = wxButton(id=wxID_WXMODELVIEWDIALOGBUTTONSAVEPNG,
              label='Save as PNG', name='buttonSavePNG', parent=self,
              pos=wxPoint(8, 8), size=wxSize(128, 32), style=0)
        self.buttonSavePNG.SetToolTipString('Save as PNG')
        EVT_BUTTON(self.buttonSavePNG, wxID_WXMODELVIEWDIALOGBUTTONSAVEPNG,
              self.OnButtonSavePNGButton)

        self.buttonSaveJPG = wxButton(id=wxID_WXMODELVIEWDIALOGBUTTONSAVEJPG,
              label='Save as JPG', name='buttonSaveJPG', parent=self,
              pos=wxPoint(144, 8), size=wxSize(128, 32), style=0)
        self.buttonSaveJPG.SetToolTipString('Save as JPG')
        EVT_BUTTON(self.buttonSaveJPG, wxID_WXMODELVIEWDIALOGBUTTONSAVEJPG,
              self.OnButtonSaveJPGButton)

        self.staticBitmapTiledLayer = wxStaticBitmap(bitmap=wxNullBitmap,
              id=wxID_WXMODELVIEWDIALOGSTATICBITMAPTILEDLAYER,
              name='staticBitmapTiledLayer', parent=self, pos=wxPoint(224, 264),
              size=wxSize(784, 544), style=0)
        self.staticBitmapTiledLayer.SetToolTipString('Tiled layer')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def SetBitmap(self, bitmap):
        self.bitmap = bitmap
        bitmapWidth = bitmap.GetWidth()
        bitmapHeight = bitmap.GetHeight()
        size = self.GetSize()

        for i in range(0, 1+size.GetWidth()/bitmapWidth):
            for j in range(0, 1+size.GetHeight()/bitmapHeight):
                wxStaticBitmap(bitmap=bitmap, id=-1,
                    name='staticBitmapTiledLayer', parent=self,
                    pos=wxPoint(i*bitmapWidth, 48+j*bitmapHeight),
                    size=wxSize(bitmapWidth, bitmapHeight), style=0)
    
    def OnButtonSavePNGButton(self, event):
        dlg = wxFileDialog(self, "Choose a file", ".", "", "*.PNG",
            wxSAVE | wxOVERWRITE_PROMPT | wxCHANGE_DIR)
        try:
            if dlg.ShowModal() == wxID_OK:
                filename = dlg.GetPath()
                # Your code
                self.bitmap.SaveFile(filename, wxBITMAP_TYPE_PNG)
        finally:
            dlg.Destroy()

        event.Skip()

    def OnButtonSaveJPGButton(self, event):
        dlg = wxFileDialog(self, "Choose a file", ".", "", "*.JPG",
            wxSAVE | wxOVERWRITE_PROMPT | wxCHANGE_DIR)
        try:
            if dlg.ShowModal() == wxID_OK:
                filename = dlg.GetPath()
                # Your code
                self.bitmap.SaveFile(filename, wxBITMAP_TYPE_JPEG)
        finally:
            dlg.Destroy()

        event.Skip()
