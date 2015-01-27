# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _genera

def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


NULL = _genera.NULL
PI = _genera.PI
SQRT2 = _genera.SQRT2
DELTA = _genera.DELTA
GRADIENT_ID = _genera.GRADIENT_ID
CURVE_ID = _genera.CURVE_ID
TEXTURE_ID = _genera.TEXTURE_ID
MODEL_ID = _genera.MODEL_ID
PARAMETER_ID = _genera.PARAMETER_ID
SCENE_ID = _genera.SCENE_ID
UNKNOWN_ID = _genera.UNKNOWN_ID
class Component(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Component, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Component, name)
    def __repr__(self):
        return "<C Component instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Component, 'this', _genera.new_Component(*args))
        _swig_setattr(self, Component, 'thisown', 1)
    def __del__(self, destroy=_genera.delete_Component):
        try:
            if self.thisown: destroy(self)
        except: pass
    def generate(*args): return _genera.Component_generate(*args)
    def loadData(*args): return _genera.Component_loadData(*args)
    def getName(*args): return _genera.Component_getName(*args)
    def setName(*args): return _genera.Component_setName(*args)
    def getGenerated(*args): return _genera.Component_getGenerated(*args)
    def setType(*args): return _genera.Component_setType(*args)
    def getType(*args): return _genera.Component_getType(*args)
    def nameIs(*args): return _genera.Component_nameIs(*args)
    def readString(*args): return _genera.Component_readString(*args)

class ComponentPtr(Component):
    def __init__(self, this):
        _swig_setattr(self, Component, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Component, 'thisown', 0)
        _swig_setattr(self, Component,self.__class__,Component)
_genera.Component_swigregister(ComponentPtr)

class Gradient(Component):
    __swig_setmethods__ = {}
    for _s in [Component]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Gradient, name, value)
    __swig_getmethods__ = {}
    for _s in [Component]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Gradient, name)
    def __repr__(self):
        return "<C Gradient instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Gradient, 'this', _genera.new_Gradient(*args))
        _swig_setattr(self, Gradient, 'thisown', 1)
    def __del__(self, destroy=_genera.delete_Gradient):
        try:
            if self.thisown: destroy(self)
        except: pass
    def loadData(*args): return _genera.Gradient_loadData(*args)
    def getColorAt(*args): return _genera.Gradient_getColorAt(*args)

class GradientPtr(Gradient):
    def __init__(self, this):
        _swig_setattr(self, Gradient, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Gradient, 'thisown', 0)
        _swig_setattr(self, Gradient,self.__class__,Gradient)
_genera.Gradient_swigregister(GradientPtr)

class Curve(Component):
    __swig_setmethods__ = {}
    for _s in [Component]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Curve, name, value)
    __swig_getmethods__ = {}
    for _s in [Component]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Curve, name)
    def __repr__(self):
        return "<C Curve instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Curve, 'this', _genera.new_Curve(*args))
        _swig_setattr(self, Curve, 'thisown', 1)
    def __del__(self, destroy=_genera.delete_Curve):
        try:
            if self.thisown: destroy(self)
        except: pass
    def loadData(*args): return _genera.Curve_loadData(*args)
    def getFilled(*args): return _genera.Curve_getFilled(*args)
    def getNumberOfPoints(*args): return _genera.Curve_getNumberOfPoints(*args)
    def getSegmentsPerCurve(*args): return _genera.Curve_getSegmentsPerCurve(*args)
    def getLineWidth(*args): return _genera.Curve_getLineWidth(*args)
    def getVisible(*args): return _genera.Curve_getVisible(*args)
    def getEndPoint(*args): return _genera.Curve_getEndPoint(*args)
    def getControlPoint(*args): return _genera.Curve_getControlPoint(*args)
    def getLeftTangent(*args): return _genera.Curve_getLeftTangent(*args)
    def getRightTangent(*args): return _genera.Curve_getRightTangent(*args)
    def generate(*args): return _genera.Curve_generate(*args)

class CurvePtr(Curve):
    def __init__(self, this):
        _swig_setattr(self, Curve, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Curve, 'thisown', 0)
        _swig_setattr(self, Curve,self.__class__,Curve)
_genera.Curve_swigregister(CurvePtr)

