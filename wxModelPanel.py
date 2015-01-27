#Boa:FramePanel:wxModelPanel

from wxPython.wx import *
from wxPython.grid import *
from struct import *
from cStringIO import StringIO
from math import *
import Image
import pickle

import wxModelViewDialog

[wxID_WXMODELPANEL, wxID_WXMODELPANELFLATRADIOBUTTON, 
 wxID_WXMODELPANELFXLISTCTRL, wxID_WXMODELPANELFXSPLITTER, 
 wxID_WXMODELPANELGRIDFXPROPERTIES, wxID_WXMODELPANELMODELPANEL, 
 wxID_WXMODELPANELMODELSPLITTER, wxID_WXMODELPANELMODELWINDOW, 
 wxID_WXMODELPANELMOVETEXT, wxID_WXMODELPANELMOVEX1BUTTON, 
 wxID_WXMODELPANELMOVEX2BUTTON, wxID_WXMODELPANELMOVEY1BUTTON, 
 wxID_WXMODELPANELMOVEY2BUTTON, wxID_WXMODELPANELMOVEZ1BUTTON, 
 wxID_WXMODELPANELMOVEZ2BUTTON, wxID_WXMODELPANELPOSITIONTEXT, 
 wxID_WXMODELPANELRENDERMODEBOX, wxID_WXMODELPANELROTATECAMTEXT, 
 wxID_WXMODELPANELROTATECAMX1BUTTON, wxID_WXMODELPANELROTATECAMX2BUTTON, 
 wxID_WXMODELPANELROTATECAMY1BUTTON, wxID_WXMODELPANELROTATECAMY2BUTTON, 
 wxID_WXMODELPANELROTATECAMZ1BUTTON, wxID_WXMODELPANELROTATECAMZ2BUTTON, 
 wxID_WXMODELPANELROTATEVIEWTEXT, wxID_WXMODELPANELROTATEVIEWX1BUTTON, 
 wxID_WXMODELPANELROTATEVIEWX2BUTTON, wxID_WXMODELPANELROTATEVIEWY1BUTTON, 
 wxID_WXMODELPANELROTATEVIEWY2BUTTON, wxID_WXMODELPANELROTATEVIEWZ1BUTTON, 
 wxID_WXMODELPANELROTATEVIEWZ2BUTTON, wxID_WXMODELPANELSMOOTHRADIOBUTTON, 
 wxID_WXMODELPANELTARGETTEXT, wxID_WXMODELPANELUPTEXT, 
 wxID_WXMODELPANELVIEWBOX, wxID_WXMODELPANELWIRERADIOBUTTON, 
] = map(lambda _init_ctrls: wxNewId(), range(36))

[wxID_WXMODELPANELCONTEXTITEMMENUITEMS_ADD_FX, 
 wxID_WXMODELPANELCONTEXTITEMMENUITEMS_DEL_FX, 
 wxID_WXMODELPANELCONTEXTITEMMENUITEMS_MOVE_DOWN, 
 wxID_WXMODELPANELCONTEXTITEMMENUITEMS_MOVE_UP, 
] = map(lambda _init_coll_contextItemMenu_Items: wxNewId(), range(4))

[wxID_WXMODELPANELADDFXSUBMENUITEMS_BASE_MODELS, 
 wxID_WXMODELPANELADDFXSUBMENUITEMS_DISTORTIONS, 
 wxID_WXMODELPANELADDFXSUBMENUITEMS_TEXTURE, 
] = map(lambda _init_coll_addFXSubMenu_Items: wxNewId(), range(3))

[wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_CUBE, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_CYLINDER, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_EXTRUDE_CURVE, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_HEIGHT_FIELD, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_METABALL, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_OCTAHEDRON, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_SPHERE, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_STAR, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_SWEEP_CURVE, 
 wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_TORUS, 
] = map(lambda _init_coll_baseModelsSubMenu_Items: wxNewId(), range(10))

[wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_HEIGHT_MAP, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_MOVE, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_NOISE, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_REFINE, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_ROTATE, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_SCALE, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_SPHERIZE, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TAPER, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TESSELLATE, 
 wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TWIST, 
] = map(lambda _init_coll_distortionsSubMenu_Items: wxNewId(), range(10))

[wxID_WXMODELPANELTEXTURESUBMENUITEMS_ENVIRONMENT_MAP, 
 wxID_WXMODELPANELTEXTURESUBMENUITEMS_TEXTURE_MAP, 
] = map(lambda _init_coll_textureSubMenu_Items: wxNewId(), range(2))

[wxID_WXMODELPANELCONTEXTBACKGROUNDMENUITEMS_ADD_FX] = map(lambda _init_coll_contextBackgroundMenu_Items: wxNewId(), range(1))

# FX and parameters
parameters = {
    "Cube" :
        ["Active"],
    "Cylinder" :
        ["Segments","Active"],
    "Extrude curve" :
        ["Curve","Segments","Active"],
    "Height field" :
        ["Texture","Facets","Active"],
    "Metaball" :
        ["X Position","Y Position","Z Position","Power","Active"],
    "Octahedron" :
        ["Active"],
    "Sphere" :
        ["Segments","Rings","Active"],
    "Star" :
        ["Horizontal tips","Vertical tips","Min radius","Max radius","Segments","Rings","Active"],
    "Sweep curve" :
        ["Curve","Active"],
    "Torus" :
        ["Radius 1","Radius 2","Segments", "Rings","Active"],

    "Height map" :
        ["Type","Value","Texture","Active"],
    "Move" :
        ["X","Y","Z","Active"],
    "Noise" :
        ["Value", "Seed", "Active"],
    "Refine" :
        ["Active"],
    "Rotate" :
        ["Direction","Value","Active"],
    "Scale" :
        ["X","Y","Z","Active"],
    "Spherize" :
        ["Value", "Active"],
    "Taper" :
        ["Direction","Value","Active"],
    "Tessellate" :
        ["Active"],
    "Twist" :
        ["Direction","Value","Active"],

    "Environment map" :
        ["Texture","Active"],
    "Texture map" :
        ["Type","Texture","Active"],
}

# FX and initial values
initialValues = {
    "Cube" :
        ["Yes"],
    "Cylinder" :
        ["64","Yes"],
    "Extrude curve" :
        ["","64","Yes"],
    "Height field" :
        ["","64","Yes"],
    "Metaball" :
        ["0","0","0","0","Yes"],
    "Octahedron" :
        ["Yes"],
    "Sphere" :
        ["64","64","Yes"],
    "Star" :
        ["4","4","1","2","64","64","Yes"],
    "Sweep curve" :
        ["","Yes"],
    "Torus" :
        ["2","1","64","64","Yes"],

    "Height map" :
        ["XY","1","","Yes"],
    "Move" :
        ["0","0","0","Yes"],
    "Noise" :
        ["1","0","Yes"],
    "Refine" :
        ["Yes"],
    "Rotate" :
        ["X","0","Yes"],
    "Scale" :
        ["1","1","1","Yes"],
    "Spherize" :
        ["1","Yes"],
    "Taper" :
        ["X","1","Yes"],
    "Tessellate" :
        ["Yes"],
    "Twist" :
        ["X","0","Yes"],

    "Environment map" :
        ["","Yes"],
    "Texture map" :
        ["Spheric","","Yes"],
}

# FX list
FXList = [
    #Base models
    "Cube","Cylinder","Extrude curve","Height field","Metaball","Octahedron","Sphere","Star","Sweep curve","Torus",
    #Distortions
    "Height map","Move","Noise","Refine","Rotate","Scale","Spherize","Taper","Tessellate","Twist",
    #Texture
    "Environment map","Texture map"
]

typeChoices = ["XY", "XZ", "YZ", "Cylindric", "Spheric"]
directionChoices = ["X", "Y", "Z"]
booleanChoices = ["Yes", "No"]

# ##################################################################### #

