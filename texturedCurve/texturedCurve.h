#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 4,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		192, 192, 192,
		0,

		//Color 1: RGB + Position
		0, 0, 0,
		255,


	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		204, 50, 50,
		0,

		//Color 1: RGB + Position
		0, 0, 0,
		255,


	//Component type
	1,		//Curve

		//Curve name
		'C','u','r','v','e','0',0,

		//Mode (1 bit) + Number of points (7 bits)
		136,

		//Segments per curve
		24,

		//Line width
		1,

		//Visible and endpoint bits (1 point per bit)
		255,
		32,

		//Control points, left tangents and right tangents
		38, 190,
		52, 126,
		24, 126,
		94, 39,
		32, 42,
		156, 36,
		206, 42,
		172, 136,
		240, 136,
		173, 211,
		209, 191,
		137, 231,
		104, 227,
		114, 232,
		94, 222,
		137, 132,
		88, 197,
		186, 67,
		82, 167,
		120, 181,
		120, 153,
		242, 166,
		243, 146,
		241, 186,

	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 48

		//Number of FX
		6,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		54,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		24,
		//Seed
		63,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		6,

		//Active (1 bit) + FX type (7 bits)
		131,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		246,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Radius
		60,


		//Active (1 bit) + FX type (7 bits)
		145,
		//Destination layer (2 bits)
		192,
		//Value
		64,

		//Active (1 bit) + FX type (7 bits)
		166,
		//Destination layer (2 bits) + Source layer (2 bits)
		48,
		//Value
		128,

		//Active (1 bit) + FX type (7 bits)
		173,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		118,
		//Curve
		'C','u','r','v','e','0',0,
		//Texture layer (2 bits) + Mask layer (2 bits)
		32,
		//Edge width
		8,

};

#pragma pack()