TEXTURE_FX_ON = _genera.TEXTURE_FX_ON
TEXTURE_FX_TYPE = _genera.TEXTURE_FX_TYPE
DESTINATION_LAYER = _genera.DESTINATION_LAYER
SOURCE_LAYER = _genera.SOURCE_LAYER
WIDTH = _genera.WIDTH
HEIGHT = _genera.HEIGHT
SCALE_X = _genera.SCALE_X
SCALE_Y = _genera.SCALE_Y
HORIZONTAL = _genera.HORIZONTAL
VERTICAL = _genera.VERTICAL
DIRECTION = _genera.DIRECTION
EMBOSS_VAL = _genera.EMBOSS_VAL
POSTERIZE_VAL = _genera.POSTERIZE_VAL
TEXTURE_LAYER = _genera.TEXTURE_LAYER
MASK_LAYER = _genera.MASK_LAYER
CHECKER = _genera.CHECKER
CURVE = _genera.CURVE
FRACTAL = _genera.FRACTAL
GLOW = _genera.GLOW
NOISE = _genera.NOISE
PICTURE = _genera.PICTURE
SINUS = _genera.SINUS
FLIP = _genera.FLIP
GLASS = _genera.GLASS
MOVE = _genera.MOVE
PIXELLATE = _genera.PIXELLATE
RANDOMIZE = _genera.RANDOMIZE
ROTATE = _genera.ROTATE
SCALE = _genera.SCALE
SPHERE_MAPPING = _genera.SPHERE_MAPPING
TILE = _genera.TILE
TWIRL = _genera.TWIRL
BRIGHTNESS = _genera.BRIGHTNESS
BUMP = _genera.BUMP
BUMP_MORE = _genera.BUMP_MORE
CONTRAST = _genera.CONTRAST
EDGE_DETECT = _genera.EDGE_DETECT
EMBOSS = _genera.EMBOSS
GRAYSCALE = _genera.GRAYSCALE
INVERSE = _genera.INVERSE
POSTERIZE = _genera.POSTERIZE
SHARPEN = _genera.SHARPEN
THRESHOLD = _genera.THRESHOLD
FAST_BLUR = _genera.FAST_BLUR
FAST_HORIZONTAL_BLUR = _genera.FAST_HORIZONTAL_BLUR
FAST_VERTICAL_BLUR = _genera.FAST_VERTICAL_BLUR
GAUSSIAN_BLUR = _genera.GAUSSIAN_BLUR
GAUSSIAN_HORIZONTAL_BLUR = _genera.GAUSSIAN_HORIZONTAL_BLUR
GAUSSIAN_VERTICAL_BLUR = _genera.GAUSSIAN_VERTICAL_BLUR
LINE_BLUR = _genera.LINE_BLUR
ADD = _genera.ADD
COPY = _genera.COPY
DIRECTIONAL_BLUR = _genera.DIRECTIONAL_BLUR
ENVIRONMENT = _genera.ENVIRONMENT
MIX = _genera.MIX
MUL = _genera.MUL
RANDOM_DUMP = _genera.RANDOM_DUMP
SHADE = _genera.SHADE
SUB = _genera.SUB
XOR = _genera.XOR
TEXTURE_CURVE = _genera.TEXTURE_CURVE
class Texture(Component):
    __swig_setmethods__ = {}
    for _s in [Component]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Texture, name, value)
    __swig_getmethods__ = {}
    for _s in [Component]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Texture, name)
    def __repr__(self):
        return "<C Texture instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Texture, 'this', _genera.new_Texture(*args))
        _swig_setattr(self, Texture, 'thisown', 1)
    def __del__(self, destroy=_genera.delete_Texture):
        try:
            if self.thisown: destroy(self)
        except: pass
    def setGenerator(*args): return _genera.Texture_setGenerator(*args)
    def loadData(*args): return _genera.Texture_loadData(*args)
    def generate(*args): return _genera.Texture_generate(*args)
    def getLayer(*args): return _genera.Texture_getLayer(*args)
    def getTexture(*args): return _genera.Texture_getTexture(*args)
    def checker(*args): return _genera.Texture_checker(*args)
    def curve(*args): return _genera.Texture_curve(*args)
    def fractal(*args): return _genera.Texture_fractal(*args)
    def glow(*args): return _genera.Texture_glow(*args)
    def noise(*args): return _genera.Texture_noise(*args)
    def picture(*args): return _genera.Texture_picture(*args)
    def sinus(*args): return _genera.Texture_sinus(*args)
    def flip(*args): return _genera.Texture_flip(*args)
    def glass(*args): return _genera.Texture_glass(*args)
    def move(*args): return _genera.Texture_move(*args)
    def pixellate(*args): return _genera.Texture_pixellate(*args)
    def randomize(*args): return _genera.Texture_randomize(*args)
    def rotate(*args): return _genera.Texture_rotate(*args)
    def scale(*args): return _genera.Texture_scale(*args)
    def sphereMapping(*args): return _genera.Texture_sphereMapping(*args)
    def tile(*args): return _genera.Texture_tile(*args)
    def twirl(*args): return _genera.Texture_twirl(*args)
    def brightness(*args): return _genera.Texture_brightness(*args)
    def bump(*args): return _genera.Texture_bump(*args)
    def bumpMore(*args): return _genera.Texture_bumpMore(*args)
    def contrast(*args): return _genera.Texture_contrast(*args)
    def edgeDetect(*args): return _genera.Texture_edgeDetect(*args)
    def emboss(*args): return _genera.Texture_emboss(*args)
    def grayscale(*args): return _genera.Texture_grayscale(*args)
    def inverse(*args): return _genera.Texture_inverse(*args)
    def posterize(*args): return _genera.Texture_posterize(*args)
    def sharpen(*args): return _genera.Texture_sharpen(*args)
    def threshold(*args): return _genera.Texture_threshold(*args)
    def fastBlur(*args): return _genera.Texture_fastBlur(*args)
    def fastHorizontalBlur(*args): return _genera.Texture_fastHorizontalBlur(*args)
    def fastVerticalBlur(*args): return _genera.Texture_fastVerticalBlur(*args)
    def gaussianBlur(*args): return _genera.Texture_gaussianBlur(*args)
    def gaussianHorizontalBlur(*args): return _genera.Texture_gaussianHorizontalBlur(*args)
    def gaussianVerticalBlur(*args): return _genera.Texture_gaussianVerticalBlur(*args)
    def lineBlur(*args): return _genera.Texture_lineBlur(*args)
    def add(*args): return _genera.Texture_add(*args)
    def copy(*args): return _genera.Texture_copy(*args)
    def directionalBlur(*args): return _genera.Texture_directionalBlur(*args)
    def environment(*args): return _genera.Texture_environment(*args)
    def mix(*args): return _genera.Texture_mix(*args)
    def mul(*args): return _genera.Texture_mul(*args)
    def randomDump(*args): return _genera.Texture_randomDump(*args)
    def shade(*args): return _genera.Texture_shade(*args)
    def sub(*args): return _genera.Texture_sub(*args)
    def xclor(*args): return _genera.Texture_xclor(*args)
    def textureCurve(*args): return _genera.Texture_textureCurve(*args)