class wxModelPanel(wxPanel):
    def _init_coll_contextItemMenu_Items(self, parent):
        # generated method, don't edit

        parent.AppendMenu(helpString='',
              id=wxID_WXMODELPANELCONTEXTITEMMENUITEMS_ADD_FX, item='Add FX',
              subMenu=self.addFXSubMenu)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELCONTEXTITEMMENUITEMS_DEL_FX, item='Delete FX',
              kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='',
              id=wxID_WXMODELPANELCONTEXTITEMMENUITEMS_MOVE_UP, item='Move up',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELCONTEXTITEMMENUITEMS_MOVE_DOWN,
              item='Move down', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXMODELPANELCONTEXTITEMMENUITEMS_DEL_FX,
              self.OnContextItemMenuItems_del_fxMenu)
        EVT_MENU(self, wxID_WXMODELPANELCONTEXTITEMMENUITEMS_MOVE_UP,
              self.OnContextItemMenuItems_move_upMenu)
        EVT_MENU(self, wxID_WXMODELPANELCONTEXTITEMMENUITEMS_MOVE_DOWN,
              self.OnContextItemMenuItems_move_downMenu)

    def _init_coll_addFXSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.AppendMenu(helpString='',
              id=wxID_WXMODELPANELADDFXSUBMENUITEMS_BASE_MODELS,
              item='Base Models', subMenu=self.baseModelsSubMenu)
        parent.AppendMenu(helpString='',
              id=wxID_WXMODELPANELADDFXSUBMENUITEMS_DISTORTIONS,
              item='Distortions', subMenu=self.distortionsSubMenu)
        parent.AppendMenu(helpString='',
              id=wxID_WXMODELPANELADDFXSUBMENUITEMS_TEXTURE, item='Texture',
              subMenu=self.textureSubMenu)

    def _init_coll_distortionsSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_HEIGHT_MAP,
              item='Height map', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_MOVE, item='Move',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_NOISE, item='Noise',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_REFINE, item='Refine',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_ROTATE, item='Rotate',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_SCALE, item='Scale',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_SPHERIZE,
              item='Spherize', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TAPER,
              item='Taper', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TESSELLATE,
              item='Tessellate', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TWIST, item='Twist',
              kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_HEIGHT_MAP,
              self.OnDistortionsSubMenuItems_height_mapMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_MOVE,
              self.OnDistortionsSubMenuItems_moveMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_NOISE,
              self.OnDistortionsSubMenuItems_noiseMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_REFINE,
              self.OnDistortionsSubMenuItems_refineMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_ROTATE,
              self.OnDistortionsSubMenuItems_rotateMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_SCALE,
              self.OnDistortionsSubMenuItems_scaleMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_SPHERIZE,
              self.OnDistortionsSubMenuItems_spherizeMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TAPER,
              self.OnDistortionsSubMenuItems_taperMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TESSELLATE,
              self.OnDistortionsSubMenuItems_tessellateMenu)
        EVT_MENU(self, wxID_WXMODELPANELDISTORTIONSSUBMENUITEMS_TWIST,
              self.OnDistortionsSubMenuItems_twistMenu)

    def _init_coll_textureSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXMODELPANELTEXTURESUBMENUITEMS_ENVIRONMENT_MAP,
              item='Environment map', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELTEXTURESUBMENUITEMS_TEXTURE_MAP,
              item='Texture map', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXMODELPANELTEXTURESUBMENUITEMS_ENVIRONMENT_MAP,
              self.OnTextureSubMenuItems_environment_mapMenu)
        EVT_MENU(self, wxID_WXMODELPANELTEXTURESUBMENUITEMS_TEXTURE_MAP,
              self.OnTextureSubMenuItems_texture_mapMenu)

    def _init_coll_baseModelsSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_CUBE, item='Cube',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_CYLINDER,
              item='Cylinder', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_EXTRUDE_CURVE,
              item='Extrude curve', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_HEIGHT_FIELD,
              item='Height field', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_METABALL,
              item='Metaball', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_OCTAHEDRON,
              item='Octahedron', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_SPHERE, item='Sphere',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_STAR, item='Star',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_SWEEP_CURVE,
              item='Sweep curve', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_TORUS, item='Torus',
              kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_CUBE,
              self.OnBaseModelsSubMenuItems_cubeMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_CYLINDER,
              self.OnBaseModelsSubMenuItems_cylinderMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_EXTRUDE_CURVE,
              self.OnBaseModelsSubMenuItems_extrude_curveMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_HEIGHT_FIELD,
              self.OnBaseModelsSubMenuItems_height_fieldMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_METABALL,
              self.OnBaseModelsSubMenuItems_metaballMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_OCTAHEDRON,
              self.OnBaseModelsSubMenuItems_octahedronMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_SPHERE,
              self.OnBaseModelsSubMenuItems_sphereMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_STAR,
              self.OnBaseModelsSubMenuItems_starMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_SWEEP_CURVE,
              self.OnBaseModelsSubMenuItems_sweep_curveMenu)
        EVT_MENU(self, wxID_WXMODELPANELBASEMODELSSUBMENUITEMS_TORUS,
              self.OnBaseModelsSubMenuItems_torusMenu)

    def _init_coll_FXListCtrl_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wxLIST_FORMAT_LEFT, heading='FX List',
              width=150)

    def _init_utils(self):
        # generated method, don't edit
        self.contextItemMenu = wxMenu(title='')

        self.addFXSubMenu = wxMenu(title='')

        self.baseModelsSubMenu = wxMenu(title='')

        self.distortionsSubMenu = wxMenu(title='')

        self.textureSubMenu = wxMenu(title='')

        self._init_coll_contextItemMenu_Items(self.contextItemMenu)
        self._init_coll_addFXSubMenu_Items(self.addFXSubMenu)
        self._init_coll_baseModelsSubMenu_Items(self.baseModelsSubMenu)
        self._init_coll_distortionsSubMenu_Items(self.distortionsSubMenu)
        self._init_coll_textureSubMenu_Items(self.textureSubMenu)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxPanel.__init__(self, id=wxID_WXMODELPANEL, name='wxModelPanel',
              parent=prnt, pos=wxPoint(309, 192), size=wxSize(787, 598),
              style=0)
        self._init_utils()
        self.SetClientSize(wxSize(787, 598))
        self.SetToolTipString('Model Panel')
        EVT_SIZE(self, self.OnWxModelPanelSize)

        self.modelSplitter = wxSplitterWindow(id=wxID_WXMODELPANELMODELSPLITTER,
              name='modelSplitter', parent=self, point=wxPoint(0, 0),
              size=wxSize(722, 598), style=wxSP_3D)
        self.modelSplitter.SetMinimumPaneSize(200)
        self.modelSplitter.SetToolTipString('Model Splitter')
        self.modelSplitter.SetMinimumPaneSize(200)

        self.FXSplitter = wxSplitterWindow(id=wxID_WXMODELPANELFXSPLITTER,
              name='FXSplitter', parent=self.modelSplitter, point=wxPoint(2, 2),
              size=wxSize(100, 314), style=wxSP_3D)
        self.FXSplitter.SetToolTipString('FX Splitter')
        self.FXSplitter.SetMinimumPaneSize(250)

        self.modelPanel = wxPanel(id=wxID_WXMODELPANELMODELPANEL,
              name='modelPanel', parent=self.modelSplitter, pos=wxPoint(209, 2),
              size=wxSize(511, 594), style=0)
        self.modelPanel.SetToolTipString('Models panel')
        EVT_SIZE(self.modelPanel, self.OnModelPanelSize)
        self.modelSplitter.SplitVertically(self.FXSplitter, self.modelPanel,
              200)

        self.FXListCtrl = wxListCtrl(id=wxID_WXMODELPANELFXLISTCTRL,
              name='FXListCtrl', parent=self.FXSplitter, pos=wxPoint(2, 2),
              size=wxSize(196, 250), style=wxLC_SINGLE_SEL | wxLC_REPORT)
        self.FXListCtrl.SetToolTipString('FXListCtrl')
        self._init_coll_FXListCtrl_Columns(self.FXListCtrl)
        EVT_RIGHT_DOWN(self.FXListCtrl, self.OnFXListCtrlRightDown)
        EVT_LIST_ITEM_SELECTED(self.FXListCtrl, wxID_WXMODELPANELFXLISTCTRL,
              self.OnFXListCtrlListItemSelected)
        EVT_LIST_ITEM_DESELECTED(self.FXListCtrl, wxID_WXMODELPANELFXLISTCTRL,
              self.OnFXListCtrlListItemDeselected)

        self.gridFXProperties = wxGrid(id=wxID_WXMODELPANELGRIDFXPROPERTIES,
              name='gridFXProperties', parent=self.FXSplitter, pos=wxPoint(2,
              259), size=wxSize(196, 333), style=0)
        self.gridFXProperties.SetColLabelSize(0)
        self.gridFXProperties.SetRowLabelSize(100)
        self.gridFXProperties.EnableGridLines(True)
        self.gridFXProperties.SetRowMinimalAcceptableHeight(100)
        EVT_GRID_CELL_CHANGE(self.gridFXProperties,
              self.OnGridFXPropertiesGridCellChange)
        EVT_GRID_CELL_LEFT_CLICK(self.gridFXProperties,
              self.OnGridFXPropertiesGridCellLeftClick)
        self.FXSplitter.SplitHorizontally(self.FXListCtrl,
              self.gridFXProperties, 182)

        self.modelWindow = wxWindow(id=wxID_WXMODELPANELMODELWINDOW,
              name='modelWindow', parent=self.modelPanel, pos=wxPoint(8, 8),
              size=wxSize(456, 456), style=wxSIMPLE_BORDER)
        EVT_LEFT_DOWN(self.modelWindow, self.OnModelWindowLeftDown)

        self.renderModeBox = wxStaticBox(id=wxID_WXMODELPANELRENDERMODEBOX,
              label='Render mode', name='renderModeBox', parent=self.modelPanel,
              pos=wxPoint(8, 472), size=wxSize(112, 112), style=0)

        self.wireRadioButton = wxRadioButton(id=wxID_WXMODELPANELWIRERADIOBUTTON,
              label='Wire', name='wireRadioButton', parent=self.modelPanel,
              pos=wxPoint(16, 488), size=wxSize(72, 32), style=0)
        self.wireRadioButton.SetValue(False)
        self.wireRadioButton.SetToolTipString('Render wired')
        EVT_RADIOBUTTON(self.wireRadioButton, wxID_WXMODELPANELWIRERADIOBUTTON,
              self.OnWireRadioButtonRadiobutton)

        self.flatRadioButton = wxRadioButton(id=wxID_WXMODELPANELFLATRADIOBUTTON,
              label='Flat', name='flatRadioButton', parent=self.modelPanel,
              pos=wxPoint(16, 520), size=wxSize(72, 32), style=0)
        self.flatRadioButton.SetValue(False)
        self.flatRadioButton.SetToolTipString('Render wired')
        EVT_RADIOBUTTON(self.flatRadioButton, wxID_WXMODELPANELFLATRADIOBUTTON,
              self.OnFlatRadioButtonRadiobutton)

        self.smoothRadioButton = wxRadioButton(id=wxID_WXMODELPANELSMOOTHRADIOBUTTON,
              label='Smooth', name='smoothRadioButton', parent=self.modelPanel,
              pos=wxPoint(16, 552), size=wxSize(72, 32), style=0)
        self.smoothRadioButton.SetValue(True)
        self.smoothRadioButton.SetToolTipString('Render wired')
        EVT_RADIOBUTTON(self.smoothRadioButton,
              wxID_WXMODELPANELSMOOTHRADIOBUTTON,
              self.OnSmoothRadioButtonRadiobutton)

        self.viewBox = wxStaticBox(id=wxID_WXMODELPANELVIEWBOX, label='View',
              name='viewBox', parent=self.modelPanel, pos=wxPoint(136, 472),
              size=wxSize(328, 112), style=0)

        self.moveText = wxStaticText(id=wxID_WXMODELPANELMOVETEXT,
              label='Move:', name='moveText', parent=self.modelPanel,
              pos=wxPoint(144, 496), size=wxSize(72, 24), style=0)

        self.moveX1Button = wxButton(id=wxID_WXMODELPANELMOVEX1BUTTON,
              label='+X', name='moveX1Button', parent=self.modelPanel,
              pos=wxPoint(216, 496), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.moveX1Button, wxID_WXMODELPANELMOVEX1BUTTON,
              self.OnMoveX1ButtonButton)

        self.moveX2Button = wxButton(id=wxID_WXMODELPANELMOVEX2BUTTON,
              label='-X', name='moveX2Button', parent=self.modelPanel,
              pos=wxPoint(256, 496), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.moveX2Button, wxID_WXMODELPANELMOVEX2BUTTON,
              self.OnMoveX2ButtonButton)

        self.moveY1Button = wxButton(id=wxID_WXMODELPANELMOVEY1BUTTON,
              label='+Y', name='moveY1Button', parent=self.modelPanel,
              pos=wxPoint(296, 496), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.moveY1Button, wxID_WXMODELPANELMOVEY1BUTTON,
              self.OnMoveY1ButtonButton)

        self.moveY2Button = wxButton(id=wxID_WXMODELPANELMOVEY2BUTTON,
              label='-Y', name='moveY2Button', parent=self.modelPanel,
              pos=wxPoint(336, 496), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.moveY2Button, wxID_WXMODELPANELMOVEY2BUTTON,
              self.OnMoveY2ButtonButton)

        self.moveZ1Button = wxButton(id=wxID_WXMODELPANELMOVEZ1BUTTON,
              label='+Z', name='moveZ1Button', parent=self.modelPanel,
              pos=wxPoint(376, 496), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.moveZ1Button, wxID_WXMODELPANELMOVEZ1BUTTON,
              self.OnMoveZ1ButtonButton)

        self.moveZ2Button = wxButton(id=wxID_WXMODELPANELMOVEZ2BUTTON,
              label='-Z', name='moveZ2Button', parent=self.modelPanel,
              pos=wxPoint(416, 496), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.moveZ2Button, wxID_WXMODELPANELMOVEZ2BUTTON,
              self.OnMoveZ2ButtonButton)

        self.rotateCamText = wxStaticText(id=wxID_WXMODELPANELROTATECAMTEXT,
              label='Rotate cam:', name='rotateCamText', parent=self.modelPanel,
              pos=wxPoint(144, 520), size=wxSize(65, 19), style=0)

        self.rotateCamX1Button = wxButton(id=wxID_WXMODELPANELROTATECAMX1BUTTON,
              label='+X', name='rotateCamX1Button', parent=self.modelPanel,
              pos=wxPoint(216, 520), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateCamX1Button, wxID_WXMODELPANELROTATECAMX1BUTTON,
              self.OnRotateCamX1ButtonButton)

        self.rotateCamX2Button = wxButton(id=wxID_WXMODELPANELROTATECAMX2BUTTON,
              label='-X', name='rotateCamX2Button', parent=self.modelPanel,
              pos=wxPoint(256, 520), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateCamX2Button, wxID_WXMODELPANELROTATECAMX2BUTTON,
              self.OnRotateCamX2ButtonButton)

        self.rotateCamY1Button = wxButton(id=wxID_WXMODELPANELROTATECAMY1BUTTON,
              label='+Y', name='rotateCamY1Button', parent=self.modelPanel,
              pos=wxPoint(296, 520), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateCamY1Button, wxID_WXMODELPANELROTATECAMY1BUTTON,
              self.OnRotateCamY1ButtonButton)

        self.rotateCamY2Button = wxButton(id=wxID_WXMODELPANELROTATECAMY2BUTTON,
              label='-Y', name='rotateCamY2Button', parent=self.modelPanel,
              pos=wxPoint(336, 520), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateCamY2Button, wxID_WXMODELPANELROTATECAMY2BUTTON,
              self.OnRotateCamY2ButtonButton)

        self.rotateCamZ1Button = wxButton(id=wxID_WXMODELPANELROTATECAMZ1BUTTON,
              label='+Z', name='rotateCamZ1Button', parent=self.modelPanel,
              pos=wxPoint(376, 520), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateCamZ1Button, wxID_WXMODELPANELROTATECAMZ1BUTTON,
              self.OnRotateCamZ1ButtonButton)

        self.rotateCamZ2Button = wxButton(id=wxID_WXMODELPANELROTATECAMZ2BUTTON,
              label='-Z', name='rotateCamZ2Button', parent=self.modelPanel,
              pos=wxPoint(416, 520), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateCamZ2Button, wxID_WXMODELPANELROTATECAMZ2BUTTON,
              self.OnRotateCamZ2ButtonButton)

        self.rotateViewText = wxStaticText(id=wxID_WXMODELPANELROTATEVIEWTEXT,
              label='Rotate view:', name='rotateViewText',
              parent=self.modelPanel, pos=wxPoint(144, 544), size=wxSize(67,
              19), style=0)

        self.rotateViewX1Button = wxButton(id=wxID_WXMODELPANELROTATEVIEWX1BUTTON,
              label='+X', name='rotateViewX1Button', parent=self.modelPanel,
              pos=wxPoint(216, 544), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateViewX1Button, wxID_WXMODELPANELROTATEVIEWX1BUTTON,
              self.OnRotateViewX1ButtonButton)

        self.rotateViewX2Button = wxButton(id=wxID_WXMODELPANELROTATEVIEWX2BUTTON,
              label='-X', name='rotateViewX2Button', parent=self.modelPanel,
              pos=wxPoint(256, 544), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateViewX2Button, wxID_WXMODELPANELROTATEVIEWX2BUTTON,
              self.OnRotateViewX2ButtonButton)

        self.rotateViewY1Button = wxButton(id=wxID_WXMODELPANELROTATEVIEWY1BUTTON,
              label='+Y', name='rotateViewY1Button', parent=self.modelPanel,
              pos=wxPoint(296, 544), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateViewY1Button, wxID_WXMODELPANELROTATEVIEWY1BUTTON,
              self.OnRotateViewY1ButtonButton)

        self.rotateViewY2Button = wxButton(id=wxID_WXMODELPANELROTATEVIEWY2BUTTON,
              label='-Y', name='rotateViewY2Button', parent=self.modelPanel,
              pos=wxPoint(336, 544), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateViewY2Button, wxID_WXMODELPANELROTATEVIEWY2BUTTON,
              self.OnRotateViewY2ButtonButton)

        self.rotateViewZ1Button = wxButton(id=wxID_WXMODELPANELROTATEVIEWZ1BUTTON,
              label='+Z', name='rotateViewZ1Button', parent=self.modelPanel,
              pos=wxPoint(376, 544), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateViewZ1Button, wxID_WXMODELPANELROTATEVIEWZ1BUTTON,
              self.OnRotateViewZ1ButtonButton)

        self.rotateViewZ2Button = wxButton(id=wxID_WXMODELPANELROTATEVIEWZ2BUTTON,
              label='-Z', name='rotateViewZ2Button', parent=self.modelPanel,
              pos=wxPoint(416, 544), size=wxSize(40, 25), style=0)
        EVT_BUTTON(self.rotateViewZ2Button, wxID_WXMODELPANELROTATEVIEWZ2BUTTON,
              self.OnRotateViewZ2ButtonButton)

        self.positionText = wxStaticText(id=wxID_WXMODELPANELPOSITIONTEXT,
              label='Pos ( ,  ,  )', name='positionText',
              parent=self.modelPanel, pos=wxPoint(472, 488), size=wxSize(53,
              19), style=0)

        self.targetText = wxStaticText(id=wxID_WXMODELPANELTARGETTEXT,
              label='Tar ( ,  ,  )', name='targetText', parent=self.modelPanel,
              pos=wxPoint(472, 520), size=wxSize(50, 19), style=0)

        self.upText = wxStaticText(id=wxID_WXMODELPANELUPTEXT,
              label='Up ( ,  ,  )', name='upText', parent=self.modelPanel,
              pos=wxPoint(472, 552), size=wxSize(48, 19), style=0)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
        
        #Store reference to MainFrame to get gradients and curves list
        self.MainFrame = self.GetParent().GetParent().GetParent()

        #Init grid control
        self.gridFXProperties.CreateGrid(0,1)
        
        #Init FX parameters
        self.FXparameters = []
        
        #Init choices
        self.curveChoices = []
        self.textureChoices = []

        #Init object
        image = wxEmptyImage(1, 1)
        image.SetRGB(0, 0, 0, 0, 0)
        size = self.modelWindow.GetSize()
        bitmap = wxBitmapFromImage(image.Scale(size.x, size.y))
        self.staticBitmap = wxStaticBitmap(self.modelWindow, -1, bitmap,
        wxPoint(0, 0), self.modelWindow.GetSize())
        EVT_LEFT_DOWN(self.staticBitmap, self.OnModelWindowLeftDown)
						    
        # Init camera
        self.xPosition = 0
        self.yPosition = 0
        self.zPosition = -20
        self.xTarget = 0
        self.yTarget = 0
        self.zTarget = 0
        self.xUp = 0
        self.yUp = 1
        self.zUp = 0
        
    def OnWxModelPanelSize(self, event):
        panelDC = wxClientDC(self)
        panelSize = panelDC.GetSize()
        self.modelSplitter.SetSize(panelSize)
        
        event.Skip()

    def OnModelPanelSize(self, event):
        modelPanelDC = wxClientDC(self.modelPanel)
        size = modelPanelDC.GetSize()
        
        width = size.GetWidth()-16
        height = size.GetHeight()-24-112
        
        # Make it square
        if width < height:
            height = width
        else:
            width = height

        # Event pops up before windows exist, so exception must be caught
        try:
            self.modelWindow.SetDimensions(8, 8, width, height)
            self.staticBitmap.SetDimensions(0, 0, width, height)
            
            self.renderModeBox.SetDimensions(8, 16+height, 104, 112)
            self.wireRadioButton.SetDimensions(24, 32+height, 72, 32)
            self.flatRadioButton.SetDimensions(24, 64+height, 72, 32)
            self.smoothRadioButton.SetDimensions(24, 96+height, 72, 32)
            
            self.viewBox.SetDimensions(120, 16+height, 344, 112)
            self.moveText.SetDimensions(136, 32+height, 72, 32)
            self.rotateCamText.SetDimensions(136, 64+height, 72, 32)
            self.rotateViewText.SetDimensions(136, 96+height, 72, 32)

            self.moveX1Button.SetDimensions(208, 32+height, 40, 25)
            self.moveX2Button.SetDimensions(248, 32+height, 40, 25)
            self.moveY1Button.SetDimensions(288, 32+height, 40, 25)
            self.moveY2Button.SetDimensions(328, 32+height, 40, 25)
            self.moveZ1Button.SetDimensions(368, 32+height, 40, 25)
            self.moveZ2Button.SetDimensions(408, 32+height, 40, 25)
            self.rotateCamX1Button.SetDimensions(208, 64+height, 40, 25)
            self.rotateCamX2Button.SetDimensions(248, 64+height, 40, 25)
            self.rotateCamY1Button.SetDimensions(288, 64+height, 40, 25)
            self.rotateCamY2Button.SetDimensions(328, 64+height, 40, 25)
            self.rotateCamZ1Button.SetDimensions(368, 64+height, 40, 25)
            self.rotateCamZ2Button.SetDimensions(408, 64+height, 40, 25)
            self.rotateViewX1Button.SetDimensions(208, 96+height, 40, 25)
            self.rotateViewX2Button.SetDimensions(248, 96+height, 40, 25)
            self.rotateViewY1Button.SetDimensions(288, 96+height, 40, 25)
            self.rotateViewY2Button.SetDimensions(328, 96+height, 40, 25)
            self.rotateViewZ1Button.SetDimensions(368, 96+height, 40, 25)
            self.rotateViewZ2Button.SetDimensions(408, 96+height, 40, 25)
            
            self.positionText.SetDimensions(472, 32+height, 96, 25)
            self.targetText.SetDimensions(472, 64+height, 96, 25)
            self.upText.SetDimensions(472, 96+height, 96, 25)

            self.Refresh()
        except:
            None

        event.Skip()

    def OnFXListCtrlRightDown(self, event):
        self.PopupMenu(self.contextItemMenu, event.GetPosition())
        event.Skip()

    def OnFXListCtrlListItemSelected(self, event):
        self.gridFXProperties.EnableCellEditControl()
        self.SetCurrentFX()
        event.Skip()

    def OnFXListCtrlListItemDeselected(self, event):
        self.gridFXProperties.SaveEditControlValue()
        self.gridFXProperties.DisableCellEditControl()

        # Remove previous FX parameters from grid
        if self.gridFXProperties.GetNumberRows() > 0:
            self.gridFXProperties.DeleteRows(0, self.gridFXProperties.GetNumberRows())

        event.Skip()
										    
    def OnGridFXPropertiesGridCellChange(self, event):
        # Get selected FX
        item = self.FXListCtrl.GetNextItem(-1, wxLIST_NEXT_ALL, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
        
        # If no FX selected, return now
        if item == -1:
            return
        
        row = event.GetRow()
        self.FXparameters[item][row] = self.gridFXProperties.GetCellValue(row, 0)
        
        event.Skip()

    def OnModelWindowLeftDown(self, event):
        dlg = wxModelViewDialog.wxModelViewDialog(self)
        dlg.SetTitle("Model view")
        dlg.Centre()

        # Get window size
        size = self.staticBitmap.GetSize()
        
        # Get current model name
        pageNumber = self.MainFrame.componentsNotebook.GetSelection()
        if pageNumber == -1:
            return
        modelName = self.MainFrame.componentsNotebook.GetPageText(pageNumber)

        # Get window size
        modelDC = wxClientDC(self.staticBitmap)
        size = modelDC.GetSize()
        width = size.GetWidth()
        height = size.GetHeight()

        renderMode = 2
        try:
            if self.wireRadioButton.GetValue():
                renderMode = 0
            elif self.flatRadioButton.GetValue():
                renderMode = 1
            elif self.smoothRadioButton.GetValue():
                renderMode = 2
        except:
            None

        str = self.MainFrame.generator.getRenderedModel(modelName,
            self.xPosition, self.yPosition, self.zPosition,
            self.xTarget, self.yTarget, self.zTarget,
            self.xUp, self.yUp, self.zUp,
            45, width, height, renderMode, width*height*4)

        if len(str) == width*height*4:
            # Create image
            source = Image.frombuffer("RGBA", (width, height), str)
            image = apply(wxEmptyImage, source.size)
            image.SetData( source.convert("RGB").tostring() )
    
            # Scale and convert to a displayable bitmap
            bitmap = wxBitmapFromImage(image.Scale(size.x, size.y).Mirror(False))

        dlg.SetBitmap(bitmap)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

        event.Skip()

    def OnGridFXPropertiesGridCellLeftClick(self, event):
        self.gridFXProperties.SetGridCursor(event.GetRow(), event.GetCol())
        if self.gridFXProperties.CanEnableCellControl():
            self.gridFXProperties.EnableCellEditControl()

    def SetCurrentFX(self):
        # Remove previous FX parameters from grid
        if self.gridFXProperties.GetNumberRows() > 0:
            self.gridFXProperties.DeleteRows(0, self.gridFXProperties.GetNumberRows())

        # Get selected FX
        if self.FXListCtrl.GetItemCount() > 0:
            item = self.FXListCtrl.GetNextItem(-1, wxLIST_NEXT_ALL, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
        
            # If no item selected, return now
            if item == -1:
                return

        else:
            return

        # Get FX name
        FXname = self.FXListCtrl.GetItemText(item)
        
        # Get parameters names
        parametersNames = parameters[FXname]

        # Insert rows
        self.gridFXProperties.InsertRows(0, len(parametersNames))
        
        for i in range(0, len(parametersNames)):
            #Set label title
            self.gridFXProperties.SetRowLabelValue(i, parametersNames[i])

            #Set cell editor
            if parametersNames[i] == "Direction":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(directionChoices))
            elif parametersNames[i] == "Type":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(typeChoices))
            elif parametersNames[i] == "Curve":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(self.curveChoices))
            elif parametersNames[i] == "Texture":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(self.textureChoices))
            elif parametersNames[i] == "Segments":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellNumberEditor(3, 255))
            elif parametersNames[i] == "Rings":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellNumberEditor(3, 255))
            elif parametersNames[i] == "Facets":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellNumberEditor(2, 255))
            elif parametersNames[i] == "Horizontal tips":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellNumberEditor(0, 255))
            elif parametersNames[i] == "Vertical tips":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellNumberEditor(0, 255))
            elif parametersNames[i] == "Seed":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellNumberEditor(0, 255))
            elif parametersNames[i] == "Active":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(booleanChoices))
            else:
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellFloatEditor())

            #Set cell value
            self.gridFXProperties.SetCellValue(i, 0, self.FXparameters[item][i])

    def drawBlackLayer(self):
        textureDC = wxClientDC(self.staticBitmap)
        size = textureDC.GetSize()

        textureDC.BeginDrawing()

        brush = wxBrush(wxColour(0,0,0), wxSOLID)
        textureDC.SetBrush(brush)

        textureDC.DrawRectangle(0, 0, size.GetWidth(), size.GetHeight())

        textureDC.EndDrawing()

    def Redraw(self):
        self.WriteCameraValues()

        # Get window size
        size = self.staticBitmap.GetSize()
        
        # Get current model name
        pageNumber = self.MainFrame.componentsNotebook.GetSelection()
        if pageNumber == -1:
            return
        modelName = self.MainFrame.componentsNotebook.GetPageText(pageNumber)

        # Get window size
        modelDC = wxClientDC(self.staticBitmap)
        size = modelDC.GetSize()
        width = size.GetWidth()
        height = size.GetHeight()

        renderMode = 2
        try:
            if self.wireRadioButton.GetValue():
                renderMode = 0
            elif self.flatRadioButton.GetValue():
                renderMode = 1
            elif self.smoothRadioButton.GetValue():
                renderMode = 2
        except:
            None

        str = self.MainFrame.generator.getRenderedModel(modelName,
            self.xPosition, self.yPosition, self.zPosition,
            self.xTarget, self.yTarget, self.zTarget,
            self.xUp, self.yUp, self.zUp,
            45, width, height, renderMode, width*height*4)

        if len(str) == width*height*4:
            # Create image
            source = Image.frombuffer("RGBA", (width, height), str)
            image = apply(wxEmptyImage, source.size)
            image.SetData( source.convert("RGB").tostring() )
    
            # Scale and convert to a displayable bitmap
            jpg = wxBitmapFromImage(image.Scale(size.x, size.y).Mirror(False))
    
            #Show it
            self.staticBitmap.SetBitmap(jpg)
        else:
            self.drawBlackLayer()

    def OnWireRadioButtonRadiobutton(self, event):
        self.Redraw()
        event.Skip()

    def OnFlatRadioButtonRadiobutton(self, event):
        self.Redraw()
        event.Skip()

    def OnSmoothRadioButtonRadiobutton(self, event):
        self.Redraw()
        event.Skip()

    def WriteCameraValues(self):
        self.positionText.SetLabel("Pos: (%.3f, %.3f, %.3f)" % (self.xPosition, self.yPosition, self.zPosition, ))
        self.targetText.SetLabel("Tgt: (%.3f, %.3f, %.3f)" % (self.xTarget, self.yTarget, self.zTarget, ))
        self.upText.SetLabel("Up: (%.3f, %.3f, %.3f)" % (self.xUp, self.yUp, self.zUp, ))

    def OnMoveX1ButtonButton(self, event):
        self.xPosition += 1
        self.xTarget += 1
        self.Redraw()
        event.Skip()

    def OnMoveX2ButtonButton(self, event):
        self.xPosition -= 1
        self.xTarget -= 1
        self.Redraw()
        event.Skip()

    def OnMoveY1ButtonButton(self, event):
        self.yPosition += 1
        self.yTarget += 1
        self.Redraw()
        event.Skip()

    def OnMoveY2ButtonButton(self, event):
        self.yPosition -= 1
        self.yTarget -= 1
        self.Redraw()
        event.Skip()

    def OnMoveZ1ButtonButton(self, event):
        self.zPosition += 1
        self.zTarget += 1
        self.Redraw()
        event.Skip()

    def OnMoveZ2ButtonButton(self, event):
        self.zPosition -= 1
        self.zTarget -= 1
        self.Redraw()
        event.Skip()

    def OnRotateCamX1ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xTarget - self.xPosition
        deltaY = self.yTarget - self.yPosition
        deltaZ = self.zTarget - self.zPosition
        self.yTarget = self.yPosition + deltaY*cos(angle) + deltaZ*sin(angle)
        self.zTarget = self.zPosition - deltaY*sin(angle) + deltaZ*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.yUp = + deltaY*cos(angle) + deltaZ*sin(angle)
        self.zUp = - deltaY*sin(angle) + deltaZ*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateCamX2ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xTarget - self.xPosition
        deltaY = self.yTarget - self.yPosition
        deltaZ = self.zTarget - self.zPosition
        self.yTarget = self.yPosition + deltaY*cos(angle) - deltaZ*sin(angle)
        self.zTarget = self.zPosition + deltaY*sin(angle) + deltaZ*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.yUp = + deltaY*cos(angle) - deltaZ*sin(angle)
        self.zUp = + deltaY*sin(angle) + deltaZ*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateCamY1ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xTarget - self.xPosition
        deltaY = self.yTarget - self.yPosition
        deltaZ = self.zTarget - self.zPosition
        self.xTarget = self.xPosition + deltaX*cos(angle) + deltaZ*sin(angle)
        self.zTarget = self.zPosition - deltaX*sin(angle) + deltaZ*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.xUp = + deltaX*cos(angle) + deltaZ*sin(angle)
        self.zUp = - deltaX*sin(angle) + deltaZ*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateCamY2ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xTarget - self.xPosition
        deltaY = self.yTarget - self.yPosition
        deltaZ = self.zTarget - self.zPosition
        self.xTarget = self.xPosition + deltaX*cos(angle) - deltaZ*sin(angle)
        self.zTarget = self.zPosition + deltaX*sin(angle) + deltaZ*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.xUp = + deltaX*cos(angle) - deltaZ*sin(angle)
        self.zUp = + deltaX*sin(angle) + deltaZ*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateCamZ1ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xTarget - self.xPosition
        deltaY = self.yTarget - self.yPosition
        deltaZ = self.zTarget - self.zPosition
        self.xTarget = self.xPosition + deltaX*cos(angle) + deltaY*sin(angle)
        self.yTarget = self.yPosition - deltaX*sin(angle) + deltaY*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.xUp = + deltaX*cos(angle) + deltaY*sin(angle)
        self.yUp = - deltaX*sin(angle) + deltaY*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateCamZ2ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xTarget - self.xPosition
        deltaY = self.yTarget - self.yPosition
        deltaZ = self.zTarget - self.zPosition
        self.xTarget = self.xPosition + deltaX*cos(angle) - deltaY*sin(angle)
        self.yTarget = self.yPosition + deltaX*sin(angle) + deltaY*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.xUp = + deltaX*cos(angle) - deltaY*sin(angle)
        self.yUp = + deltaX*sin(angle) + deltaY*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateViewX1ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xPosition - self.xTarget
        deltaY = self.yPosition - self.yTarget
        deltaZ = self.zPosition - self.zTarget
        self.yPosition = self.yTarget + deltaY*cos(angle) + deltaZ*sin(angle)
        self.zPosition = self.zTarget - deltaY*sin(angle) + deltaZ*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.yUp = + deltaY*cos(angle) + deltaZ*sin(angle)
        self.zUp = - deltaY*sin(angle) + deltaZ*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateViewX2ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xPosition - self.xTarget
        deltaY = self.yPosition - self.yTarget
        deltaZ = self.zPosition - self.zTarget
        self.yPosition = self.yTarget + deltaY*cos(angle) - deltaZ*sin(angle)
        self.zPosition = self.zTarget + deltaY*sin(angle) + deltaZ*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.yUp = + deltaY*cos(angle) - deltaZ*sin(angle)
        self.zUp = + deltaY*sin(angle) + deltaZ*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateViewY1ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xPosition - self.xTarget
        deltaY = self.yPosition - self.yTarget
        deltaZ = self.zPosition - self.zTarget
        self.xPosition = self.xTarget + deltaX*cos(angle) + deltaZ*sin(angle)
        self.zPosition = self.zTarget - deltaX*sin(angle) + deltaZ*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.xUp = + deltaX*cos(angle) + deltaZ*sin(angle)
        self.zUp = - deltaX*sin(angle) + deltaZ*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateViewY2ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xPosition - self.xTarget
        deltaY = self.yPosition - self.yTarget
        deltaZ = self.zPosition - self.zTarget
        self.xPosition = self.xTarget + deltaX*cos(angle) - deltaZ*sin(angle)
        self.zPosition = self.zTarget + deltaX*sin(angle) + deltaZ*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.xUp = + deltaX*cos(angle) - deltaZ*sin(angle)
        self.zUp = + deltaX*sin(angle) + deltaZ*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateViewZ1ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xPosition - self.xTarget
        deltaY = self.yPosition - self.yTarget
        deltaZ = self.zPosition - self.zTarget
        self.xPosition = self.xTarget + deltaX*cos(angle) + deltaY*sin(angle)
        self.yPosition = self.yTarget - deltaX*sin(angle) + deltaY*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.xUp = + deltaX*cos(angle) + deltaY*sin(angle)
        self.yUp = - deltaX*sin(angle) + deltaY*cos(angle)

        self.Redraw()
        event.Skip()

    def OnRotateViewZ2ButtonButton(self, event):
        angle = 15.0*3.1416/180.0

        deltaX = self.xPosition - self.xTarget
        deltaY = self.yPosition - self.yTarget
        deltaZ = self.zPosition - self.zTarget
        self.xPosition = self.xTarget + deltaX*cos(angle) - deltaY*sin(angle)
        self.yPosition = self.yTarget + deltaX*sin(angle) + deltaY*cos(angle)

        deltaX = self.xUp
        deltaY = self.yUp
        deltaZ = self.zUp
        self.xUp = + deltaX*cos(angle) - deltaY*sin(angle)
        self.yUp = + deltaX*sin(angle) + deltaY*cos(angle)

        self.Redraw()
        event.Skip()

    def OnContextItemMenuItems_del_fxMenu(self, event):
        # Get selected FX
        item = self.FXListCtrl.GetNextItem(-1, wxLIST_NEXT_ALL, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
        
        # If no FX selected, return now
        if item == -1:
            dlg = wxMessageDialog(self, 'No FX selected',
              'Delete FX', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            return
        else:
            #Confirm deleting
            dlg = wxMessageDialog(self, 'Really want to delete this FX?',
              'Delete FX', wxYES_NO | wxNO_DEFAULT | wxICON_QUESTION)
            try:
                selected = dlg.ShowModal()
            finally:
                dlg.Destroy()
            
            #Delete FX
            if selected == wxID_YES:
                self.FXListCtrl.DeleteItem(item)
                del self.FXparameters[item]
                
                self.FXListCtrl.SetItemState(item,
                  wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED,
                  wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
                self.SetCurrentFX()

        event.Skip()

    def OnContextItemMenuItems_move_upMenu(self, event):
        # Get selected FX
        item = self.FXListCtrl.GetNextItem(-1, wxLIST_NEXT_ALL, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
        
        # If no FX selected, return now
        if item == -1:
            dlg = wxMessageDialog(self, 'No FX selected',
              'Delete FX', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            return
        else:
            #Move FX
            if item > 0:
                temp = self.FXparameters[item]
                self.FXparameters[item] = self.FXparameters[item-1]
                self.FXparameters[item-1] = temp

                string = self.FXListCtrl.GetItemText(item)
                self.FXListCtrl.DeleteItem(item)
                self.FXListCtrl.InsertStringItem(item-1, string)

                #Update controls
                self.FXListCtrl.SetItemState(item-1,
                  wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED,
                  wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
                self.SetCurrentFX()

        event.Skip()

    def OnContextItemMenuItems_move_downMenu(self, event):
        # Get selected FX
        item = self.FXListCtrl.GetNextItem(-1, wxLIST_NEXT_ALL, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
        
        # If no FX selected, return now
        if item == -1:
            dlg = wxMessageDialog(self, 'No FX selected',
              'Delete FX', wxOK | wxICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            return
        else:
            #Move FX
            if item < self.FXListCtrl.GetItemCount()-1:
                temp = self.FXparameters[item]
                self.FXparameters[item] = self.FXparameters[item+1]
                self.FXparameters[item+1] = temp

                string = self.FXListCtrl.GetItemText(item)
                self.FXListCtrl.DeleteItem(item)
                self.FXListCtrl.InsertStringItem(item+1, string)

                #Update controls
                self.FXListCtrl.SetItemState(item+1,
                  wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED,
                  wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
                self.SetCurrentFX()

        event.Skip()

    def AddEffect(self, effectName):
        item = self.FXListCtrl.GetNextItem(-1, wxLIST_NEXT_ALL, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
        self.FXListCtrl.InsertStringItem(item+1, effectName)
        self.FXparameters.insert(item+1, initialValues[effectName][:])

        self.FXListCtrl.SetFocus()
        self.FXListCtrl.SetItemState(item, 0, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
        self.FXListCtrl.SetItemState(item+1,
            wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED,
            wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)

        self.SetCurrentFX()
        
    def OnBaseModelsSubMenuItems_cubeMenu(self, event):
        self.AddEffect("Cube")
        event.Skip()

    def OnBaseModelsSubMenuItems_cylinderMenu(self, event):
        self.AddEffect("Cylinder")
        event.Skip()

    def OnBaseModelsSubMenuItems_extrude_curveMenu(self, event):
        self.AddEffect("Extrude curve")
        event.Skip()

    def OnBaseModelsSubMenuItems_height_fieldMenu(self, event):
        self.AddEffect("Height field")
        event.Skip()

    def OnBaseModelsSubMenuItems_metaballMenu(self, event):
        self.AddEffect("Metaball")
        event.Skip()

    def OnBaseModelsSubMenuItems_octahedronMenu(self, event):
        self.AddEffect("Octahedron")
        event.Skip()

    def OnBaseModelsSubMenuItems_sphereMenu(self, event):
        self.AddEffect("Sphere")
        event.Skip()

    def OnBaseModelsSubMenuItems_starMenu(self, event):
        self.AddEffect("Star")
        event.Skip()

    def OnBaseModelsSubMenuItems_sweep_curveMenu(self, event):
        self.AddEffect("Sweep curve")
        event.Skip()

    def OnBaseModelsSubMenuItems_torusMenu(self, event):
        self.AddEffect("Torus")
        event.Skip()

    def OnDistortionsSubMenuItems_height_mapMenu(self, event):
        self.AddEffect("Height map")
        event.Skip()

    def OnDistortionsSubMenuItems_moveMenu(self, event):
        self.AddEffect("Move")
        event.Skip()

    def OnDistortionsSubMenuItems_noiseMenu(self, event):
        self.AddEffect("Noise")
        event.Skip()

    def OnDistortionsSubMenuItems_refineMenu(self, event):
        self.AddEffect("Refine")
        event.Skip()

    def OnDistortionsSubMenuItems_rotateMenu(self, event):
        self.AddEffect("Rotate")
        event.Skip()

    def OnDistortionsSubMenuItems_scaleMenu(self, event):
        self.AddEffect("Scale")
        event.Skip()

    def OnDistortionsSubMenuItems_spherizeMenu(self, event):
        self.AddEffect("Spherize")
        event.Skip()

    def OnDistortionsSubMenuItems_taperMenu(self, event):
        self.AddEffect("Taper")
        event.Skip()

    def OnDistortionsSubMenuItems_tessellateMenu(self, event):
        self.AddEffect("Tessellate")
        event.Skip()

    def OnDistortionsSubMenuItems_twistMenu(self, event):
        self.AddEffect("Twist")
        event.Skip()

    def OnTextureSubMenuItems_environment_mapMenu(self, event):
        self.AddEffect("Environment map")
        event.Skip()

    def OnTextureSubMenuItems_texture_mapMenu(self, event):
        self.AddEffect("Texture map")
        event.Skip()

    def Save(self, fileName):
        #Pickle model
        f = open(fileName + ".mdl", "wb")
        
        #Pickle number of FX
        pickle.dump(self.FXListCtrl.GetItemCount(), f)

        #Pickle every FX name
        for i in range(0, self.FXListCtrl.GetItemCount()):
            pickle.dump(self.FXListCtrl.GetItemText(i), f)

        #Pickle FX parameters
        pickle.dump(self.FXparameters, f)

        f.close()

    def Load(self, fileName):
        #Unpickle model
        f = open(fileName, "rb")

        #Unpickle number of FX
        numberOfFX = pickle.load(f)

        #Unpickle every FX name
        for i in range(0, numberOfFX):
            self.FXListCtrl.InsertStringItem(i, pickle.load(f))

        #Unpickle FX parameters
        self.FXparameters = pickle.load(f)

	#Select first FX
	if self.FXListCtrl.GetItemCount() > 0:
	    self.FXListCtrl.SetItemState(0, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED,
            wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)

        f.close()

    def Size(self, componentName):
        size = 0

        #Number of FX
        size += 1

        for i in range(0, self.FXListCtrl.GetItemCount()):
            FXName = self.FXListCtrl.GetItemText(i)

            #Active and FX type
            size += 1

            #Base models
            if FXName == "Cube":
                size += 0
            elif FXName == "Cylinder":
                size += 1
            elif FXName == "Extrude curve":
                curve = self.FXparameters[i][0]
                size += len(curve)+1
                size += 1
            elif FXName == "Height field":
                texture = self.FXparameters[i][0]
                size += len(texture)+1
                size += 1
            elif FXName == "Metaball":
                size += 4*4
            elif FXName == "Octahedron":
                size += 0
            elif FXName == "Sphere":
                size += 2
            elif FXName == "Star":
                size += 2*4 + 4
            elif FXName == "Sweep curve":
                curve = self.FXparameters[i][3]
                size += len(curve)+1
            elif FXName == "Torus":
                size += 2*4 + 2

            #Distortions
            elif FXName == "Height map":
                texture = self.FXparameters[i][2]
                size += len(texture)+1
                size += 1+1*4
            elif FXName == "Move":
                size += 3*4
            elif FXName == "Noise":
                size += 1+1*4
            elif FXName == "Refine":
                size += 0
            elif FXName == "Rotate":
                size += 1+1*4
            elif FXName == "Scale":
                size += 3*4
            elif FXName == "Spherize":
                size += 1*4
            elif FXName == "Taper":
                size += 1+1*4
            elif FXName == "Tessellate":
                size += 0
            elif FXName == "Twist":
                size += 1+1*4

            #Texture
            elif FXName == "Environment map":
                texture = self.FXparameters[i][0]
                size += len(texture)+1
            elif FXName == "Texture map":
                size += 1
                texture = self.FXparameters[i][1]
                size += len(texture)+1
                
        return size

    def SaveH(self, f, componentName):
        f.write("\t\t//Model name\n")
        f.write("\t\t")
        for i in componentName:
            f.write("'%c'," % (i,))
        f.write("0,\n\n")

        f.write("\t\t//Model size (24 network ordered bits)\n")
        modelSize = self.Size(componentName)
        f.write("\t\t%d, %d, %d\n\n" %
            (modelSize>>16, (modelSize>>8) & 0xFF, modelSize & 0xFF,))
        
        f.write("\t\t//Number of FX\n")
        f.write("\t\t%d,\n\n" % (self.FXListCtrl.GetItemCount(),))
        
        for i in range(0, self.FXListCtrl.GetItemCount()):
            f.write("\t\t//Active (1 bit) + FX type (7 bits)\n")

            #Active: 1 bit
            #FX type: 7 bits
            FXName = self.FXListCtrl.GetItemText(i)
            FXID = FXList.index(FXName)
            activePosition = parameters[FXName].index("Active")
            active = (self.FXparameters[i][activePosition] == "Yes")
            f.write("\t\t%d,\n" % (active*128 + FXID,))

            #Base models
            if FXName == "Cube":
                None

            elif FXName == "Cylinder":
                segments = int(self.FXparameters[i][0])

                f.write("\t\t//Segments\n")
                f.write("\t\t%d,\n" % (segments,))

            elif FXName == "Extrude curve":
                curve = self.FXparameters[i][0]

                f.write("\t\t//Curve\n")
                f.write("\t\t")
                for i in curve:
                    f.write("'%c'," % (i,))
                f.write("0,\n\n")

            elif FXName == "Height field":
                texture = self.FXparameters[i][0]
                facets = int(self.FXparameters[i][1])

                f.write("\t\t//Texture\n")
                f.write("\t\t")
                for i in texture:
                    f.write("'%c'," % (i,))
                f.write("0,\n\n")

                f.write("\t\t//Facets\n")
                f.write("\t\t%d,\n" % (facets,))

            elif FXName == "Metaball":
                positionX = float(self.FXparameters[i][0])
                positionY = float(self.FXparameters[i][1])
                positionZ = float(self.FXparameters[i][2])
                power = float(self.FXparameters[i][3])

                output = pack('f', positionX)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//X position\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', positionY)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Y position\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', positionZ)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Z position\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', power)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Power\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

            elif FXName == "Octahedron":
                None

            elif FXName == "Sphere":
                segments = int(self.FXparameters[i][0])
                rings = int(self.FXparameters[i][1])

                f.write("\t\t//Segments\n")
                f.write("\t\t%d,\n" % (segments,))

                f.write("\t\t//Rings\n")
                f.write("\t\t%d,\n" % (rings,))

            elif FXName == "Star":
                horizontalTips = int(self.FXparameters[i][0])
                verticalTips = int(self.FXparameters[i][1])
                minRadius = float(self.FXparameters[i][2])
                maxRadius = float(self.FXparameters[i][3])
                segments = int(self.FXparameters[i][4])
                rings = int(self.FXparameters[i][5])

                f.write("\t\t//Horizontal tips\n")
                f.write("\t\t%d,\n" % (horizontalTips,))

                f.write("\t\t//Vertical tips\n")
                f.write("\t\t%d,\n" % (verticalTips,))

                output = pack('f', minRadius)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Minimum radius\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', maxRadius)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Maximum radius\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                f.write("\t\t//Segments\n")
                f.write("\t\t%d,\n" % (segments,))

                f.write("\t\t//Rings\n")
                f.write("\t\t%d,\n" % (rings,))

            elif FXName == "Sweep curve":
                curve = self.FXparameters[i][0]

                f.write("\t\t//Curve\n")
                f.write("\t\t")
                for i in curve:
                    f.write("'%c'," % (i,))
                f.write("0,\n\n")

            elif FXName == "Torus":
                radius1 = float(self.FXparameters[i][0])
                radius2 = float(self.FXparameters[i][1])
                segments = int(self.FXparameters[i][2])
                rings = int(self.FXparameters[i][3])

                output = pack('f', radius1)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Radius 1\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', radius2)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Radius 2\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                f.write("\t\t//Segments\n")
                f.write("\t\t%d,\n" % (segments,))

                f.write("\t\t//Rings\n")
                f.write("\t\t%d,\n" % (rings,))

            #Distortions
            elif FXName == "Height map":
                type = typeChoices.index(self.FXparameters[i][0])
                value = float(self.FXparameters[i][1])
                texture = self.FXparameters[i][2]

                f.write("\t\t//Type (2 bits)\n")
                f.write("\t\t%d,\n" % (type,))

                output = pack('f', value)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Value\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                f.write("\t\t//Texture\n")
                f.write("\t\t")
                for i in texture:
                    f.write("'%c'," % (i,))
                f.write("0,\n\n")

            elif FXName == "Move":
                x = float(self.FXparameters[i][0])
                y = float(self.FXparameters[i][1])
                z = float(self.FXparameters[i][2])

                output = pack('f', x)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//X\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', y)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Y\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', z)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Z\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

            elif FXName == "Noise":
                value = float(self.FXparameters[i][0])
                seed = int(self.FXparameters[i][1])

                output = pack('f', value)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Value\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                f.write("\t\t//Seed\n")
                f.write("\t\t%d,\n" % (seed,))

            elif FXName == "Refine":
                None

            elif FXName == "Rotate":
                direction = directionChoices.index(self.FXparameters[i][0])
                value = float(self.FXparameters[i][1])

                f.write("\t\t//Direction (2 bits)\n")
                f.write("\t\t%d,\n" % (direction,))

                output = pack('f', value)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Value\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

            elif FXName == "Scale":
                x = float(self.FXparameters[i][0])
                y = float(self.FXparameters[i][1])
                z = float(self.FXparameters[i][2])

                output = pack('f', x)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//X\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', y)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Y\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

                output = pack('f', z)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Z\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

            elif FXName == "Spherize":
                value = float(self.FXparameters[i][0])

                output = pack('f', value)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Value\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

            elif FXName == "Taper":
                direction = directionChoices.index(self.FXparameters[i][0])
                value = float(self.FXparameters[i][1])

                f.write("\t\t//Direction (2 bits)\n")
                f.write("\t\t%d,\n" % (direction,))

                output = pack('f', value)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Value\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

            elif FXName == "Tessellate":
                None

            elif FXName == "Twist":
                direction = directionChoices.index(self.FXparameters[i][0])
                value = float(self.FXparameters[i][1])

                f.write("\t\t//Direction (2 bits)\n")
                f.write("\t\t%d,\n" % (direction,))

                output = pack('f', value)
                (a,b,c,d,) = unpack('BBBB', output)
                f.write("\t\t//Value\n")
                f.write("\t\t%d,%d,%d,%d,\n" % (a,b,c,d,))

            #Texture
            elif FXName == "Environment map":
                texture = self.FXparameters[i][0]

                f.write("\t\t//Texture\n")
                f.write("\t\t")
                for i in texture:
                    f.write("'%c'," % (i,))
                f.write("0,\n\n")

            elif FXName == "Texture map":
                type = typeChoices.index(self.FXparameters[i][0])
                texture = self.FXparameters[i][1]

                f.write("\t\t//Type (2 bits)\n")
                f.write("\t\t%d,\n" % (type,))

                f.write("\t\t//Texture\n")
                f.write("\t\t")
                for i in texture:
                    f.write("'%c'," % (i,))
                f.write("0,\n\n")

            f.write("\n")

    def GetData(self, componentName):
        # Store model name
        output = componentName
        output += pack('B', 0)
        
        # Store model size (24 bits network ordered)
        totalSize = self.Size(componentName)
        output += pack('B', totalSize>>16)
        output += pack('B', (totalSize>>8) & 0xFF)
        output += pack('B', totalSize & 0xFF)
        
        # Store number of FX
        output += pack('B', self.FXListCtrl.GetItemCount())

        # Store FX data
        for i in range(0, self.FXListCtrl.GetItemCount()):
            # Active: 1 bit
            # FX type: 7 bits
            FXName = self.FXListCtrl.GetItemText(i)
            FXID = FXList.index(FXName)
            activePosition = parameters[FXName].index("Active")
            active = (self.FXparameters[i][activePosition] == "Yes")
            output += pack('B', active*128 + FXID)

            #Base models
            if FXName == "Cube":
                None

            elif FXName == "Cylinder":
                segments = int(self.FXparameters[i][0])

                output += pack('B', segments)

            elif FXName == "Extrude curve":
                curve = self.FXparameters[i][0]

                output += curve
                output += pack('B', 0)

            elif FXName == "Height field":
                texture = self.FXparameters[i][0]
                facets = int(self.FXparameters[i][1])

                output += texture
                output += pack('B', 0)
                output += pack('B', facets)

            elif FXName == "Metaball":
                positionX = float(self.FXparameters[i][0])
                positionY = float(self.FXparameters[i][1])
                positionZ = float(self.FXparameters[i][2])
                power = float(self.FXparameters[i][3])

                output += pack('f', positionX)
                output += pack('f', positionY)
                output += pack('f', positionZ)
                output += pack('f', power)

            elif FXName == "Octahedron":
                None

            elif FXName == "Sphere":
                segments = int(self.FXparameters[i][0])
                rings = int(self.FXparameters[i][1])

                output += pack('B', segments)
                output += pack('B', rings)

            elif FXName == "Star":
                horizontalTips = int(self.FXparameters[i][0])
                verticalTips = int(self.FXparameters[i][1])
                minRadius = float(self.FXparameters[i][2])
                maxRadius = float(self.FXparameters[i][3])
                segments = int(self.FXparameters[i][4])
                rings = int(self.FXparameters[i][5])

                output += pack('B', horizontalTips)
                output += pack('B', verticalTips)
                output += pack('f', minRadius)
                output += pack('f', maxRadius)
                output += pack('B', segments)
                output += pack('B', rings)

            elif FXName == "Sweep curve":
                curve = self.FXparameters[i][0]

                output += curve

            elif FXName == "Torus":
                radius1 = float(self.FXparameters[i][0])
                radius2 = float(self.FXparameters[i][1])
                segments = int(self.FXparameters[i][2])
                rings = int(self.FXparameters[i][3])

                output += pack('f', radius1)
                output += pack('f', radius2)
                output += pack('B', segments)
                output += pack('B', rings)

            #Distortions
            elif FXName == "Height map":
                type = typeChoices.index(self.FXparameters[i][0])
                value = float(self.FXparameters[i][1])
                texture = self.FXparameters[i][2]

                output += pack('B', type)
                output += pack('f', value)
                output += texture
                output += pack('B', 0)

            elif FXName == "Move":
                x = float(self.FXparameters[i][0])
                y = float(self.FXparameters[i][1])
                z = float(self.FXparameters[i][2])

                output += pack('f', x)
                output += pack('f', y)
                output += pack('f', z)

            elif FXName == "Noise":
                value = float(self.FXparameters[i][0])
                seed = int(self.FXparameters[i][1])

                output += pack('f', value)
                output += pack('B', seed)

            elif FXName == "Refine":
                None

            elif FXName == "Rotate":
                direction = directionChoices.index(self.FXparameters[i][0])
                value = float(self.FXparameters[i][1])

                output += pack('B', direction)
                output += pack('f', value)

            elif FXName == "Scale":
                x = float(self.FXparameters[i][0])
                y = float(self.FXparameters[i][1])
                z = float(self.FXparameters[i][2])

                output += pack('f', x)
                output += pack('f', y)
                output += pack('f', z)

            elif FXName == "Spherize":
                value = float(self.FXparameters[i][0])

                output += pack('f', value)

            elif FXName == "Taper":
                direction = directionChoices.index(self.FXparameters[i][0])
                value = float(self.FXparameters[i][1])

                output += pack('B', direction)
                output += pack('f', value)

            elif FXName == "Tessellate":
                None

            elif FXName == "Twist":
                direction = directionChoices.index(self.FXparameters[i][0])
                value = float(self.FXparameters[i][1])

                output += pack('B', direction)
                output += pack('f', value)

            #Texture
            elif FXName == "Environment map":
                texture = self.FXparameters[i][0]

                output += texture
                output += pack('B', 0)

            elif FXName == "Texture map":
                type = typeChoices.index(self.FXparameters[i][0])
                texture = self.FXparameters[i][1]

                output += pack('B', type)
                output += texture
                output += pack('B', 0)

        return output
