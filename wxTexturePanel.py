#Boa:FramePanel:wxTexturePanel

from wxPython.wx import *
#from wxPython.gizmos import *
from wxPython.grid import *
from struct import *
from cStringIO import StringIO
import Image
import pickle

import wxTiledDialog

[wxID_WXTEXTUREPANEL, wxID_WXTEXTUREPANELFXLISTCTRL, 
 wxID_WXTEXTUREPANELFXSPLITTER, wxID_WXTEXTUREPANELGRIDFXPROPERTIES, 
 wxID_WXTEXTUREPANELPANELTEXTURES, wxID_WXTEXTUREPANELTEXTURESPLITTER, 
 wxID_WXTEXTUREPANELWINDOWTEXTURE0, wxID_WXTEXTUREPANELWINDOWTEXTURE1, 
 wxID_WXTEXTUREPANELWINDOWTEXTURE2, wxID_WXTEXTUREPANELWINDOWTEXTURE3, 
] = map(lambda _init_ctrls: wxNewId(), range(10))

[wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_ADD_FX, 
 wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_DEL_FX, 
 wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_MOVE_DOWN, 
 wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_MOVE_UP, 
] = map(lambda _init_coll_contextItemMenu_Items: wxNewId(), range(4))

[wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_BASE_TEXTURES, 
 wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_BLURS, 
 wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_COLORS, 
 wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_COMBOS, 
 wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_DISTORTIONS, 
 wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_LAYERS, 
] = map(lambda _init_coll_addFXSubMenu_Items: wxNewId(), range(6))

[wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_CHECKER, 
 wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_CURVE, 
 wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_FRACTAL, 
 wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_GLOW, 
 wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_NOISE, 
 wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_PICTURE, 
 wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_SINUS, 
] = map(lambda _init_coll_baseTexturesSubMenu_Items: wxNewId(), range(7))

[wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_FLIP, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_GLASS, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_MOVE, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_PIXELLATE, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_RANDOMIZE, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_ROTATE, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_SCALE, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_SPHERE_MAPPING, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_TILE, 
 wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_TWIRL, 
] = map(lambda _init_coll_distortionsSubMenu_Items: wxNewId(), range(10))

[wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BRIGHTNESS, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BUMP, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BUMP_MORE, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_CONTRAST, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_EDGE_DETECT, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_EMBOSS, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_GRAYSCALE, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_INVERSE, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_POSTERIZE, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_SHARPEN, 
 wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_THRESHOLD, 
] = map(lambda _init_coll_colorsSubMenu_Items: wxNewId(), range(11))

[wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_BLUR, 
 wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_HORIZONTAL_BLUR, 
 wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_VERTICAL_BLUR, 
 wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_BLUR, 
 wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_HORIZONTAL_BLUR, 
 wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_VERTICAL_BLUR, 
 wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_LINE_BLUR, 
] = map(lambda _init_coll_blursSubMenu_Items: wxNewId(), range(7))

[wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_ADD, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_COPY, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_DIRECTIONAL_BLUR, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_ENVIRONMENT, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_MIX, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_MUL, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_RANDOM_DUMP, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_SHADE, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_SUB, 
 wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_XOR, 
] = map(lambda _init_coll_layersSubMenu_Items: wxNewId(), range(10))

[wxID_WXTEXTUREPANELCONTEXTBACKGROUNDMENUITEMS_ADD_FX] = map(lambda _init_coll_contextBackgroundMenu_Items: wxNewId(), range(1))

[wxID_WXTEXTUREPANELCOMBOSSUBMENUITEMS_TEXTURE_CURVE] = map(lambda _init_coll_combosSubMenu_Items: wxNewId(), range(1))

# FX and parameters
parameters = {
    "Checker" :
        ["Destination","Width","Height","Gradient","Active"],
    "Curve" :
        ["Destination","Width","Height","Curve","Active"],
    "Fractal" :
        ["Destination","Width","Height","Gradient","Noise","Seed","Active"],
    "Glow" :
        ["Destination","Width","Height","Gradient","Radius","Active"],
    "Noise" :
        ["Destination","Width","Height","Gradient","Seed","Active"],
    "Picture" :
        ["Destination","Width","Height","Data","Active"],
    "Sinus" :
        ["Destination","Width","Height","Gradient","TurbulenceX1","TurbulenceX2","TurbulenceY1","TurbulenceY2","Phase1","Phase2","Active"],

    "Flip" :
        ["Destination","Horizontal","Vertical","Active"],
    "Glass" :
        ["Destination","Turbulence X1","Turbulence X2","Turbulence Y1","Turbulence Y2","Phase 1","Phase 2","Intensity","Active"],
    "Move" :
        ["Destination","Direction","Value","Active"],
    "Pixellate" :
        ["Destination","Value","Active"],
    "Randomize" :
        ["Destination","Value","Seed","Active"],
    "Rotate" :
        ["Destination","Value","Active"],
    "Scale" :
        ["Destination","New width","New height","Active"],
    "Sphere mapping" :
        ["Destination","Active"],
    "Tile" :
        ["Destination","Horizontal tile","Vertical tile","Active"],
    "Twirl" :
        ["Destination","Value","Active"],

    "Brightness" :
        ["Destination","Value","Active"],
    "Bump" :
        ["Destination","Active"],
    "Bump more" :
        ["Destination","Active"],
    "Contrast" :
        ["Destination","Value","Active"],
    "Edge detect" :
        ["Destination","Active"],
    "Emboss" :
        ["Destination","Direction","Active"],
    "Grayscale" :
        ["Destination","Active"],
    "Inverse" :
        ["Destination","Active"],
    "Posterize" :
        ["Destination","Levels","Active"],
    "Sharpen" :
        ["Destination","Value","Active"],
    "Threshold" :
        ["Destination","Value","Active"],

    "Fast blur" :
        ["Destination","Radius","Active"],
    "Fast horizontal blur" :
        ["Destination","Radius","Active"],
    "Fast vertical blur" :
        ["Destination","Radius","Active"],
    "Gaussian blur" :
        ["Destination","Radius","Active"],
    "Gaussian horizontal blur" :
        ["Destination","Radius","Active"],
    "Gaussian vertical blur" :
        ["Destination","Radius","Active"],
    "Line blur" :
        ["Destination","Orientation","Radius","Active"],

    "Add" :
        ["Destination","Source","Active"],
    "Copy" :
        ["Destination","Source","Active"],
    "Directional blur" :
        ["Destination","Source","Value","Active"],
    "Environment" :
        ["Destination","Source","Value","Active"],
    "Mix" :
        ["Destination","Source","Value","Active"],
    "Mul" :
        ["Destination","Source","Active"],
    "Random dump" :
        ["Destination","Source","Number","Seed","Active"],
    "Shade" :
        ["Destination","Source","Active"],
    "Sub" :
        ["Destination","Source","Active"],
    "Xor" :
        ["Destination","Source","Active"],

    "Texture curve" :
        ["Destination","Width","Height","Curve","Texture","Mask","Edge width","Active"]
}