class TexturePtr(Texture):
    def __init__(self, this):
        _swig_setattr(self, Texture, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Texture, 'thisown', 0)
        _swig_setattr(self, Texture,self.__class__,Texture)
_genera.Texture_swigregister(TexturePtr)

MODEL_FX_ON = _genera.MODEL_FX_ON
MODEL_FX_TYPE = _genera.MODEL_FX_TYPE
CUBE = _genera.CUBE
CYLINDER = _genera.CYLINDER
EXTRUDE_CURVE = _genera.EXTRUDE_CURVE
HEIGHT_FIELD = _genera.HEIGHT_FIELD
METABALL = _genera.METABALL
OCTAHEDRON = _genera.OCTAHEDRON
SPHERE = _genera.SPHERE
STAR = _genera.STAR
SWEEP_CURVE = _genera.SWEEP_CURVE
TORUS = _genera.TORUS
HEIGHT_MAP = _genera.HEIGHT_MAP
MOVE_OBJECT = _genera.MOVE_OBJECT
NOISE_OBJECT = _genera.NOISE_OBJECT
REFINE = _genera.REFINE
ROTATE_OBJECT = _genera.ROTATE_OBJECT
SCALE_OBJECT = _genera.SCALE_OBJECT
SPHERIZE = _genera.SPHERIZE
TAPER = _genera.TAPER
TESSELLATE = _genera.TESSELLATE
TWIST_OBJECT = _genera.TWIST_OBJECT
ENVIRONMENT_MAP = _genera.ENVIRONMENT_MAP
TEXTURE_MAP = _genera.TEXTURE_MAP
class Texel(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Texel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Texel, name)
    def __repr__(self):
        return "<C Texel instance at %s>" % (self.this,)
    __swig_setmethods__["u"] = _genera.Texel_u_set
    __swig_getmethods__["u"] = _genera.Texel_u_get
    if _newclass:u = property(_genera.Texel_u_get, _genera.Texel_u_set)
    __swig_setmethods__["v"] = _genera.Texel_v_set
    __swig_getmethods__["v"] = _genera.Texel_v_get
    if _newclass:v = property(_genera.Texel_v_get, _genera.Texel_v_set)
    def __init__(self, *args):
        _swig_setattr(self, Texel, 'this', _genera.new_Texel(*args))
        _swig_setattr(self, Texel, 'thisown', 1)
    def __del__(self, destroy=_genera.delete_Texel):
        try:
            if self.thisown: destroy(self)
        except: pass

