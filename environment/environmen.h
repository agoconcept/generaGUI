#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 3,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		130,

		//Color 0: RGB + Position
		255, 255, 255,
		0,

		//Color 1: RGB + Position
		47, 47, 79,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 74

		//Number of FX
		15,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		10,
		//Seed
		8,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		4,

		//Active (1 bit) + FX type (7 bits)
		140,
		//Destination layer (2 bits)
		0,
		//Value
		32,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		30,
		//Seed
		4,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		64,
		//Value
		10,

		//Active (1 bit) + FX type (7 bits)
		165,
		//Destination layer (2 bits) + Source layer (2 bits)
		80,
		//Value
		16,

		//Active (1 bit) + FX type (7 bits)
		165,
		//Destination layer (2 bits) + Source layer (2 bits)
		16,
		//Value
		48,

		//Active (1 bit) + FX type (7 bits)
		146,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		146,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		131,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		173,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Radius
		64,


		//Active (1 bit) + FX type (7 bits)
		145,
		//Destination layer (2 bits)
		128,
		//Value
		16,

		//Active (1 bit) + FX type (7 bits)
		38,
		//Destination layer (2 bits) + Source layer (2 bits)
		32,
		//Value
		14,

		//Active (1 bit) + FX type (7 bits)
		166,
		//Destination layer (2 bits) + Source layer (2 bits)
		96,
		//Value
		14,

		//Active (1 bit) + FX type (7 bits)
		164,
		//Destination layer (2 bits) + Source layer (2 bits)
		192,

		//Active (1 bit) + FX type (7 bits)
		170,
		//Destination layer (2 bits) + Source layer (2 bits)
		208,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		131,

		//Color 0: RGB + Position
		255, 255, 255,
		0,

		//Color 1: RGB + Position
		66, 111, 66,
		127,

		//Color 2: RGB + Position
		204, 50, 50,
		255,


};

#pragma pack()