# FX and initial values
initialValues = {
    "Checker" :
        ["Layer 0","256","256","","Yes"],
    "Curve" :
        ["Layer 0","256","256","","Yes"],
    "Fractal" :
        ["Layer 0","256","256","","1","1","Yes"],
    "Glow" :
        ["Layer 0","256","256","","1","Yes"],
    "Noise" :
        ["Layer 0","256","256","","1","Yes"],
    "Picture" :
        ["Layer 0","256","256","","Yes"],
    "Sinus" :
        ["Layer 0","256","256","","1","1","1","1","1","1","Yes"],

    "Flip" :
        ["Layer 0","Yes","Yes","Yes"],
    "Glass" :
        ["Layer 0","1","1","1","1","1","1","1","Yes"],
    "Move" :
        ["Layer 0","Up","1","Yes"],
    "Pixellate" :
        ["Layer 0","8","Yes"],
    "Randomize" :
        ["Layer 0","1","1","Yes"],
    "Rotate" :
        ["Layer 0","1","Yes"],
    "Scale" :
        ["Layer 0","256","256","Yes","Yes"],
    "Sphere mapping" :
        ["Layer 0","Yes"],
    "Tile" :
        ["Layer 0","2","2","Yes"],
    "Twirl" :
        ["Layer 0","128","Yes"],

    "Brightness" :
        ["Layer 0","128","Yes"],
    "Bump" :
        ["Layer 0","Yes"],
    "Bump more" :
        ["Layer 0","Yes"],
    "Contrast" :
        ["Layer 0","128","Yes"],
    "Edge detect" :
        ["Layer 0","Yes"],
    "Emboss" :
        ["Layer 0","Up","Yes"],
    "Grayscale" :
        ["Layer 0","Yes"],
    "Inverse" :
        ["Layer 0","Yes"],
    "Posterize" :
        ["Layer 0","4","Yes"],
    "Sharpen" :
        ["Layer 0","1","Yes"],
    "Threshold" :
        ["Layer 0","128","Yes"],

    "Fast blur" :
        ["Layer 0","1","Yes"],
    "Fast horizontal blur" :
        ["Layer 0","1","Yes"],
    "Fast vertical blur" :
        ["Layer 0","1","Yes"],
    "Gaussian blur" :
        ["Layer 0","1","Yes"],
    "Gaussian horizontal blur" :
        ["Layer 0","1","Yes"],
    "Gaussian vertical blur" :
        ["Layer 0","1","Yes"],
    "Line blur" :
        ["Layer 0","32","1","Yes"],

    "Add" :
        ["Layer 0","Layer 0","Yes"],
    "Copy" :
        ["Layer 0","Layer 0","Yes"],
    "Directional blur" :
        ["Layer 0","Layer 0","1","Yes"],
    "Environment" :
        ["Layer 0","Layer 0","1","Yes"],
    "Mix" :
        ["Layer 0","Layer 0","128","Yes"],
    "Mul" :
        ["Layer 0","Layer 0","Yes"],
    "Random dump" :
        ["Layer 0","Layer 0","1","1","Yes"],
    "Shade" :
        ["Layer 0","Layer 0","Yes"],
    "Sub" :
        ["Layer 0","Layer 0","Yes"],
    "Xor" :
        ["Layer 0","Layer 0","Yes"],

    "Texture curve" :
        ["Layer 1","256","256","","Layer 0","Layer 2","4","Yes"]
}

# FX list
FXList = [
    #Base textures
    "Checker","Curve","Fractal","Glow","Noise","Picture","Sinus",
    #Distortions
    "Flip","Glass","Move","Pixellate","Randomize","Rotate","Scale","Sphere mapping","Tile","Twirl",
    #Colors
    "Brightness","Bump","Bump more","Contrast","Edge detect","Emboss","Grayscale","Inverse","Posterize","Sharpen","Threshold",
    #Blurs
    "Fast blur","Fast horizontal blur","Fast vertical blur","Gaussian blur","Gaussian horizontal blur","Gaussian vertical blur","Line blur",
    #Layers
    "Add","Copy","Directional blur","Environment","Mix","Mul","Random dump","Shade","Sub","Xor",
    #Combos
    "Texture curve"
]

layerChoices = ["Layer 0", "Layer 1", "Layer 2", "Layer 3"]
sizeChoices = ["8", "16", "32", "64", "128", "256", "512", "1024"]
directionChoices = ["Up left", "Up", "Up right", "Left", "Right", "Down left", "Down", "Down right"]
booleanChoices = ["Yes", "No"]

# ##################################################################### #