class TexelPtr(Texel):
    def __init__(self, this):
        _swig_setattr(self, Texel, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Texel, 'thisown', 0)
        _swig_setattr(self, Texel,self.__class__,Texel)
_genera.Texel_swigregister(TexelPtr)

class Face(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Face, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Face, name)
    def __repr__(self):
        return "<C Face instance at %s>" % (self.this,)
    __swig_setmethods__["vertex1"] = _genera.Face_vertex1_set
    __swig_getmethods__["vertex1"] = _genera.Face_vertex1_get
    if _newclass:vertex1 = property(_genera.Face_vertex1_get, _genera.Face_vertex1_set)
    __swig_setmethods__["vertex2"] = _genera.Face_vertex2_set
    __swig_getmethods__["vertex2"] = _genera.Face_vertex2_get
    if _newclass:vertex2 = property(_genera.Face_vertex2_get, _genera.Face_vertex2_set)
    __swig_setmethods__["vertex3"] = _genera.Face_vertex3_set
    __swig_getmethods__["vertex3"] = _genera.Face_vertex3_get
    if _newclass:vertex3 = property(_genera.Face_vertex3_get, _genera.Face_vertex3_set)
    __swig_setmethods__["twoSided"] = _genera.Face_twoSided_set
    __swig_getmethods__["twoSided"] = _genera.Face_twoSided_get
    if _newclass:twoSided = property(_genera.Face_twoSided_get, _genera.Face_twoSided_set)
    def __init__(self, *args):
        _swig_setattr(self, Face, 'this', _genera.new_Face(*args))
        _swig_setattr(self, Face, 'thisown', 1)
    def __del__(self, destroy=_genera.delete_Face):
        try:
            if self.thisown: destroy(self)
        except: pass

class FacePtr(Face):
    def __init__(self, this):
        _swig_setattr(self, Face, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Face, 'thisown', 0)
        _swig_setattr(self, Face,self.__class__,Face)
_genera.Face_swigregister(FacePtr)

