#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 4,

	//Component type
	1,		//Curve

		//Curve name
		'C','u','r','v','e','0',0,

		//Mode (1 bit) + Number of points (7 bits)
		8,

		//Segments per curve
		24,

		//Line width
		1,

		//Visible and endpoint bits (1 point per bit)
		255,
		136,

		//Control points, left tangents and right tangents
		101, 214,
		170, 238,
		32, 190,
		68, 125,
		36, 54,
		100, 196,
		153, 49,
		78, 66,
		228, 32,
		203, 134,
		225, 51,
		181, 217,
		118, 207,
		149, 214,
		87, 200,
		108, 157,
		93, 120,
		123, 194,
		162, 96,
		109, 106,
		215, 86,
		178, 167,
		192, 124,
		164, 210,

	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 72

		//Number of FX
		16,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		30,
		//Seed
		1,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		8,

		//Active (1 bit) + FX type (7 bits)
		165,
		//Destination layer (2 bits) + Source layer (2 bits)
		0,
		//Value
		16,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		170,
		//Destination layer (2 bits) + Source layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		10,
		//Seed
		158,


		//Active (1 bit) + FX type (7 bits)
		151,
		//Destination layer (2 bits)
		64,

		//Active (1 bit) + FX type (7 bits)
		165,
		//Destination layer (2 bits) + Source layer (2 bits)
		16,
		//Value
		32,

		//Active (1 bit) + FX type (7 bits)
		164,
		//Destination layer (2 bits) + Source layer (2 bits)
		64,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		64,
		//Value
		6,

		//Active (1 bit) + FX type (7 bits)
		150,
		//Destination layer (2 bits) + Emboss (3 bits)
		112,

		//Active (1 bit) + FX type (7 bits)
		148,
		//Destination layer (2 bits)
		64,
		//Value
		224,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		2,

		//Active (1 bit) + FX type (7 bits)
		168,
		//Destination layer (2 bits) + Source layer (2 bits)
		16,

		//Active (1 bit) + FX type (7 bits)
		173,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		237,
		//Curve
		'C','u','r','v','e','0',0,
		//Texture layer (2 bits) + Mask layer (2 bits)
		32,
		//Edge width
		2,

		//Active (1 bit) + FX type (7 bits)
		170,
		//Destination layer (2 bits) + Source layer (2 bits)
		208,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		131,

		//Color 0: RGB + Position
		47, 47, 79,
		0,

		//Color 1: RGB + Position
		204, 127, 50,
		127,

		//Color 2: RGB + Position
		255, 255, 255,
		255,


	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		128, 128, 128,
		0,

		//Color 1: RGB + Position
		0, 0, 0,
		255,


};

#pragma pack()
