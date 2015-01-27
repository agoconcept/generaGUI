#Boa:Frame:MainFrame

from wxPython.wx import *
from struct import *
import pickle
import genera

import wxDemoPanel
import wxGradientPanel
import wxCurvePanel
import wxTexturePanel
import wxModelPanel
import wxParameterPanel
import wxScenePanel

#----------------------------------------------------------------------

fileTypesOpen = "Project files (*.cpt)|*.cpt|"\
                "Gradient files (*.grd)|*.grd|"\
                "Curve files (*.crv)|*.crv|"\
                "Texture files (*.txr)|*.txr|"\
                "Model files (*.mdl)|*.mdl|"\
                "Parameter files (*.prm)|*.prm|"\
                "Scene files (*.scn)|*.scn|"\
                "All files (*.*)|*.*"
fileTypesSave = "Project files (*.cpt)|*.cpt|"\
                "All files (*.*)|*.*"

def create(parent):
    return MainFrame(parent)

[wxID_MAINFRAME, wxID_MAINFRAMECOMPONENTSNOTEBOOK, 
 wxID_MAINFRAMECOMPONENTSTREE, wxID_MAINFRAMEGENERATOOLBAR, 
 wxID_MAINFRAMESPLITTER, wxID_MAINFRAMESTATUSBAR1, 
] = map(lambda _init_ctrls: wxNewId(), range(6))

[wxID_MAINFRAMEMENU1ITEMSEXIT, wxID_MAINFRAMEMENU1ITEMSNEW, 
 wxID_MAINFRAMEMENU1ITEMSOPEN, wxID_MAINFRAMEMENU1ITEMSSAVEAS, 
] = map(lambda _init_coll_menuFile_Items: wxNewId(), range(4))

[wxID_MAINFRAMEMENUCOMPONENTSITEMSADDCURVE, 
 wxID_MAINFRAMEMENUCOMPONENTSITEMSADDGRADIENT, 
 wxID_MAINFRAMEMENUCOMPONENTSITEMSADDMODEL, 
 wxID_MAINFRAMEMENUCOMPONENTSITEMSADDPARAMETER, 
 wxID_MAINFRAMEMENUCOMPONENTSITEMSADDSCENE, 
 wxID_MAINFRAMEMENUCOMPONENTSITEMSADDTEXTURE, 
 wxID_MAINFRAMEMENUCOMPONENTSITEMS_DELETE, 
 wxID_MAINFRAMEMENUCOMPONENTSITEMS_RENAME, 
] = map(lambda _init_coll_menuComponents_Items: wxNewId(), range(8))

[wxID_MAINFRAMEGENERATOOLBARTOOLS_CURVE, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_DELETECOMPONENT, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_GENERATEALL, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_GENERATECOMPONENT, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_GRADIENT, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_MODELS, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_NEW, wxID_MAINFRAMEGENERATOOLBARTOOLS_OPEN, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_PARAMETER, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_RENAME_COMPONENT, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_SAVEAS, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_SCENE, 
 wxID_MAINFRAMEGENERATOOLBARTOOLS_TEXTURE, 
] = map(lambda _init_coll_generaToolBar_Tools: wxNewId(), range(13))

[wxID_MAINFRAMEMENUHELPITEMSABOUT] = map(lambda _init_coll_menuHelp_Items: wxNewId(), range(1))