class Model(Component):
    __swig_setmethods__ = {}
    for _s in [Component]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Model, name, value)
    __swig_getmethods__ = {}
    for _s in [Component]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Model, name)
    def __repr__(self):
        return "<C Model instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Model, 'this', _genera.new_Model(*args))
        _swig_setattr(self, Model, 'thisown', 1)
    def __del__(self, destroy=_genera.delete_Model):
        try:
            if self.thisown: destroy(self)
        except: pass
    def setGenerator(*args): return _genera.Model_setGenerator(*args)
    def loadData(*args): return _genera.Model_loadData(*args)
    def generate(*args): return _genera.Model_generate(*args)
    def precalculate(*args): return _genera.Model_precalculate(*args)
    def getNumberOfVertices(*args): return _genera.Model_getNumberOfVertices(*args)
    def setNumberOfVertices(*args): return _genera.Model_setNumberOfVertices(*args)
    def getVertex(*args): return _genera.Model_getVertex(*args)
    def setVertex(*args): return _genera.Model_setVertex(*args)
    def getVertexNormal(*args): return _genera.Model_getVertexNormal(*args)
    def setVertexNormal(*args): return _genera.Model_setVertexNormal(*args)
    def getVertexUV(*args): return _genera.Model_getVertexUV(*args)
    def setVertexUV(*args): return _genera.Model_setVertexUV(*args)
    def getMin(*args): return _genera.Model_getMin(*args)
    def getMax(*args): return _genera.Model_getMax(*args)
    def getCenter(*args): return _genera.Model_getCenter(*args)
    def getNumberOfFaces(*args): return _genera.Model_getNumberOfFaces(*args)
    def setNumberOfFaces(*args): return _genera.Model_setNumberOfFaces(*args)
    def getFace(*args): return _genera.Model_getFace(*args)
    def setFace(*args): return _genera.Model_setFace(*args)
    def getFaceNormal(*args): return _genera.Model_getFaceNormal(*args)
    def setFaceNormal(*args): return _genera.Model_setFaceNormal(*args)
    def getTextureMap(*args): return _genera.Model_getTextureMap(*args)
    def setTextureMap(*args): return _genera.Model_setTextureMap(*args)
    def getEnvironmentMap(*args): return _genera.Model_getEnvironmentMap(*args)
    def setEnvironmentMap(*args): return _genera.Model_setEnvironmentMap(*args)
    def getTextureMapped(*args): return _genera.Model_getTextureMapped(*args)
    def setTextureMapped(*args): return _genera.Model_setTextureMapped(*args)
    def getEnvironmentMapped(*args): return _genera.Model_getEnvironmentMapped(*args)
    def setEnvironmentMapped(*args): return _genera.Model_setEnvironmentMapped(*args)
    def cube(*args): return _genera.Model_cube(*args)
    def cylinder(*args): return _genera.Model_cylinder(*args)
    def heightField(*args): return _genera.Model_heightField(*args)
    def octahedron(*args): return _genera.Model_octahedron(*args)
    def sphere(*args): return _genera.Model_sphere(*args)
    def star(*args): return _genera.Model_star(*args)
    def torus(*args): return _genera.Model_torus(*args)
    def heightMap(*args): return _genera.Model_heightMap(*args)
    def moveObject(*args): return _genera.Model_moveObject(*args)
    def noise(*args): return _genera.Model_noise(*args)
    def refine(*args): return _genera.Model_refine(*args)
    def rotateObject(*args): return _genera.Model_rotateObject(*args)
    def scaleObject(*args): return _genera.Model_scaleObject(*args)
    def spherize(*args): return _genera.Model_spherize(*args)
    def taper(*args): return _genera.Model_taper(*args)
    def tessellate(*args): return _genera.Model_tessellate(*args)
    def twistObject(*args): return _genera.Model_twistObject(*args)
    def environment(*args): return _genera.Model_environment(*args)
    def texture(*args): return _genera.Model_texture(*args)
    def draw(*args): return _genera.Model_draw(*args)

class ModelPtr(Model):
    def __init__(self, this):
        _swig_setattr(self, Model, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Model, 'thisown', 0)
        _swig_setattr(self, Model,self.__class__,Model)
_genera.Model_swigregister(ModelPtr)

class Genera(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Genera, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Genera, name)
    def __repr__(self):
        return "<C Genera instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Genera, 'this', _genera.new_Genera(*args))
        _swig_setattr(self, Genera, 'thisown', 1)
    def __del__(self, destroy=_genera.delete_Genera):
        try:
            if self.thisown: destroy(self)
        except: pass
    def load(*args): return _genera.Genera_load(*args)
    def getComponent(*args): return _genera.Genera_getComponent(*args)
    def generateTexture(*args): return _genera.Genera_generateTexture(*args)
    def generateAll(*args): return _genera.Genera_generateAll(*args)
    def loadPy(*args): return _genera.Genera_loadPy(*args)
    def getTextureLayer(*args): return _genera.Genera_getTextureLayer(*args)
    def getTextureLayerWidth(*args): return _genera.Genera_getTextureLayerWidth(*args)
    def getTextureLayerHeight(*args): return _genera.Genera_getTextureLayerHeight(*args)
    def getRenderedModel(*args): return _genera.Genera_getRenderedModel(*args)

class GeneraPtr(Genera):
    def __init__(self, this):
        _swig_setattr(self, Genera, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Genera, 'thisown', 0)
        _swig_setattr(self, Genera,self.__class__,Genera)
_genera.Genera_swigregister(GeneraPtr)