class wxTexturePanel(wxPanel):
    def _init_coll_baseTexturesSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_CHECKER,
              item='Checker', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_CURVE,
              item='Curve', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_FRACTAL,
              item='Fractal', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_GLOW, item='Glow',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_NOISE,
              item='Noise', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_PICTURE,
              item='Picture', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_SINUS,
              item='Sinus', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_CHECKER,
              self.OnBaseTexturesSubMenuItems_checkerMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_CURVE,
              self.OnBaseTexturesSubMenuItems_curveMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_FRACTAL,
              self.OnBaseTexturesSubMenuItems_fractalMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_GLOW,
              self.OnBaseTexturesSubMenuItems_glowMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_NOISE,
              self.OnBaseTexturesSubMenuItems_noiseMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_PICTURE,
              self.OnBaseTexturesSubMenuItems_pictureMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBASETEXTURESSUBMENUITEMS_SINUS,
              self.OnBaseTexturesSubMenuItems_sinusMenu)

    def _init_coll_blursSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_BLUR,
              item='Fast blur', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_HORIZONTAL_BLUR,
              item='Fast horizontal blur', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_VERTICAL_BLUR,
              item='Fast vertical blur', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_BLUR,
              item='Gaussian blur', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_HORIZONTAL_BLUR,
              item='Gaussian horizontal blur', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_VERTICAL_BLUR,
              item='Gaussian vertical blur', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_LINE_BLUR,
              item='Line blur', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_BLUR,
              self.OnBlursSubMenuItems_fast_blurMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_HORIZONTAL_BLUR,
              self.OnBlursSubMenuItems_fast_horizontal_blurMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_FAST_VERTICAL_BLUR,
              self.OnBlursSubMenuItems_fast_vertical_blurMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_BLUR,
              self.OnBlursSubMenuItems_gaussian_blurMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_HORIZONTAL_BLUR,
              self.OnBlursSubMenuItems_gaussian_horizontal_blurMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_GAUSSIAN_VERTICAL_BLUR,
              self.OnBlursSubMenuItems_gaussian_vertical_blurMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELBLURSSUBMENUITEMS_LINE_BLUR,
              self.OnBlursSubMenuItems_line_blurMenu)

    def _init_coll_layersSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_ADD, item='Add',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_COPY, item='Copy',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_DIRECTIONAL_BLUR,
              item='Directional blur', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_ENVIRONMENT,
              item='Environment', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_MIX, item='Mix',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_MUL, item='Mul',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_RANDOM_DUMP,
              item='Random dump', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_SHADE, item='Shade',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_SUB, item='Sub',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_XOR, item='Xor',
              kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_ADD,
              self.OnLayersSubMenuItems_addMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_COPY,
              self.OnLayersSubMenuItems_copyMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_DIRECTIONAL_BLUR,
              self.OnLayersSubMenuItems_directional_blurMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_ENVIRONMENT,
              self.OnLayersSubMenuItems_environmentMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_MIX,
              self.OnLayersSubMenuItems_mixMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_MUL,
              self.OnLayersSubMenuItems_mulMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_RANDOM_DUMP,
              self.OnLayersSubMenuItems_random_dumpMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_SHADE,
              self.OnLayersSubMenuItems_shadeMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_SUB,
              self.OnLayersSubMenuItems_subMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELLAYERSSUBMENUITEMS_XOR,
              self.OnLayersSubMenuItems_xorMenu)

    def _init_coll_colorsSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BRIGHTNESS,
              item='Brightness', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BUMP, item='Bump',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BUMP_MORE,
              item='Bump more', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_CONTRAST,
              item='Contrast', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_EDGE_DETECT,
              item='Edge detect', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_EMBOSS, item='Emboss',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_GRAYSCALE,
              item='Grayscale', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_INVERSE, item='Inverse',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_POSTERIZE,
              item='Posterize', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_SHARPEN, item='Sharpen',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_THRESHOLD,
              item='Threshold', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BRIGHTNESS,
              self.OnColorsSubMenuItems_brightnessMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BUMP,
              self.OnColorsSubMenuItems_bumpMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_BUMP_MORE,
              self.OnColorsSubMenuItems_bump_moreMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_CONTRAST,
              self.OnColorsSubMenuItems_contrastMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_EDGE_DETECT,
              self.OnColorsSubMenuItems_edge_detectMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_EMBOSS,
              self.OnColorsSubMenuItems_embossMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_GRAYSCALE,
              self.OnColorsSubMenuItems_grayscaleMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_INVERSE,
              self.OnColorsSubMenuItems_inverseMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_POSTERIZE,
              self.OnColorsSubMenuItems_posterizeMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_SHARPEN,
              self.OnColorsSubMenuItems_sharpenMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOLORSSUBMENUITEMS_THRESHOLD,
              self.OnColorsSubMenuItems_thresholdMenu)

    def _init_coll_distortionsSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_FLIP, item='Flip',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_GLASS, item='Glass',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_MOVE, item='Move',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_PIXELLATE,
              item='Pixellate', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_RANDOMIZE,
              item='Randomize', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_ROTATE,
              item='Rotate', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_SCALE, item='Scale',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_SPHERE_MAPPING,
              item='Sphere mapping', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_TILE, item='Tile',
              kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_TWIRL, item='Twirl',
              kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_FLIP,
              self.OnDistortionsSubMenuItems_flipMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_GLASS,
              self.OnDistortionsSubMenuItems_glassMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_MOVE,
              self.OnDistortionsSubMenuItems_moveMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_PIXELLATE,
              self.OnDistortionsSubMenuItems_pixellateMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_RANDOMIZE,
              self.OnDistortionsSubMenuItems_randomizeMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_ROTATE,
              self.OnDistortionsSubMenuItems_rotateMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_SCALE,
              self.OnDistortionsSubMenuItems_scaleMenu)
        EVT_MENU(self,
              wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_SPHERE_MAPPING,
              self.OnDistortionsSubMenuItems_sphere_mappingMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_TILE,
              self.OnDistortionsSubMenuItems_tileMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELDISTORTIONSSUBMENUITEMS_TWIRL,
              self.OnDistortionsSubMenuItems_twirlMenu)

    def _init_coll_addFXSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.AppendMenu(helpString='',
              id=wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_BASE_TEXTURES,
              item='Base Textures', subMenu=self.baseTexturesSubMenu)
        parent.AppendMenu(helpString='',
              id=wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_DISTORTIONS,
              item='Distortions', subMenu=self.distortionsSubMenu)
        parent.AppendMenu(helpString='',
              id=wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_COLORS, item='Colors',
              subMenu=self.colorsSubMenu)
        parent.AppendMenu(helpString='',
              id=wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_BLURS, item='Blurs',
              subMenu=self.blursSubMenu)
        parent.AppendMenu(helpString='',
              id=wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_LAYERS, item='Layers',
              subMenu=self.layersSubMenu)
        parent.AppendMenu(helpString='',
              id=wxID_WXTEXTUREPANELADDFXSUBMENUITEMS_COMBOS, item='Combos',
              subMenu=self.combosSubMenu)

    def _init_coll_contextItemMenu_Items(self, parent):
        # generated method, don't edit

        parent.AppendMenu(helpString='',
              id=wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_ADD_FX, item='Add FX',
              subMenu=self.addFXSubMenu)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_DEL_FX,
              item='Delete FX', kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_MOVE_UP,
              item='Move up', kind=wxITEM_NORMAL)
        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_MOVE_DOWN,
              item='Move down', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_DEL_FX,
              self.OnContextItemMenuItems_del_fxMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_MOVE_UP,
              self.OnContextItemMenuItems_move_upMenu)
        EVT_MENU(self, wxID_WXTEXTUREPANELCONTEXTITEMMENUITEMS_MOVE_DOWN,
              self.OnContextItemMenuItems_move_downMenu)

    def _init_coll_combosSubMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='',
              id=wxID_WXTEXTUREPANELCOMBOSSUBMENUITEMS_TEXTURE_CURVE,
              item='Texture curve', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_WXTEXTUREPANELCOMBOSSUBMENUITEMS_TEXTURE_CURVE,
              self.OnCombosSubMenuItems_texture_curveMenu)

    def _init_coll_FXListCtrl_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wxLIST_FORMAT_LEFT, heading='FX List',
              width=150)

    def _init_utils(self):
        # generated method, don't edit
        self.contextItemMenu = wxMenu(title='')

        self.addFXSubMenu = wxMenu(title='')

        self.baseTexturesSubMenu = wxMenu(title='')

        self.distortionsSubMenu = wxMenu(title='')

        self.colorsSubMenu = wxMenu(title='')

        self.blursSubMenu = wxMenu(title='')

        self.layersSubMenu = wxMenu(title='')

        self.combosSubMenu = wxMenu(title='')

        self._init_coll_contextItemMenu_Items(self.contextItemMenu)
        self._init_coll_addFXSubMenu_Items(self.addFXSubMenu)
        self._init_coll_baseTexturesSubMenu_Items(self.baseTexturesSubMenu)
        self._init_coll_distortionsSubMenu_Items(self.distortionsSubMenu)
        self._init_coll_colorsSubMenu_Items(self.colorsSubMenu)
        self._init_coll_blursSubMenu_Items(self.blursSubMenu)
        self._init_coll_layersSubMenu_Items(self.layersSubMenu)
        self._init_coll_combosSubMenu_Items(self.combosSubMenu)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxPanel.__init__(self, id=wxID_WXTEXTUREPANEL, name='wxTexturePanel',
              parent=prnt, pos=wxPoint(287, 267), size=wxSize(716, 439),
              style=0)
        self._init_utils()
        self.SetClientSize(wxSize(716, 439))
        self.SetToolTipString('Texture Panel')
        EVT_SIZE(self, self.OnWxTexturePanelSize)

        self.textureSplitter = wxSplitterWindow(id=wxID_WXTEXTUREPANELTEXTURESPLITTER,
              name='textureSplitter', parent=self, point=wxPoint(0, 0),
              size=wxSize(722, 438), style=wxSP_3D)
        self.textureSplitter.SetToolTipString('Texture Splitter')
        self.textureSplitter.SetMinimumPaneSize(200)

        self.FXSplitter = wxSplitterWindow(id=wxID_WXTEXTUREPANELFXSPLITTER,
              name='FXSplitter', parent=self.textureSplitter, point=wxPoint(2,
              2), size=wxSize(100, 314), style=wxSP_3D)
        self.FXSplitter.SetToolTipString('FX Splitter')
        self.FXSplitter.SetMinimumPaneSize(250)

        self.FXListCtrl = wxListCtrl(id=wxID_WXTEXTUREPANELFXLISTCTRL,
              name='FXListCtrl', parent=self.FXSplitter, pos=wxPoint(2, 2),
              size=wxSize(196, 180), style=wxLC_SINGLE_SEL | wxLC_REPORT)
        self.FXListCtrl.SetToolTipString('FXListCtrl')
        self._init_coll_FXListCtrl_Columns(self.FXListCtrl)
        EVT_RIGHT_DOWN(self.FXListCtrl, self.OnFXListCtrlRightDown)
        EVT_LIST_ITEM_SELECTED(self.FXListCtrl, wxID_WXTEXTUREPANELFXLISTCTRL,
              self.OnFXListCtrlListItemSelected)
        EVT_LIST_ITEM_DESELECTED(self.FXListCtrl, wxID_WXTEXTUREPANELFXLISTCTRL,
              self.OnFXListCtrlListItemDeselected)

        self.gridFXProperties = wxGrid(id=wxID_WXTEXTUREPANELGRIDFXPROPERTIES,
              name='gridFXProperties', parent=self.FXSplitter, pos=wxPoint(2,
              189), size=wxSize(196, 243), style=0)
        self.gridFXProperties.SetColLabelSize(0)
        self.gridFXProperties.SetRowLabelSize(100)
        self.gridFXProperties.EnableGridLines(True)
        self.gridFXProperties.SetRowMinimalAcceptableHeight(100)
        EVT_GRID_CELL_CHANGE(self.gridFXProperties,
              self.OnGridFXPropertiesGridCellChange)
        EVT_GRID_CELL_LEFT_CLICK(self.gridFXProperties,
              self.OnGridFXPropertiesGridCellLeftClick)
        self.FXSplitter.SplitHorizontally(self.FXListCtrl,
              self.gridFXProperties, 252)

        self.panelTextures = wxPanel(id=wxID_WXTEXTUREPANELPANELTEXTURES,
              name='panelTextures', parent=self.textureSplitter,
              pos=wxPoint(209, 2), size=wxSize(511, 434), style=0)
        self.panelTextures.SetToolTipString('Textures panel')
        EVT_SIZE(self.panelTextures, self.OnPanelTexturesSize)
        self.textureSplitter.SplitVertically(self.FXSplitter,
              self.panelTextures, 200)

        self.windowTexture0 = wxWindow(id=wxID_WXTEXTUREPANELWINDOWTEXTURE0,
              name='windowTexture0', parent=self.panelTextures, pos=wxPoint(8,
              8), size=wxSize(144, 144), style=wxSIMPLE_BORDER)
        EVT_LEFT_DOWN(self.windowTexture0, self.OnWindowTexture0LeftDown)

        self.windowTexture1 = wxWindow(id=wxID_WXTEXTUREPANELWINDOWTEXTURE1,
              name='windowTexture1', parent=self.panelTextures, pos=wxPoint(160,
              8), size=wxSize(144, 144), style=wxSIMPLE_BORDER)
        EVT_LEFT_DOWN(self.windowTexture1, self.OnWindowTexture1LeftDown)

        self.windowTexture2 = wxWindow(id=wxID_WXTEXTUREPANELWINDOWTEXTURE2,
              name='windowTexture2', parent=self.panelTextures, pos=wxPoint(8,
              160), size=wxSize(144, 144), style=wxSIMPLE_BORDER)
        EVT_LEFT_DOWN(self.windowTexture2, self.OnWindowTexture2LeftDown)

        self.windowTexture3 = wxWindow(id=wxID_WXTEXTUREPANELWINDOWTEXTURE3,
              name='windowTexture3', parent=self.panelTextures, pos=wxPoint(160,
              160), size=wxSize(144, 144), style=wxSIMPLE_BORDER)
        EVT_LEFT_DOWN(self.windowTexture3, self.OnWindowTexture3LeftDown)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
        
        #Store reference to MainFrame to get gradients and curves list
        self.MainFrame = self.GetParent().GetParent().GetParent()

        #Init grid control
        self.gridFXProperties.CreateGrid(0,1)
        
        #Init FX parameters
        self.FXparameters = []
        
        #Init choices
        self.gradientChoices = []
        self.curveChoices = []
        
        #Init layers
        image0 = wxEmptyImage(1, 1)
        image0.SetRGB(0, 0, 0, 0, 0)
        size = self.windowTexture0.GetSize()
        bitmap0 = wxBitmapFromImage(image0.Scale(size.x, size.y))
        self.staticBitmap0 = wxStaticBitmap(self.windowTexture0, -1, bitmap0,
            wxPoint(0, 0), self.windowTexture0.GetSize())
        EVT_LEFT_DOWN(self.staticBitmap0, self.OnWindowTexture0LeftDown)

        image1 = wxEmptyImage(1, 1)
        image1.SetRGB(0, 0, 0, 0, 0)
        size = self.windowTexture1.GetSize()
        bitmap1 = wxBitmapFromImage(image1.Scale(size.x, size.y))
        self.staticBitmap1 = wxStaticBitmap(self.windowTexture1, -1, bitmap1,
            wxPoint(0, 0), self.windowTexture1.GetSize())
        EVT_LEFT_DOWN(self.staticBitmap1, self.OnWindowTexture1LeftDown)

        image2 = wxEmptyImage(1, 1)
        image2.SetRGB(0, 0, 0, 0, 0)
        size = self.windowTexture2.GetSize()
        bitmap2 = wxBitmapFromImage(image2.Scale(size.x, size.y))
        self.staticBitmap2 = wxStaticBitmap(self.windowTexture2, -1, bitmap2,
            wxPoint(0, 0), self.windowTexture2.GetSize())
        EVT_LEFT_DOWN(self.staticBitmap2, self.OnWindowTexture2LeftDown)

        image3 = wxEmptyImage(1, 1)
        image3.SetRGB(0, 0, 0, 0, 0)
        size = self.windowTexture3.GetSize()
        bitmap3 = wxBitmapFromImage(image3.Scale(size.x, size.y))
        self.staticBitmap3 = wxStaticBitmap(self.windowTexture3, -1, bitmap3,
            wxPoint(0, 0), self.windowTexture3.GetSize())
        EVT_LEFT_DOWN(self.staticBitmap3, self.OnWindowTexture3LeftDown)
        
    def OnWxTexturePanelSize(self, event):
        panelDC = wxClientDC(self)
        panelSize = panelDC.GetSize()
        self.textureSplitter.SetSize(panelSize)
        
        event.Skip()

    def OnPanelTexturesSize(self, event):
        texturesPanelDC = wxClientDC(self.panelTextures)
        size = texturesPanelDC.GetSize()
        
        #8 pixels between windows
        width = (size.GetWidth()-24) / 2
        height = (size.GetHeight()-24) / 2
        
        # Make it square
        if width < height:
            height = width
        else:
            width = height

        # Event pops up before windows exist, so exception must be caught
        try:
            self.windowTexture0.SetDimensions(8, 8, width, height)
            self.staticBitmap0.SetDimensions(0, 0, width, height)

            self.windowTexture1.SetDimensions(16+width, 8, width, height)
            self.staticBitmap1.SetDimensions(0, 0, width, height)

            self.windowTexture2.SetDimensions(8, 16+height, width, height)
            self.staticBitmap2.SetDimensions(0, 0, width, height)

            self.windowTexture3.SetDimensions(16+width, 16+height, width, height)
            self.staticBitmap3.SetDimensions(0, 0, width, height)

            self.Refresh()
        except:
            None
            
        event.Skip()

    def drawBlackLayer(self, window):
        textureDC = wxClientDC(window)
        size = textureDC.GetSize()

        textureDC.BeginDrawing()

        brush = wxBrush(wxColour(0,0,0), wxSOLID)
        textureDC.SetBrush(brush)

        textureDC.DrawRectangle(0, 0, size.GetWidth(), size.GetHeight())

        textureDC.EndDrawing()

    def PaintLayer(self, number):
        if number == 0:
            bitmap = self.staticBitmap0
        elif number == 1:
            bitmap = self.staticBitmap1
        elif number == 2:
            bitmap = self.staticBitmap2
        elif number == 3:
            bitmap = self.staticBitmap3

        # Get window size
        size = bitmap.GetSize()
        
        # Get current texture name
        pageNumber = self.MainFrame.componentsNotebook.GetSelection()
        if pageNumber == -1:
            return
        textureName = self.MainFrame.componentsNotebook.GetPageText(pageNumber)

        # Get image data
        width = self.MainFrame.generator.getTextureLayerWidth(textureName, number)
        height = self.MainFrame.generator.getTextureLayerHeight(textureName, number)

        # If no image yet created, draw a black image
        if width == -1 or height == -1 :
            self.drawBlackLayer(bitmap)
        else :
            str = self.MainFrame.generator.getTextureLayer(textureName, number, width*height*4)

            # Create image
            source = Image.frombuffer("RGBA", (width, height), str)
            image = apply(wxEmptyImage, source.size)
            image.SetData( source.convert("RGB").tostring() )

            # Scale and convert to a displayable bitmap
            jpg = wxBitmapFromImage(image.Scale(size.x, size.y).Mirror(False))

            #Show it
            bitmap.SetBitmap(jpg)

    def ShowTiledLayer(self, number):
        dlg = wxTiledDialog.wxTiledDialog(self)
        dlg.SetTitle("Tiled layer %d" % (number,))
        dlg.Centre()

        # Get current texture name
        pageNumber = self.MainFrame.componentsNotebook.GetSelection()
        textureName = self.MainFrame.componentsNotebook.GetPageText(pageNumber)

        # Get image data
        width = self.MainFrame.generator.getTextureLayerWidth(textureName, number)
        height = self.MainFrame.generator.getTextureLayerHeight(textureName, number)

        # If no image yet created, draw a black image
        if width == -1 or height == -1 :
            # Create black bitmap
            image = wxEmptyImage(1, 1)
            image.SetRGB(0, 0, 0, 0, 0)
            bitmap = wxBitmapFromImage(image.Scale(256, 256))
        else :
            str = self.MainFrame.generator.getTextureLayer(textureName, number, width*height*4)

            # Create image
            source = Image.frombuffer("RGBA", (width, height), str)
            image = apply(wxEmptyImage, source.size)
            image.SetData( source.convert("RGB").tostring() )

            # Scale and convert to a displayable bitmap
            bitmap = wxBitmapFromImage(image.Mirror(False))

        dlg.SetBitmap(bitmap)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
        
    def OnWindowTexture0LeftDown(self, event):
        self.ShowTiledLayer(0)
        event.Skip()

    def OnWindowTexture1LeftDown(self, event):
        self.ShowTiledLayer(1)
        event.Skip()

    def OnWindowTexture2LeftDown(self, event):
        self.ShowTiledLayer(2)
        event.Skip()

    def OnWindowTexture3LeftDown(self, event):
        self.ShowTiledLayer(3)
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
            if parametersNames[i] == "Destination":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(layerChoices))
            elif parametersNames[i] == "Source":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(layerChoices))
            elif parametersNames[i] == "Mask":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(layerChoices))
            elif parametersNames[i] == "Texture":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(layerChoices))
            elif parametersNames[i] == "Width":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(sizeChoices))
            elif parametersNames[i] == "Height":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(sizeChoices))
            elif parametersNames[i] == "New width":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(sizeChoices))
            elif parametersNames[i] == "New height":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(sizeChoices))
            elif parametersNames[i] == "Direction":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(directionChoices))
            elif parametersNames[i] == "Rotation":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(rotationChoices))
            elif parametersNames[i] == "Data":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellTextEditor())
            elif parametersNames[i] == "Gradient":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(self.gradientChoices))
            elif parametersNames[i] == "Curve":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(self.curveChoices))
            elif parametersNames[i] == "Active":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(booleanChoices))
            elif parametersNames[i] == "Horizontal":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(booleanChoices))
            elif parametersNames[i] == "Vertical":
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellChoiceEditor(booleanChoices))
            else:
                self.gridFXProperties.SetCellEditor(i, 0, wxGridCellNumberEditor(0, 255))

            #Set cell value
            self.gridFXProperties.SetCellValue(i, 0, self.FXparameters[item][i])

    def Redraw(self):
        # Repaint texture layers
        self.PaintLayer(0)
        self.PaintLayer(1)
        self.PaintLayer(2)
        self.PaintLayer(3)

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
        
    def OnBaseTexturesSubMenuItems_checkerMenu(self, event):
        self.AddEffect("Checker")
        event.Skip()

    def OnBaseTexturesSubMenuItems_curveMenu(self, event):
        self.AddEffect("Curve")
        event.Skip()

    def OnBaseTexturesSubMenuItems_fractalMenu(self, event):
        self.AddEffect("Fractal")
        event.Skip()

    def OnBaseTexturesSubMenuItems_glowMenu(self, event):
        self.AddEffect("Glow")
        event.Skip()

    def OnBaseTexturesSubMenuItems_noiseMenu(self, event):
        self.AddEffect("Noise")
        event.Skip()

    def OnBaseTexturesSubMenuItems_pictureMenu(self, event):
        dlg = wxFileDialog(self, "Choose an image file", ".", "", "*.*",
            wxOPEN | wxCHANGE_DIR)
        try:
            if dlg.ShowModal() == wxID_OK:
                filename = dlg.GetPath()
                
                # Open image
                image = wxImage(filename)
                
                sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
                if image.GetWidth() not in sizes:
                    dlg = wxMessageDialog(self, 'Width must be a power of 2',
                      'Size error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    return
                if image.GetHeight() not in sizes:
                    dlg = wxMessageDialog(self, 'Height must be a power of 2',
                      'Size error', wxOK | wxICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    return

                item = self.FXListCtrl.GetNextItem(-1, wxLIST_NEXT_ALL, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
                self.FXListCtrl.InsertStringItem(item+1, "Picture")
                self.FXparameters.insert(item+1, initialValues["Picture"][:])

                self.FXListCtrl.SetFocus()
                self.FXListCtrl.SetItemState(item, 0, wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)
                self.FXListCtrl.SetItemState(item+1,
                    wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED,
                    wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED)

                self.FXparameters[item+1][1] = "%d" % (image.GetWidth(),)
                self.FXparameters[item+1][2] = "%d" % (image.GetHeight(),)
                
                imageData = image.GetData()
                self.FXparameters[item+1][3] = imageData
                
                self.SetCurrentFX()

        finally:
            dlg.Destroy()
        
        event.Skip()

    def OnBaseTexturesSubMenuItems_sinusMenu(self, event):
        self.AddEffect("Sinus")
        event.Skip()

    def OnDistortionsSubMenuItems_flipMenu(self, event):
        self.AddEffect("Flip")
        event.Skip()

    def OnDistortionsSubMenuItems_glassMenu(self, event):
        self.AddEffect("Glass")
        event.Skip()

    def OnDistortionsSubMenuItems_moveMenu(self, event):
        self.AddEffect("Move")
        event.Skip()

    def OnDistortionsSubMenuItems_pixellateMenu(self, event):
        self.AddEffect("Pixellate")
        event.Skip()

    def OnDistortionsSubMenuItems_randomizeMenu(self, event):
        self.AddEffect("Randomize")
        event.Skip()

    def OnDistortionsSubMenuItems_rotateMenu(self, event):
        self.AddEffect("Rotate")
        event.Skip()

    def OnDistortionsSubMenuItems_scaleMenu(self, event):
        self.AddEffect("Scale")
        event.Skip()

    def OnDistortionsSubMenuItems_sphere_mappingMenu(self, event):
        self.AddEffect("Sphere mapping")
        event.Skip()

    def OnDistortionsSubMenuItems_tileMenu(self, event):
        self.AddEffect("Tile")
        event.Skip()

    def OnDistortionsSubMenuItems_twirlMenu(self, event):
        self.AddEffect("Twirl")
        event.Skip()

    def OnColorsSubMenuItems_brightnessMenu(self, event):
        self.AddEffect("Brightness")
        event.Skip()

    def OnColorsSubMenuItems_bumpMenu(self, event):
        self.AddEffect("Bump")
        event.Skip()

    def OnColorsSubMenuItems_bump_moreMenu(self, event):
        self.AddEffect("Bump more")
        event.Skip()

    def OnColorsSubMenuItems_contrastMenu(self, event):
        self.AddEffect("Contrast")
        event.Skip()

    def OnColorsSubMenuItems_edge_detectMenu(self, event):
        self.AddEffect("Edge detect")
        event.Skip()

    def OnColorsSubMenuItems_embossMenu(self, event):
        self.AddEffect("Emboss")
        event.Skip()

    def OnColorsSubMenuItems_grayscaleMenu(self, event):
        self.AddEffect("Grayscale")
        event.Skip()

    def OnColorsSubMenuItems_inverseMenu(self, event):
        self.AddEffect("Inverse")
        event.Skip()

    def OnColorsSubMenuItems_posterizeMenu(self, event):
        self.AddEffect("Posterize")
        event.Skip()

    def OnColorsSubMenuItems_sharpenMenu(self, event):
        self.AddEffect("Sharpen")
        event.Skip()

    def OnColorsSubMenuItems_thresholdMenu(self, event):
        self.AddEffect("Threshold")
        event.Skip()

    def OnBlursSubMenuItems_fast_blurMenu(self, event):
        self.AddEffect("Fast blur")
        event.Skip()

    def OnBlursSubMenuItems_fast_horizontal_blurMenu(self, event):
        self.AddEffect("Fast horizontal blur")
        event.Skip()

    def OnBlursSubMenuItems_fast_vertical_blurMenu(self, event):
        self.AddEffect("Fast vertical blur")
        event.Skip()

    def OnBlursSubMenuItems_gaussian_blurMenu(self, event):
        self.AddEffect("Gaussian blur")
        event.Skip()

    def OnBlursSubMenuItems_gaussian_horizontal_blurMenu(self, event):
        self.AddEffect("Gaussian horizontal blur")
        event.Skip()

    def OnBlursSubMenuItems_gaussian_vertical_blurMenu(self, event):
        self.AddEffect("Gaussian vertical blur")
        event.Skip()

    def OnBlursSubMenuItems_line_blurMenu(self, event):
        self.AddEffect("Line blur")
        event.Skip()

    def OnLayersSubMenuItems_addMenu(self, event):
        self.AddEffect("Add")
        event.Skip()

    def OnLayersSubMenuItems_copyMenu(self, event):
        self.AddEffect("Copy")
        event.Skip()

    def OnLayersSubMenuItems_directional_blurMenu(self, event):
        self.AddEffect("Directional blur")
        event.Skip()

    def OnLayersSubMenuItems_environmentMenu(self, event):
        self.AddEffect("Environment")
        event.Skip()

    def OnLayersSubMenuItems_mixMenu(self, event):
        self.AddEffect("Mix")
        event.Skip()

    def OnLayersSubMenuItems_mulMenu(self, event):
        self.AddEffect("Mul")
        event.Skip()

    def OnLayersSubMenuItems_random_dumpMenu(self, event):
        self.AddEffect("Random dump")
        event.Skip()

    def OnLayersSubMenuItems_shadeMenu(self, event):
        self.AddEffect("Shade")
        event.Skip()

    def OnLayersSubMenuItems_subMenu(self, event):
        self.AddEffect("Sub")
        event.Skip()

    def OnLayersSubMenuItems_xorMenu(self, event):
        self.AddEffect("Xor")
        event.Skip()

    def OnCombosSubMenuItems_texture_curveMenu(self, event):
        self.AddEffect("Texture curve")
        event.Skip()

    def Save(self, fileName):
        #Pickle texture
        f = open(fileName + ".txr", "wb")
        
        #Pickle number of FX
        pickle.dump(self.FXListCtrl.GetItemCount(), f)

        #Pickle every FX name
        for i in range(0, self.FXListCtrl.GetItemCount()):
            pickle.dump(self.FXListCtrl.GetItemText(i), f)

        #Pickle FX parameters
        pickle.dump(self.FXparameters, f)

        f.close()

    def Load(self, fileName):
        #Unpickle texture
        f = open(fileName, "rb")

        #Unpickle number of FX
        numberOfFX = pickle.load(f)

        #Unpickle every FX name
        for i in range(0, numberOfFX):
            self.FXListCtrl.InsertStringItem(i, pickle.load(f))

        #Unpickle FX parameters
        self.FXparameters = pickle.load(f)
        
        #Select first FX
        if self.FXListCtrl.GetItemCount() > 0 :
            self.FXListCtrl.SetItemState(0,
                wxLIST_STATE_SELECTED|wxLIST_STATE_FOCUSED,
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

            #Base textures
            if FXName == "Checker":
                gradient = self.FXparameters[i][3]
                size += len(gradient)+1
                size += 1
            elif FXName == "Curve":
                curve = self.FXparameters[i][3]
                size += len(curve)+1
                size += 1
            elif FXName == "Fractal":
                gradient = self.FXparameters[i][3]
                size += len(gradient)+1
                size += 3
            elif FXName == "Glow":
                gradient = self.FXparameters[i][3]
                size += len(gradient)+1
                size += 2
            elif FXName == "Noise":
                gradient = self.FXparameters[i][3]
                size += len(gradient)+1
                size += 2
            elif FXName == "Picture":
                picture = self.FXparameters[i][3]
                size += len(picture)
                size += 1
            elif FXName == "Sinus":
                gradient = self.FXparameters[i][3]
                size += len(gradient)+1
                size += 7

            #Distortions
            elif FXName == "Flip":
                size += 1
            elif FXName == "Glass":
                size += 8
            elif FXName == "Move":
                size += 2
            elif FXName == "Pixellate":
                size += 2
            elif FXName == "Randomize":
                size += 3
            elif FXName == "Rotate":
                size += 2
            elif FXName == "Scale":
                size += 1
            elif FXName == "Sphere mapping":
                size += 1
            elif FXName == "Tile":
                size += 3
            elif FXName == "Twirl":
                size += 2

            #Colors
            elif FXName == "Brightness":
                size += 2
            elif FXName == "Bump":
                size += 1
            elif FXName == "Bump more":
                size += 1
            elif FXName == "Contrast":
                size += 2
            elif FXName == "Edge detect":
                size += 1
            elif FXName == "Emboss":
                size += 1
            elif FXName == "Grayscale":
                size += 1
            elif FXName == "Inverse":
                size += 1
            elif FXName == "Posterize":
                size += 2
            elif FXName == "Sharpen":
                size += 2
            elif FXName == "Threshold":
                size += 2

            #Blurs
            elif FXName == "Fast blur":
                size += 2
            elif FXName == "Fast horizontal blur":
                size += 2
            elif FXName == "Fast vertical blur":
                size += 2
            elif FXName == "Gaussian blur":
                size += 2
            elif FXName == "Gaussian horizontal blur":
                size += 2
            elif FXName == "Gaussian vertical blur":
                size += 2
            elif FXName == "Line blur":
                size += 3

            #Layers
            elif FXName == "Add":
                size += 1
            elif FXName == "Copy":
                size += 1
            elif FXName == "Directional blur":
                size += 2
            elif FXName == "Environment":
                size += 2
            elif FXName == "Mix":
                size += 2
            elif FXName == "Mul":
                size += 1
            elif FXName == "Random dump":
                size += 3
            elif FXName == "Shade":
                size += 1
            elif FXName == "Sub":
                size += 1
            elif FXName == "Xor":
                size += 1
                
            #Combos
            elif FXName == "Texture curve":
                curve = self.FXparameters[i][3]
                size += len(curve)+1
                size += 3

        return size

    def SaveH(self, f, componentName):
        f.write("\t\t//Texture name\n")
        f.write("\t\t")
        for i in componentName:
            f.write("'%c'," % (i,))
        f.write("0,\n\n")

        f.write("\t\t//Texture size (24 network ordered bits)\n")
        textureSize = self.Size(componentName)
        f.write("\t\t%d, %d, %d\n\n" %
            (textureSize>>16, (textureSize>>8) & 0xFF, textureSize & 0xFF,))
        
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

            #Base textures
            if FXName == "Checker":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                
                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

                f.write("\t\t//Gradient\n")
                f.write("\t\t")
                for i in gradient:
                    f.write("'%c'," % (i,))
                f.write("0,\n\n")

            elif FXName == "Curve":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                curve = self.FXparameters[i][3]
                
                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

                f.write("\t\t//Curve\n")
                f.write("\t\t")
                for i in curve:
                    f.write("'%c'," % (i,))
                f.write("0,\n\n")

            elif FXName == "Fractal":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                noise = int(self.FXparameters[i][4])
                seed = int(self.FXparameters[i][5])
                
                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

                f.write("\t\t//Gradient\n")
                f.write("\t\t")
                for i in gradient:
                    f.write("'%c'," % (i,))
                f.write("0,\n")

                f.write("\t\t//Noise\n")
                f.write("\t\t%d,\n" % (noise,))

                f.write("\t\t//Seed\n")
                f.write("\t\t%d,\n\n" % (seed,))

            elif FXName == "Glow":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                radius = int(self.FXparameters[i][4])
                
                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

                f.write("\t\t//Gradient\n")
                f.write("\t\t")
                for i in gradient:
                    f.write("'%c'," % (i,))
                f.write("0,\n")

                f.write("\t\t//Radius\n")
                f.write("\t\t%d,\n\n" % (radius,))

            elif FXName == "Noise":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                seed = int(self.FXparameters[i][4])
                
                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

                f.write("\t\t//Gradient\n")
                f.write("\t\t")
                for i in gradient:
                    f.write("'%c'," % (i,))
                f.write("0,\n")

                f.write("\t\t//Seed\n")
                f.write("\t\t%d,\n\n" % (seed,))

            elif FXName == "Picture":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                data = self.FXparameters[i][3]
                
                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

                f.write("\t\t//Data\n")
                f.write("\t\t")
                count = 0
                for i in data:
                    f.write("'%c'," % (i,))
                    count += 1
                    if (count%16 == 15):
                        f.write("\n")

            elif FXName == "Sinus":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                turbX1 = int(self.FXparameters[i][4])
                turbX2 = int(self.FXparameters[i][5])
                turbY1 = int(self.FXparameters[i][6])
                turbY2 = int(self.FXparameters[i][7])
                phase1 = int(self.FXparameters[i][8])
                phase2 = int(self.FXparameters[i][9])
                
                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

                f.write("\t\t//Gradient\n")
                f.write("\t\t")
                for i in gradient:
                    f.write("'%c'," % (i,))
                f.write("0,\n")

                f.write("\t\t//Turbulence\n")
                f.write("\t\t%d, %d, %d, %d,\n" % (turbX1,turbX2,turbY1,turbY2,))

                f.write("\t\t//Phase\n")
                f.write("\t\t%d, %d,\n" % (phase1,phase2,))

            #Distortions
            elif FXName == "Flip":
                destination = layerChoices.index(self.FXparameters[i][0])
                horizontal = (self.FXparameters[i][1] == "Yes")
                vertical = (self.FXparameters[i][2] == "Yes")

                f.write("\t\t//Destination layer (2 bits) + Horizontal (1 bit) + Vertical (1 bit)\n")
                f.write("\t\t%d,\n" % (destination*64 + horizontal*32 + vertical*16,))

            elif FXName == "Glass":
                destination = layerChoices.index(self.FXparameters[i][0])
                turbX1 = int(self.FXparameters[i][1])
                turbX2 = int(self.FXparameters[i][2])
                turbY1 = int(self.FXparameters[i][3])
                turbY2 = int(self.FXparameters[i][4])
                phase1 = int(self.FXparameters[i][5])
                phase2 = int(self.FXparameters[i][6])
                intensity = int(self.FXparameters[i][7])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Turbulence\n")
                f.write("\t\t%d, %d, %d, %d,\n" % (turbX1,turbX2,turbY1,turbY2,))

                f.write("\t\t//Phase\n")
                f.write("\t\t%d, %d,\n" % (phase1,phase2,))

                f.write("\t\t//Intensity\n")
                f.write("\t\t%d,\n" % (intensity,))

            elif FXName == "Move":
                destination = layerChoices.index(self.FXparameters[i][0])
                direction = directionChoices.index(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])

                f.write("\t\t//Destination layer (2 bits) + Direction (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + direction*8,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Pixellate":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])

                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Randomize":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                seed = int(self.FXparameters[i][2])

                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

                f.write("\t\t//Seed\n")
                f.write("\t\t%d,\n" % (seed,))

            elif FXName == "Rotate":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])

                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Scale":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                
                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

            elif FXName == "Sphere mapping":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

            elif FXName == "Tile":
                destination = layerChoices.index(self.FXparameters[i][0])
                horizontalTile = int(self.FXparameters[i][1])
                verticalTile = int(self.FXparameters[i][2])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Horizontal and vertical tile\n")
                f.write("\t\t%d,%d\n" % (horizontalTile,verticalTile,))

            elif FXName == "Twirl":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            #Colors
            elif FXName == "Brightness":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Bump":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

            elif FXName == "Bump more":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

            elif FXName == "Contrast":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Edge detect":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

            elif FXName == "Emboss":
                destination = layerChoices.index(self.FXparameters[i][0])
                emboss = directionChoices.index(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits) + Emboss (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + emboss*8,))

            elif FXName == "Grayscale":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

            elif FXName == "Inverse":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

            elif FXName == "Posterize":
                destination = layerChoices.index(self.FXparameters[i][0])
                levels = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (levels,))

            elif FXName == "Sharpen":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Threshold":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            #Blurs
            elif FXName == "Fast blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Fast horizontal blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Fast vertical blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Gaussian blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Gaussian horizontal blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Gaussian vertical blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Line blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                orientation = int(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])
                
                f.write("\t\t//Destination layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64,))

                f.write("\t\t//Orientation\n")
                f.write("\t\t%d,\n" % (orientation,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            #Layers
            elif FXName == "Add":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

            elif FXName == "Copy":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

            elif FXName == "Directional blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Environment":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Mix":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

                f.write("\t\t//Value\n")
                f.write("\t\t%d,\n" % (value,))

            elif FXName == "Mul":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

            elif FXName == "Random dump":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                number = int(self.FXparameters[i][2])
                seed = int(self.FXparameters[i][3])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

                f.write("\t\t//Number\n")
                f.write("\t\t%d,\n" % (number,))

                f.write("\t\t//Seed\n")
                f.write("\t\t%d,\n" % (seed,))

            elif FXName == "Shade":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

            elif FXName == "Sub":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

            elif FXName == "Xor":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                f.write("\t\t//Destination layer (2 bits) + Source layer (2 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + source*16,))

            #Combos
            elif FXName == "Texture curve":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                curve = self.FXparameters[i][3]
                texture = layerChoices.index(self.FXparameters[i][4])
                mask = layerChoices.index(self.FXparameters[i][5])
                edgeWidth = int(self.FXparameters[i][6])

                f.write("\t\t//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)\n")
                f.write("\t\t%d,\n" % (destination*64 + width*8 + height,))

                f.write("\t\t//Curve\n")
                f.write("\t\t")
                for i in curve:
                    f.write("'%c'," % (i,))
                f.write("0,\n")

                f.write("\t\t//Texture layer (2 bits) + Mask layer (2 bits)\n")
                f.write("\t\t%d,\n" % (texture*64 + mask*16,))

                f.write("\t\t//Edge width\n")
                f.write("\t\t%d,\n" % (edgeWidth,))

            f.write("\n")

    def GetData(self, componentName):
        # Store texture name
        output = componentName
        output += pack('B', 0)
        
        # Store texture size (24 bits network ordered)
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

            #Base textures
            if FXName == "Checker":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                
                output += pack('B', destination*64 + width*8 + height)
                output += gradient
                output += pack('B', 0)

            elif FXName == "Curve":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                curve = self.FXparameters[i][3]
                
                output += pack('B', destination*64 + width*8 + height)
                output += curve
                output += pack('B', 0)

            elif FXName == "Fractal":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                noise = int(self.FXparameters[i][4])
                seed = int(self.FXparameters[i][5])
                
                output += pack('B', destination*64 + width*8 + height)
                output += gradient
                output += pack('B', 0)
                output += pack('B', noise)
                output += pack('B', seed)

            elif FXName == "Glow":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                radius = int(self.FXparameters[i][4])
                
                output += pack('B', destination*64 + width*8 + height)
                output += gradient
                output += pack('B', 0)
                output += pack('B', radius)

            elif FXName == "Noise":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                seed = int(self.FXparameters[i][4])
                
                output += pack('B', destination*64 + width*8 + height)
                output += gradient
                output += pack('B', 0)
                output += pack('B', seed)

            elif FXName == "Picture":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                data = self.FXparameters[i][3]
                
                output += pack('B', destination*64 + width*8 + height)
                output += data

            elif FXName == "Sinus":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                gradient = self.FXparameters[i][3]
                turbX1 = int(self.FXparameters[i][4])
                turbX2 = int(self.FXparameters[i][5])
                turbY1 = int(self.FXparameters[i][6])
                turbY2 = int(self.FXparameters[i][7])
                phase1 = int(self.FXparameters[i][8])
                phase2 = int(self.FXparameters[i][9])
                
                output += pack('B', destination*64 + width*8 + height)
                output += gradient
                output += pack('B', 0)
                output += pack('BBBB', turbX1, turbX2, turbY1, turbY2)
                output += pack('BB', phase1, phase2)

            #Distortions
            elif FXName == "Flip":
                destination = layerChoices.index(self.FXparameters[i][0])
                horizontal = (self.FXparameters[i][1] == "Yes")
                vertical = (self.FXparameters[i][2] == "Yes")

                output += pack('B', destination*64 + horizontal*32 + vertical*16)

            elif FXName == "Glass":
                destination = layerChoices.index(self.FXparameters[i][0])
                turbX1 = int(self.FXparameters[i][1])
                turbX2 = int(self.FXparameters[i][2])
                turbY1 = int(self.FXparameters[i][3])
                turbY2 = int(self.FXparameters[i][4])
                phase1 = int(self.FXparameters[i][5])
                phase2 = int(self.FXparameters[i][6])
                intensity = int(self.FXparameters[i][7])
                
                output += pack('B', destination*64)
                output += pack('BBBB', turbX1, turbX2, turbY1, turbY2)
                output += pack('BB', phase1, phase2)
                output += pack('B', intensity)

            elif FXName == "Move":
                destination = layerChoices.index(self.FXparameters[i][0])
                direction = directionChoices.index(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])

                output += pack('B', destination*64 + direction*8)
                output += pack('B', value)

            elif FXName == "Pixellate":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])

                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Randomize":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                seed = int(self.FXparameters[i][2])

                output += pack('B', destination*64)
                output += pack('B', value)
                output += pack('B', seed)

            elif FXName == "Rotate":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])

                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Scale":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                
                output += pack('B', destination*64 + width*8 + height)

            elif FXName == "Sphere mapping":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                output += pack('B', destination*64)

            elif FXName == "Tile":
                destination = layerChoices.index(self.FXparameters[i][0])
                horizontalTile = int(self.FXparameters[i][1])
                verticalTile = int(self.FXparameters[i][2])
                
                output += pack('B', destination*64)
                output += pack('B', horizontalTile)
                output += pack('B', verticalTile)

            elif FXName == "Twirl":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            #Colors
            elif FXName == "Brightness":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Bump":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                output += pack('B', destination*64)

            elif FXName == "Bump more":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                output += pack('B', destination*64)

            elif FXName == "Contrast":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Edge detect":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                output += pack('B', destination*64)

            elif FXName == "Emboss":
                destination = layerChoices.index(self.FXparameters[i][0])
                emboss = directionChoices.index(self.FXparameters[i][1])
                
                output += pack('B', destination*64 + emboss*8)

            elif FXName == "Grayscale":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                output += pack('B', destination*64)

            elif FXName == "Inverse":
                destination = layerChoices.index(self.FXparameters[i][0])
                
                output += pack('B', destination*64)

            elif FXName == "Posterize":
                destination = layerChoices.index(self.FXparameters[i][0])
                levels = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', levels)

            elif FXName == "Sharpen":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Threshold":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            #Blurs
            elif FXName == "Fast blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Fast horizontal blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Fast vertical blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Gaussian blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Gaussian horizontal blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Gaussian vertical blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                value = int(self.FXparameters[i][1])
                
                output += pack('B', destination*64)
                output += pack('B', value)

            elif FXName == "Line blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                orientation = int(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])
                
                output += pack('B', destination*64)
                output += pack('B', orientation)
                output += pack('B', value)

            #Layers
            elif FXName == "Add":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                output += pack('B', destination*64 + source*16)

            elif FXName == "Copy":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                output += pack('B', destination*64 + source*16)

            elif FXName == "Directional blur":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])
                
                output += pack('B', destination*64 + source*16)
                output += pack('B', value)

            elif FXName == "Environment":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])
                
                output += pack('B', destination*64 + source*16)
                output += pack('B', value)

            elif FXName == "Mix":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                value = int(self.FXparameters[i][2])
                
                output += pack('B', destination*64 + source*16)
                output += pack('B', value)

            elif FXName == "Mul":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                
                output += pack('B', destination*64 + source*16)

            elif FXName == "Random dump":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])
                number = int(self.FXparameters[i][2])
                seed = int(self.FXparameters[i][3])

                output += pack('B', destination*64 + source*16)
                output += pack('B', number)
                output += pack('B', seed)

            elif FXName == "Shade":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])

                output += pack('B', destination*64 + source*16)

            elif FXName == "Sub":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])

                output += pack('B', destination*64 + source*16)

            elif FXName == "Xor":
                destination = layerChoices.index(self.FXparameters[i][0])
                source = layerChoices.index(self.FXparameters[i][1])

                output += pack('B', destination*64 + source*16)

            #Combos
            elif FXName == "Texture curve":
                destination = layerChoices.index(self.FXparameters[i][0])
                width = sizeChoices.index(self.FXparameters[i][1])
                height = sizeChoices.index(self.FXparameters[i][2])
                curve = self.FXparameters[i][3]
                texture = layerChoices.index(self.FXparameters[i][4])
                mask = layerChoices.index(self.FXparameters[i][5])
                edgeWidth = int(self.FXparameters[i][6])
                
                output += pack('B', destination*64 + width*8 + height)
                output += curve
                output += pack('B', 0)
                output += pack('B', texture*64 + mask*16)
                output += pack('B', edgeWidth)

        return output
