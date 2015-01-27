#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 3,

	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 48

		//Number of FX
		11,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		44,
		//Seed
		1,


		//Active (1 bit) + FX type (7 bits)
		156,
		//Destination layer (2 bits)
		0,
		//Value
		8,

		//Active (1 bit) + FX type (7 bits)
		153,
		//Destination layer (2 bits)
		0,
		//Value
		6,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		162,
		//Destination layer (2 bits)
		0,
		//Orientation
		48,
		//Value
		128,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		152,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		146,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		173,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Curve
		'C','u','r','v','e','0',0,
		//Texture layer (2 bits) + Mask layer (2 bits)
		32,
		//Edge width
		4,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		143, 143, 188,
		0,

		//Color 1: RGB + Position
		0, 0, 0,
		255,


	//Component type
	1,		//Curve

		//Curve name
		'C','u','r','v','e','0',0,

		//Mode (1 bit) + Number of points (7 bits)
		6,

		//Segments per curve
		32,

		//Line width
		1,

		//Visible and endpoint bits (1 point per bit)
		63,
		0,

		//Control points, left tangents and right tangents
		42, 170,
		73, 208,
		11, 132,
		112, 35,
		48, 38,
		176, 32,
		94, 99,
		0, 138,
		196, 60,
		164, 102,
		93, 181,
		235, 23,
		220, 158,
		241, 121,
		199, 195,
		130, 231,
		169, 74,
		91, 74,

};

#pragma pack()