class MainFrame(wxFrame):
    def _init_coll_menuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='About this tool',
              id=wxID_MAINFRAMEMENUHELPITEMSABOUT, item='About',
              kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_MAINFRAMEMENUHELPITEMSABOUT,
              self.OnMenuhelpitems0Menu)

    def _init_coll_menuComponents_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='Add a new gradient to the project',
              id=wxID_MAINFRAMEMENUCOMPONENTSITEMSADDGRADIENT,
              item='Add &gradient', kind=wxITEM_NORMAL)
        parent.Append(helpString='Add a new curve to the project',
              id=wxID_MAINFRAMEMENUCOMPONENTSITEMSADDCURVE, item='Add &curve',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='Add a new texture to the project',
              id=wxID_MAINFRAMEMENUCOMPONENTSITEMSADDTEXTURE,
              item='Add &texture', kind=wxITEM_NORMAL)
        parent.Append(helpString='Add a new model to the project',
              id=wxID_MAINFRAMEMENUCOMPONENTSITEMSADDMODEL, item='Add &model',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='Add a new parameter to the project',
              id=wxID_MAINFRAMEMENUCOMPONENTSITEMSADDPARAMETER,
              item='Add &parameter', kind=wxITEM_NORMAL)
        parent.Append(helpString='Add a new scene to the project',
              id=wxID_MAINFRAMEMENUCOMPONENTSITEMSADDSCENE, item='Add &scene',
              kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='Rename component name',
              id=wxID_MAINFRAMEMENUCOMPONENTSITEMS_RENAME, item='&Rename',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='Delete current component',
              id=wxID_MAINFRAMEMENUCOMPONENTSITEMS_DELETE, item='&Delete',
              kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_MAINFRAMEMENUCOMPONENTSITEMSADDSCENE,
              self.OnMenucomponentsitems0Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENUCOMPONENTSITEMSADDPARAMETER,
              self.OnMenucomponentsitems1Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENUCOMPONENTSITEMSADDMODEL,
              self.OnMenucomponentsitems2Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENUCOMPONENTSITEMSADDTEXTURE,
              self.OnMenucomponentsitems3Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENUCOMPONENTSITEMSADDCURVE,
              self.OnMenucomponentsitems4Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENUCOMPONENTSITEMSADDGRADIENT,
              self.OnMenucomponentsitems5Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENUCOMPONENTSITEMS_RENAME,
              self.OnMenuComponentsItems_renameMenu)
        EVT_MENU(self, wxID_MAINFRAMEMENUCOMPONENTSITEMS_DELETE,
              self.OnMenuComponentsItems_deleteMenu)

    def _init_coll_menuBar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title='&File')
        parent.Append(menu=self.menuComponents, title='&Components')
        parent.Append(menu=self.menuHelp, title='&Help')

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='Create a new project',
              id=wxID_MAINFRAMEMENU1ITEMSNEW, item='&New project',
              kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='Open an existing project',
              id=wxID_MAINFRAMEMENU1ITEMSOPEN, item='&Open',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='Save current project ',
              id=wxID_MAINFRAMEMENU1ITEMSSAVEAS, item='S&ave as...',
              kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString="I'm too lame to use this great tool",
              id=wxID_MAINFRAMEMENU1ITEMSEXIT, item='&Exit',
              kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_MAINFRAMEMENU1ITEMSNEW, self.OnMenufileitems0Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENU1ITEMSOPEN, self.OnMenufileitems1Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENU1ITEMSSAVEAS,
              self.OnMenufileitems3Menu)
        EVT_MENU(self, wxID_MAINFRAMEMENU1ITEMSEXIT, self.OnMenufileitems5Menu)

    def _init_coll_generaToolBar_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_NEW, kind=wxITEM_NORMAL,
              label='New', longHelp='Create a new project',
              shortHelp='New project')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_OPEN, kind=wxITEM_NORMAL,
              label='Open', longHelp='Open a project from disk',
              shortHelp='Open a project')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_SAVEAS, kind=wxITEM_NORMAL,
              label='Save', longHelp='Save current project',
              shortHelp='Save current project')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_GRADIENT, kind=wxITEM_NORMAL,
              label='Gradient', longHelp='Create a new gradient component',
              shortHelp='New gradient')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_CURVE, kind=wxITEM_NORMAL,
              label='Curve', longHelp='Create a new curve component',
              shortHelp='New curve')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_TEXTURE, kind=wxITEM_NORMAL,
              label='Texture', longHelp='Create a new texture component',
              shortHelp='New texture')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_MODELS, kind=wxITEM_NORMAL,
              label='Model', longHelp='Create a new model component',
              shortHelp='New model')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_PARAMETER, kind=wxITEM_NORMAL,
              label='Parameter', longHelp='Create a new parameter component',
              shortHelp='New parameter')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_SCENE, kind=wxITEM_NORMAL,
              label='Scene', longHelp='Create a new scene component',
              shortHelp='New scene')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_RENAME_COMPONENT,
              kind=wxITEM_NORMAL, label='Rename',
              longHelp='Rename currently selected component',
              shortHelp='Rename current component')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_DELETECOMPONENT,
              kind=wxITEM_NORMAL, label='Delete',
              longHelp='Delete currently selected component',
              shortHelp='Delete current component')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_GENERATECOMPONENT,
              kind=wxITEM_NORMAL, label='Generate',
              longHelp='Generate current component',
              shortHelp='Generate current component')
        parent.DoAddTool(bitmap=wxNullBitmap, bmpDisabled=wxNullBitmap,
              id=wxID_MAINFRAMEGENERATOOLBARTOOLS_GENERATEALL,
              kind=wxITEM_NORMAL, label='Generate all',
              longHelp='Generate every component in the project',
              shortHelp='Generate all components')
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_NEW,
              self.OnGeneraToolBarTools_newTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_OPEN,
              self.OnGeneraToolBarTools_openTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_SAVEAS,
              self.OnGeneraToolBarTools_saveasTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_GRADIENT,
              self.OnGeneraToolBarTools_gradientTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_CURVE,
              self.OnGeneraToolBarTools_curveTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_TEXTURE,
              self.OnGeneraToolBarTools_textureTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_MODELS,
              self.OnGeneraToolBarTools_modelsTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_PARAMETER,
              self.OnGeneraToolBarTools_parameterTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_SCENE,
              self.OnGeneraToolBarTools_sceneTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_DELETECOMPONENT,
              self.OnGeneraToolBarTools_deletecomponentTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_RENAME_COMPONENT,
              self.OnGeneraToolBarTools_rename_componentTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_GENERATECOMPONENT,
              self.OnGeneraToolBarTools_generatecomponentTool)
        EVT_TOOL(self, wxID_MAINFRAMEGENERATOOLBARTOOLS_GENERATEALL,
              self.OnGeneraToolBarTools_generateallTool)

        parent.Realize()

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(i=0, text='Genera by ago / Concept')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.menuFile = wxMenu(title='')

        self.menuBar = wxMenuBar()

        self.menuHelp = wxMenu(title='')

        self.menuComponents = wxMenu(title='')

        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuBar_Menus(self.menuBar)
        self._init_coll_menuHelp_Items(self.menuHelp)
        self._init_coll_menuComponents_Items(self.menuComponents)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxFrame.__init__(self, id=wxID_MAINFRAME, name='MainFrame', parent=prnt,
              pos=wxPoint(0, 0), size=wxSize(1144, 790),
              style=wxDEFAULT_FRAME_STYLE,
              title="Concept's Genera. We Are Vastly Superior")
        self._init_utils()
        self.SetClientSize(wxSize(1144, 790))
        self.SetMenuBar(self.menuBar)
        self.SetSizeHints(640, 480, -1, -1)
        self.Show(True)
        EVT_CLOSE(self, self.OnMainFrameClose)

        self.statusBar1 = wxStatusBar(id=wxID_MAINFRAMESTATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetSize(wxSize(640, 25))
        self.statusBar1.SetPosition(wxPoint(0, 429))
        self.statusBar1.SetToolTipString('Status Bar')
        self.statusBar1.SetStatusText('Genera by ago / Concept')
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.Splitter = wxSplitterWindow(id=wxID_MAINFRAMESPLITTER,
              name='Splitter', parent=self, point=wxPoint(0, 0),
              size=wxSize(640, 429), style=wxSP_3D)
        self.Splitter.SetMinimumPaneSize(250)

        self.componentsTree = wxTreeCtrl(id=wxID_MAINFRAMECOMPONENTSTREE,
              name='componentsTree', parent=self.Splitter, pos=wxPoint(2, 2),
              size=wxSize(250, 713), style=wxTR_HAS_BUTTONS,
              validator=wxDefaultValidator)
        self.componentsTree.SetToolTipString('Components tree')
        EVT_TREE_SEL_CHANGED(self.componentsTree, wxID_MAINFRAMECOMPONENTSTREE,
              self.OnComponentstreeTreeSelChanged)

        self.componentsNotebook = wxNotebook(id=wxID_MAINFRAMECOMPONENTSNOTEBOOK,
              name='componentsNotebook', parent=self.Splitter, pos=wxPoint(259,
              2), size=wxSize(883, 713), style=0)
        self.componentsNotebook.SetToolTipString('Components Notebook')
        EVT_NOTEBOOK_PAGE_CHANGED(self.componentsNotebook,
              wxID_MAINFRAMECOMPONENTSNOTEBOOK,
              self.OnComponentsnotebookNotebookPageChanged)
        EVT_SIZE(self.componentsNotebook, self.OnComponentsNotebookSize)
        self.Splitter.SplitVertically(self.componentsTree,
              self.componentsNotebook, 250)

        self.generaToolBar = wxToolBar(id=wxID_MAINFRAMEGENERATOOLBAR,
              name='generaToolBar', parent=self, pos=wxPoint(0, 26),
              size=wxSize(970, 22),
              style=wxTB_NOICONS | wxTB_HORIZONTAL | wxTB_TEXT)
        self.generaToolBar.SetThemeEnabled(False)
        self.SetToolBar(self.generaToolBar)

        self._init_coll_generaToolBar_Tools(self.generaToolBar)

    def __init__(self, parent):
        self._init_ctrls(parent)

        self.Reset()

    def Reset(self):
        self.rootItem = self.componentsTree.AddRoot('DEMO')
        self.scenesItem = self.componentsTree.AppendItem(self.rootItem, 'SCENES')
        self.parametersItem = self.componentsTree.AppendItem(self.rootItem, 'PARAMETERS')
        self.modelsItem = self.componentsTree.AppendItem(self.rootItem, 'MODELS')
        self.texturesItem = self.componentsTree.AppendItem(self.rootItem, 'TEXTURES')
        self.curvesItem = self.componentsTree.AppendItem(self.rootItem, 'CURVES')
        self.gradientsItem = self.componentsTree.AppendItem(self.rootItem, 'GRADIENTS')
        self.componentsTree.Expand(self.rootItem)
        
        #Store component pages indexed by their name
        self.componentsList = {}
        
        #Store number of every component
        self.numberOfScenes = 0
        self.numberOfParameters = 0
        self.numberOfModels = 0
        self.numberOfTextures = 0
        self.numberOfCurves = 0
        self.numberOfGradients = 0
        
        #Store tree item indexed by their position in the notebook
        self.items = []
        
        #Components type list
        self.componentsType = ['GRADIENTS', 'CURVES', 'TEXTURES',
            'MODELS', 'PARAMETERS', 'SCENES']

        #Init generator
        self.generator = genera.Genera()

    #New
    def OnMenufileitems0Menu(self, event):
        self.NewProject()
        event.Skip()

    #Open
    def OnMenufileitems1Menu(self, event):
        self.Open()
        event.Skip()

    #Save as
    def OnMenufileitems3Menu(self, event):
        self.SaveAs()
        event.Skip()

    #Exit
    def OnMenufileitems5Menu(self, event):
        self.Exit()
        event.Skip()

    def AddScene(self):
        #Get new scene name
        dlg = wxTextEntryDialog(self, 'Type a name for the new scene',
            'New scene name', 'Scene' + str(self.numberOfScenes))
        try:
            if dlg.ShowModal() == wxID_OK:
                answer = dlg.GetValue()
                
                if not answer in self.componentsList:
                
                    #Add a new scene to the components tree
                    item = self.componentsTree.AppendItem(self.scenesItem, answer)
                    self.componentsTree.Expand(self.scenesItem)

                    #Create a new scene
                    temp = wxScenePanel.wxScenePanel(id=-1,
                        name='scenePanel', parent=self.componentsNotebook,
                        pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

                    #Add page to components list
                    self.componentsList[answer] = self.componentsNotebook.GetPageCount()
                    
                    #Add item to scenes pages
                    self.items.append(item)

                    #Add scene page to notebook
                    self.componentsNotebook.AddPage(temp, answer, TRUE)

                    #Select current scene in component tree
                    self.componentsTree.SelectItem(item)
                    
                    #Increment number of scenes
                    self.numberOfScenes += 1

                else:
                    dlg = wxMessageDialog(self,
                        'There\'s already a component named "' + answer + '"',
                        'Error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    
        finally:
            dlg.Destroy()

    def AddParameter(self):
        #Get new parameter name
        dlg = wxTextEntryDialog(self, 'Type a name for the new parameter',
            'New parameter name', 'Parameter' + str(self.numberOfParameters))
        try:
            if dlg.ShowModal() == wxID_OK:
                answer = dlg.GetValue()
                
                if not answer in self.componentsList:
                
                    #Add a new parameter to the components tree
                    item = self.componentsTree.AppendItem(self.parametersItem, answer)
                    self.componentsTree.Expand(self.parametersItem)

                    #Create a new parameter
                    temp = wxParameterPanel.wxParameterPanel(id=-1,
                        name='parameterPanel', parent=self.componentsNotebook,
                        pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

                    #Add page to components list
                    self.componentsList[answer] = self.componentsNotebook.GetPageCount()
                    
                    #Add item to parameters pages
                    self.items.append(item)

                    #Add parameter page to notebook
                    self.componentsNotebook.AddPage(temp, answer, TRUE)

                    #Select current parameter in component tree
                    self.componentsTree.SelectItem(item)

                    #Increment number of parameters
                    self.numberOfParameters += 1

                else:
                    dlg = wxMessageDialog(self,
                        'There\'s already a component named "' + answer + '"',
                        'Error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    
        finally:
            dlg.Destroy()

    def AddModel(self):
        #Get new model name
        dlg = wxTextEntryDialog(self, 'Type a name for the new model',
            'New model name', 'Model' + str(self.numberOfModels))
        try:
            if dlg.ShowModal() == wxID_OK:
                answer = dlg.GetValue()
                
                if not answer in self.componentsList:
                
                    #Add a new model to the components tree
                    item = self.componentsTree.AppendItem(self.modelsItem, answer)
                    self.componentsTree.Expand(self.modelsItem)

                    #Create a new model
                    temp = wxModelPanel.wxModelPanel(id=-1,
                        name='modelPanel', parent=self.componentsNotebook,
                        pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

                    #Add page to components list
                    self.componentsList[answer] = self.componentsNotebook.GetPageCount()

                    #Add item to models pages
                    self.items.append(item)

                    #Add model page to notebook
                    self.componentsNotebook.AddPage(temp, answer, TRUE)

                    #Select current model in component tree
                    self.componentsTree.SelectItem(item)

                    #Increment number of models
                    self.numberOfModels += 1

                else:
                    dlg = wxMessageDialog(self,
                        'There\'s already a component named "' + answer + '"',
                        'Error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    
        finally:
            dlg.Destroy()

    def AddTexture(self):
        #Get new texture name
        dlg = wxTextEntryDialog(self, 'Type a name for the new texture',
            'New texture name', 'Texture' + str(self.numberOfTextures))
        try:
            if dlg.ShowModal() == wxID_OK:
                answer = dlg.GetValue()
                
                if not answer in self.componentsList:
                
                    #Add a new texture to the components tree
                    item = self.componentsTree.AppendItem(self.texturesItem, answer)
                    self.componentsTree.Expand(self.texturesItem)

                    #Create a new texture
                    temp = wxTexturePanel.wxTexturePanel(id=-1,
                        name='texturePanel', parent=self.componentsNotebook,
                        pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

                    #Add page to components list
                    self.componentsList[answer] = self.componentsNotebook.GetPageCount()

                    #Add item to textures pages
                    self.items.append(item)

                    #Add texture page to notebook
                    self.componentsNotebook.AddPage(temp, answer, TRUE)

                    #Select current texture in component tree
                    self.componentsTree.SelectItem(item)

                    #Increment number of textures
                    self.numberOfTextures += 1

                else:
                    dlg = wxMessageDialog(self,
                        'There\'s already a component named "' + answer + '"',
                        'Error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    
        finally:
            dlg.Destroy()

    def AddCurve(self):
        #Get new curve name
        dlg = wxTextEntryDialog(self, 'Type a name for the new curve',
            'New curve name', 'Curve' + str(self.numberOfCurves))
        try:
            if dlg.ShowModal() == wxID_OK:
                answer = dlg.GetValue()
                
                if not answer in self.componentsList:
                
                    #Add a new curve to the components tree
                    item = self.componentsTree.AppendItem(self.curvesItem, answer)
                    self.componentsTree.Expand(self.curvesItem)

                    #Create a new curve
                    temp = wxCurvePanel.wxCurvePanel(id=-1,
                        name='curvePanel', parent=self.componentsNotebook,
                        pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

                    #Add page to components list
                    self.componentsList[answer] = self.componentsNotebook.GetPageCount()

                    #Add item to curves pages
                    self.items.append(item)

                    #Add curve page to notebook
                    self.componentsNotebook.AddPage(temp, answer, TRUE)

                    #Select current curve in component tree
                    self.componentsTree.SelectItem(item)

                    #Increment number of curves
                    self.numberOfCurves += 1

                else:
                    dlg = wxMessageDialog(self,
                        'There\'s already a component named "' + answer + '"',
                        'Error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    
        finally:
            dlg.Destroy()

    def AddGradient(self):
        #Get new gradient name
        dlg = wxTextEntryDialog(self, 'Type a name for the new gradient',
            'New gradient name', 'Gradient' + str(self.numberOfGradients))
        try:
            if dlg.ShowModal() == wxID_OK:
                answer = dlg.GetValue()
                
                if not answer in self.componentsList:
                
                    #Add a new gradient to the components tree
                    item = self.componentsTree.AppendItem(self.gradientsItem, answer)
                    self.componentsTree.Expand(self.gradientsItem)

                    #Create a new gradient
                    temp = wxGradientPanel.wxGradientPanel(id=-1,
                        name='gradientPanel', parent=self.componentsNotebook,
                        pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

                    #Add page to components list
                    self.componentsList[answer] = self.componentsNotebook.GetPageCount()
                
                    #Add item to gradients pages
                    self.items.append(item)

                    #Add gradient page to notebook
                    self.componentsNotebook.AddPage(temp, answer, TRUE)
                    
                    #Select current gradient in component tree
                    self.componentsTree.SelectItem(item)

                    #Increment number of Gradients
                    self.numberOfGradients += 1

                else:
                    dlg = wxMessageDialog(self,
                        'There\'s already a component named "' + answer + '"',
                        'Error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    
        finally:
            dlg.Destroy()

    #Add scene
    def OnMenucomponentsitems0Menu(self, event):
        self.AddScene()
        event.Skip()

    #Add parameter
    def OnMenucomponentsitems1Menu(self, event):
        self.AddParameter()
        event.Skip()

    #Add model
    def OnMenucomponentsitems2Menu(self, event):
        self.AddModel()
        event.Skip()

    #Add texture
    def OnMenucomponentsitems3Menu(self, event):
        self.AddTexture()
        event.Skip()

    #Add curve
    def OnMenucomponentsitems4Menu(self, event):
        self.AddCurve()
        event.Skip()

    #Add gradient
    def OnMenucomponentsitems5Menu(self, event):
        self.AddGradient()
        event.Skip()

    #Rename component
    def OnMenuComponentsItems_renameMenu(self, event):
        self.RenameComponent()
        event.Skip()

    #Delete component
    def OnMenuComponentsItems_deleteMenu(self, event):
        self.DeleteComponent()
        event.Skip()


    #About
    def OnMenuhelpitems0Menu(self, event):
        dlg = wxMessageDialog(self, 'Made by ago/Concept (aka Santi Gallego)\n'\
          'http://www.wearevastlysuperior.com\n'\
          'Made with wxPython (http://wxpython.sf.net)',
          'About Concept\'s generator', wxOK | wxICON_INFORMATION)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()        
        event.Skip()

    #Selected item has changed in components tree
    def OnComponentstreeTreeSelChanged(self, event):
        itemID = self.componentsTree.GetSelection()

        if itemID == self.componentsTree.GetRootItem():
            #TODO: Add generator logo and demo properties here
            pass

        currentItemName = self.componentsTree.GetItemText(itemID)
        parentID = self.componentsTree.GetItemParent(itemID)

        if self.componentsTree.GetItemText(parentID) in self.componentsType:
            notebookPage = self.componentsList[currentItemName]
            
            if notebookPage != self.componentsNotebook.GetSelection():
                self.componentsNotebook.SetSelection(notebookPage)

        #Update gradients and curves list in textures
        for treeItem in self.items:
            if self.componentsTree.GetItemParent(treeItem) == self.texturesItem:
                #Get component name
                componentName = self.componentsTree.GetItemText(treeItem)

                #Get component page
                componentPage = self.componentsList[componentName]

                #Update
                if componentPage < self.componentsNotebook.GetPageCount():
                    self.componentsNotebook.GetPage(componentPage).gradientChoices = self.GetGradients()
                    self.componentsNotebook.GetPage(componentPage).curveChoices = self.GetCurves()
                    self.componentsNotebook.GetPage(componentPage).SetCurrentFX()
                    self.componentsNotebook.GetPage(componentPage).Redraw()

        #Update textures and curves list in models
        for treeItem in self.items:
            if self.componentsTree.GetItemParent(treeItem) == self.modelsItem:
                #Get component name
                componentName = self.componentsTree.GetItemText(treeItem)

                #Get component page
                componentPage = self.componentsList[componentName]

                #Update
                if componentPage < self.componentsNotebook.GetPageCount():
                    self.componentsNotebook.GetPage(componentPage).textureChoices = self.GetTextures()
                    self.componentsNotebook.GetPage(componentPage).curveChoices = self.GetCurves()
                    self.componentsNotebook.GetPage(componentPage).SetCurrentFX()
                    self.componentsNotebook.GetPage(componentPage).Redraw()

        event.Skip()

    #Selected item has changed in notebook
    def OnComponentsnotebookNotebookPageChanged(self, event):
        currentPage = event.GetSelection()
        
        if currentPage > -1:
            item = self.items[currentPage]
        
            if item != self.componentsTree.GetSelection():
                self.componentsTree.SelectItem(item)
        
        event.Skip()

    def OnGeneraToolBarTools_newTool(self, event):
        self.NewProject()
        event.Skip()

    def OnGeneraToolBarTools_openTool(self, event):
        self.Open()
        event.Skip()

    def OnGeneraToolBarTools_saveasTool(self, event):
        self.SaveAs()
        event.Skip()

    def OnGeneraToolBarTools_gradientTool(self, event):
        self.AddGradient()
        event.Skip()

    def OnGeneraToolBarTools_curveTool(self, event):
        self.AddCurve()
        event.Skip()

    def OnGeneraToolBarTools_textureTool(self, event):
        self.AddTexture()
        event.Skip()

    def OnGeneraToolBarTools_modelsTool(self, event):
        self.AddModel()
        event.Skip()

    def OnGeneraToolBarTools_parameterTool(self, event):
        self.AddParameter()
        event.Skip()

    def OnGeneraToolBarTools_sceneTool(self, event):
        self.AddScene()
        event.Skip()

    def OnGeneraToolBarTools_generatecomponentTool(self, event):
        #TODO: Generate only current component
        event.Skip()

    def OnGeneraToolBarTools_generateallTool(self, event):
        #Generate all components in the project
        self.GenerateAll()
        
        #Repaint current component
        pageNumber = self.componentsNotebook.GetSelection()
        if pageNumber > -1:
            self.componentsNotebook.GetPage(pageNumber).Redraw()
            
        event.Skip()

    #Check if any component is selected
    def componentIsSelected(self):
        itemID = self.componentsTree.GetSelection()
        parentID = self.componentsTree.GetItemParent(itemID)
        
        return self.componentsTree.GetItemText(parentID) in self.componentsType

    def updatePages(self, number):
        #Update page numbers, substracting 1 to every page whose number is greater than 'number'
        list = self.componentsList.keys()
        for i in range(0, len(list)):
            if self.componentsList[list[i]] > number:
                self.componentsList[list[i]] = self.componentsList[list[i]]-1

    def RenameComponent(self):
        #Check if any component is selected
        if not self.componentIsSelected():
            dlg = wxMessageDialog(self, 'No component selected',
              'Error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            return          
        
        #Confirm and rename current component
        dlg = wxTextEntryDialog(self, 'Type the new name for the component',
            'Rename component', '')
        try:
            if dlg.ShowModal() == wxID_OK:
                answer = dlg.GetValue()
                
                itemID = self.componentsTree.GetSelection()
                parentID = self.componentsTree.GetItemParent(itemID)

                if not answer in self.componentsList:
                    #Get component name
                    componentName = self.componentsTree.GetItemText(itemID)
            
                    #Get page number
                    pageNumber = self.componentsNotebook.GetSelection()

                    #Rename notebook page
                    self.componentsNotebook.SetPageText(pageNumber, answer)

                    #Rename component name in components tree
                    self.componentsTree.SetItemText(itemID, answer)

                    #Change key name in componentsList
                    self.componentsList[answer] = self.componentsList[componentName]
                    del self.componentsList[componentName]
                    
                else:
                    dlg = wxMessageDialog(self,
                        'There\'s already a component named "' + answer + '"',
                        'Error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()

        finally:
            dlg.Destroy()

    def DeleteComponent(self):
        #Check if any component is selected
        if not self.componentIsSelected():
            dlg = wxMessageDialog(self, 'No component selected',
              'Error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            return          
        
        #Confirm and delete current component
        dlg = wxMessageDialog(self, 
        'Really want to delete current component?', 'Delete component',
          wxYES_NO | wxNO_DEFAULT | wxICON_QUESTION)
        try:
             selected = dlg.ShowModal()
        finally:
            dlg.Destroy()
        
        if selected == wxID_YES:
            itemID = self.componentsTree.GetSelection()
            parentID = self.componentsTree.GetItemParent(itemID)
            
            #Get component name
            componentName = self.componentsTree.GetItemText(itemID)
            
            #Get page number
            pageNumber = self.componentsNotebook.GetSelection()

            #Delete component from tree
            self.componentsTree.Delete(itemID)
            
            #Delete component from proper list
            if self.componentsTree.GetItemText(parentID) in self.componentsType:
                del self.componentsList[componentName]
            self.updatePages(pageNumber)

            #Delete tree item from notebook list
            del self.items[pageNumber]
            
            # Delete notebook page
            self.componentsNotebook.DeletePage(pageNumber)
            
    def OnGeneraToolBarTools_rename_componentTool(self, event):
        self.RenameComponent()
        event.Skip()

    def OnGeneraToolBarTools_deletecomponentTool(self, event):
        self.DeleteComponent()
        event.Skip()

    def OnComponentsNotebookSize(self, event):
        event.Skip()

    def NewProject(self):
        dlg = wxMessageDialog(self, 'Really want to close current project and create a new one?',
            'New project', wxYES_NO | wxNO_DEFAULT | wxICON_QUESTION)
        try:
            selected = dlg.ShowModal()
        finally:
            dlg.Destroy()

        if selected == wxID_YES:
            
            # Delete all notebook pages
            self.componentsNotebook.DeleteAllPages()
            
            # Delete all tree items
            self.componentsTree.DeleteAllItems()

            self.Reset()

    def OpenCPT(self, fileName, name):
        name = name.rstrip(".cpt")
        
        #Unpickle project
        f = open(fileName, "rb")

        #Save number of components
        numberOfItems = pickle.load(f)
                
        #Iterate and save every component name
        for i in range(numberOfItems):
            #Load every component
            componentName = pickle.load(f)
            
            componentPath = fileName[0:fileName.rfind("/")+1]
            
            if componentName.endswith(".grd"):
                self.OpenGRD(componentPath+componentName, componentName)
            elif componentName.endswith(".crv"):
                self.OpenCRV(componentPath+componentName, componentName)
            elif componentName.endswith(".txr"):
                self.OpenTXR(componentPath+componentName, componentName)
            elif componentName.endswith(".mdl"):
                self.OpenMDL(componentPath+componentName, componentName)
            elif componentName.endswith(".prm"):
                self.OpenPRM(componentPath+componentName, componentName)
            elif componentName.endswith(".txr"):
                self.OpenTXR(componentPath+componentName, componentName)

        #Select last component in component tree
        self.componentsTree.SelectItem(self.items[numberOfItems-1])
        
        f.close()
        
    def OpenGRD(self, fileName, name):
        name = name.rstrip(".grd")
        
        if not name in self.componentsList:
        
            #Add a new gradient to the components tree
            item = self.componentsTree.AppendItem(self.gradientsItem, name)
            self.componentsTree.Expand(self.gradientsItem)

            #Add a new gradient to the notebook
            temp = wxGradientPanel.wxGradientPanel(id=-1,
                name='gradientPanel', parent=self.componentsNotebook,
                pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

            #Load data from file
            temp.Load(fileName)
                        
            #Add page to components list
            self.componentsList[name] = self.componentsNotebook.GetPageCount()

            #Add item to gradients pages
            self.items.append(item)

            #Add gradient page to notebook
            self.componentsNotebook.AddPage(temp, name, TRUE)

            #Select current gradient in component tree
            self.componentsTree.SelectItem(item)

            #Increment number of gradients
            self.numberOfGradients += 1
                        
        else:
            dlg = wxMessageDialog(self,
                'There\'s already a component named "' + name + '"',
                'Error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

    def OpenCRV(self, fileName, name):
        name = name.rstrip(".crv")
        
        if not name in self.componentsList:
                
            #Add a new curve to the components tree
            item = self.componentsTree.AppendItem(self.curvesItem, name)
            self.componentsTree.Expand(self.curvesItem)

            #Add a new curve to the notebook
            temp = wxCurvePanel.wxCurvePanel(id=-1,
                name='curvePanel', parent=self.componentsNotebook,
                pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

            #Load data from file
            temp.Load(fileName)
            
            #Add page to components list
            self.componentsList[name] = self.componentsNotebook.GetPageCount()

            #Add item to curves pages
            self.items.append(item)

            #Add curve page to notebook
            self.componentsNotebook.AddPage(temp, name, TRUE)

            #Select current curve in component tree
            self.componentsTree.SelectItem(item)

            #Increment number of curves
            self.numberOfCurves += 1
            
        else:
            dlg = wxMessageDialog(self,
                'There\'s already a component named "' + name + '"',
                'Error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

    def OpenTXR(self, fileName, name):
        name = name.rstrip(".txr")
        
        if not name in self.componentsList:
        
            #Add a new texture to the components tree
            item = self.componentsTree.AppendItem(self.texturesItem, name)
            self.componentsTree.Expand(self.texturesItem)

            #Add a new texture to the notebook
            temp = wxTexturePanel.wxTexturePanel(id=-1,
                name='texturePanel', parent=self.componentsNotebook,
                pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

            #Load data from file
            temp.Load(fileName)
            
            #Add page to components list
            self.componentsList[name] = self.componentsNotebook.GetPageCount()

            #Add item to textures pages
            self.items.append(item)

            #Add texture page to notebook
            self.componentsNotebook.AddPage(temp, name, TRUE)

            #Select current texture in component tree
            self.componentsTree.SelectItem(item)

            #Increment number of textures
            self.numberOfTextures += 1
            
        else:
            dlg = wxMessageDialog(self,
                'There\'s already a component named "' + name + '"',
                'Error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

    def OpenMDL(self, fileName, name):
        name = name.rstrip(".mdl")
        
        if not name in self.componentsList:
        
            #Add a new model to the components tree
            item = self.componentsTree.AppendItem(self.modelsItem, name)
            self.componentsTree.Expand(self.modelsItem)

            #Add a new model to the notebook
            temp = wxModelPanel.wxModelPanel(id=-1,
                name='modelPanel', parent=self.componentsNotebook,
                pos=wxPoint(159, 2), size=wxSize(639, 254), style=0)

            #Load data from file
            temp.Load(fileName)
            
            #Add page to components list
            self.componentsList[name] = self.componentsNotebook.GetPageCount()

            #Add item to models pages
            self.items.append(item)

            #Add model page to notebook
            self.componentsNotebook.AddPage(temp, name, TRUE)

            #Select current model in component tree
            self.componentsTree.SelectItem(item)

            #Increment number of models
            self.numberOfModels += 1
            
        else:
            dlg = wxMessageDialog(self,
                'There\'s already a component named "' + name + '"',
                'Error', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

    def OpenPRM(self, fileName, name):
        #TODO
        pass

    def OpenSCN(self, fileName, name):
        #TODO
        pass

    def Open(self):
        dlg = wxFileDialog(self, "Choose a file", ".", "",
            fileTypesOpen, wxOPEN | wxCHANGE_DIR)
        try:
            if dlg.ShowModal() == wxID_OK:
                fileName = dlg.GetPath()
                name = dlg.GetFilename()
                
                #Create a new component and open it
                if name.endswith(".cpt"):
                    self.OpenCPT(fileName, name)

                elif name.endswith(".grd"):
                    self.OpenGRD(fileName, name)

                elif name.endswith(".crv"):
                    self.OpenCRV(fileName, name)
                    
                elif name.endswith(".txr"):
                    self.OpenTXR(fileName, name)

                elif name.endswith(".mdl"):
                    self.OpenMDL(fileName, name)

                elif name.endswith(".prm"):
                    self.OpenPRM(fileName, name)

                elif name.endswith(".scn"):
                    self.OpenSCN(fileName, name)

                #Generate all
                self.GenerateAll()

                #Repaint current component
                pageNumber = self.componentsNotebook.GetSelection()
                self.componentsNotebook.GetPage(pageNumber).Redraw()

        finally:
            dlg.Destroy()

    def SaveAs(self):
        #Save project file
        dlg = wxFileDialog(self, "Choose a file", ".", "", 
            fileTypesSave, wxSAVE | wxOVERWRITE_PROMPT | wxCHANGE_DIR)
        try:
            if dlg.ShowModal() == wxID_OK:
                fileName = dlg.GetPath()
                if dlg.GetFilename().endswith(".cpt") :
                    projectName = dlg.GetFilename()[0:-4]
                else :
                    projectName = dlg.GetFilename()

                #Pickle project
                f = open(fileName, "wb")

                #Save number of components
                pickle.dump(len(self.items), f)
                
                #Iterate and save every component name
                for treeItem in self.items:
                    if self.componentsTree.GetItemParent(treeItem) == self.gradientsItem:
                        str = ".grd"
                    elif self.componentsTree.GetItemParent(treeItem) == self.curvesItem:
                        str = ".crv"
                    elif self.componentsTree.GetItemParent(treeItem) == self.texturesItem:
                        str = ".txr"
                    elif self.componentsTree.GetItemParent(treeItem) == self.modelsItem:
                        str = ".mdl"
                    elif self.componentsTree.GetItemParent(treeItem) == self.parametersItem:
                        str = ".prm"
                    elif self.componentsTree.GetItemParent(treeItem) == self.scenesItem:
                        str = ".scn"

                    pickle.dump(self.componentsTree.GetItemText(treeItem) + str, f)

                f.close()
                
                #Iterate and save every component in an individual file
                for treeItem in self.items:

                    #Get component name
                    componentName = self.componentsTree.GetItemText(treeItem)
                    
                    #Get component page
                    componentPage = self.componentsList[componentName]
                    
                    #Save component
                    self.componentsNotebook.GetPage(componentPage).Save(componentName)
            
                # Save H file
                self.SaveH(projectName+".h")

                dlg = wxMessageDialog(self, 'Project %s saved' % (fileName,),
                  'Saved project', wxOK | wxICON_INFORMATION)
                try:
                    dlg.ShowModal()
                finally:
                    dlg.Destroy()
        
        finally:
            dlg.Destroy()

    def SaveH(self, fileName):
        f = open(fileName, "wt")

        f.write("#pragma pack(1)\n\n")
        f.write("unsigned char project[] = {\n\n")

        f.write("\t//Number of components (16 network ordered bits)\n")
        f.write("\t%d, %d,\n\n" % (len(self.items)/256, len(self.items)%256,))

        for treeItem in self.items:

            # Save component type
            f.write("\t//Component type\n")
            if self.componentsTree.GetItemParent(treeItem) == self.gradientsItem:
                f.write("\t0,\t\t//Gradient\n\n")
            elif self.componentsTree.GetItemParent(treeItem) == self.curvesItem:
                f.write("\t1,\t\t//Curve\n\n")
            elif self.componentsTree.GetItemParent(treeItem) == self.texturesItem:
                f.write("\t2,\t\t//Texture\n\n")
            elif self.componentsTree.GetItemParent(treeItem) == self.modelsItem:
                f.write("\t3,\t\t//Model\n\n")
            elif self.componentsTree.GetItemParent(treeItem) == self.parametersItem:
                f.write("\t4,\t\t//Parameter\n\n")
            elif self.componentsTree.GetItemParent(treeItem) == self.scenesItem:
                f.write("\t5,\t\t//Scene\n\n")

            #Get component name
            componentName = self.componentsTree.GetItemText(treeItem)

            #Get component page
            componentPage = self.componentsList[componentName]

            #Save component
            self.componentsNotebook.GetPage(componentPage).SaveH(f, componentName)

        f.write("};\n\n")
        f.write("#pragma pack()\n")

        f.close()

    def GetData(self):
        # Number of components
        output = pack('!H', len(self.items))

        for treeItem in self.items:

            # Save component type
            if self.componentsTree.GetItemParent(treeItem) == self.gradientsItem:
                output += pack('B', 0)      # Gradient
            elif self.componentsTree.GetItemParent(treeItem) == self.curvesItem:
                output += pack('B', 1)      # Curve
            elif self.componentsTree.GetItemParent(treeItem) == self.texturesItem:
                output += pack('B', 2)      # Texture
            elif self.componentsTree.GetItemParent(treeItem) == self.modelsItem:
                output += pack('B', 3)      # Model
            elif self.componentsTree.GetItemParent(treeItem) == self.parametersItem:
                output += pack('B', 4)      # Parameter
            elif self.componentsTree.GetItemParent(treeItem) == self.scenesItem:
                output += pack('B', 5)      # Scene

            #Get component name
            componentName = self.componentsTree.GetItemText(treeItem)

            #Get component page
            componentPage = self.componentsList[componentName]

            #Save component
            temp = self.componentsNotebook.GetPage(componentPage).GetData(componentName)
            output += temp
            
        return output

    def GenerateAll(self):
        busyInfo = wxBusyInfo('Please wait while generating...')
        dataString = self.GetData()
        self.generator.loadPy(dataString)
        self.generator.generateAll()

    def Exit(self):
        dlg = wxMessageDialog(self, 'Really want to exit?',
            'Exit', wxYES_NO | wxNO_DEFAULT | wxICON_QUESTION)
        try:
            selected = dlg.ShowModal()
        finally:
            dlg.Destroy()

        if selected == wxID_YES:
            self.Destroy()

    def OnMainFrameClose(self, event):
        self.Exit()
        
        #This works this way, so leave it commented...
        #event.Skip()

    def GetGradients(self):
        gradientsList = []
        for i in range(0, len(self.items)):
            #If it's a gradient, append its name to the list
            try :
                if self.componentsTree.GetItemParent(self.items[i]) == self.gradientsItem:
                    itemName = self.componentsTree.GetItemText(self.items[i])
                    gradientsList.append(itemName)
            except :
                None
        return gradientsList
    
    def GetCurves(self):
        curvesList = []
        for i in range(0, len(self.items)):
            #If it's a curve, append its name to the list
            try :
                if self.componentsTree.GetItemParent(self.items[i]) == self.curvesItem:
                    curvesList.append(self.componentsTree.GetItemText(self.items[i]))
            except :
                None
        return curvesList
    
    def GetTextures(self):
        texturesList = []
        for i in range(0, len(self.items)):
            #If it's a texture, append its name to the list
            try :
                if self.componentsTree.GetItemParent(self.items[i]) == self.texturesItem:
                    texturesList.append(self.componentsTree.GetItemText(self.items[i]))
            except :
                None
        return texturesList
