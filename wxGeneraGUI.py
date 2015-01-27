#!/usr/bin/env python
#Boa:App:BoaApp

from wxPython.wx import *

import wxMainFrame

modules ={'wxCurvePanel': [0, 'Curve panel', 'wxCurvePanel.py'],
 'wxGradientPanel': [0, 'Gradient panel', 'wxGradientPanel.py'],
 'wxMainFrame': [1, 'Main frame of Application', 'wxMainFrame.py'],
 'wxModelPanel': [0, 'Model panel', 'wxModelPanel.py'],
 'wxParameterPanel': [0, 'Parameter panel', 'wxParameterPanel.py'],
 'wxScenePanel': [0, 'Scene panel', 'wxScenePanel.py'],
 'wxTexturePanel': [0, 'Texture panel', 'wxTexturePanel.py'],
 'wxTiledDialog': [0, 'Tiled dialog', 'wxTiledDialog.py']}

class BoaApp(wxApp):
    def OnInit(self):
        wxInitAllImageHandlers()
        self.main = wxMainFrame.create(None)
        # needed when running from Boa under Windows 9X
        #self.SetTopWindow(self.main)
        #self.main.Show();self.main.Hide();self.main.Show()
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
