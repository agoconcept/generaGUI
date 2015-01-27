#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 3,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		35, 142, 35,
		0,

		//Color 1: RGB + Position
		47, 47, 47,
		255,


	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		130,

		//Color 0: RGB + Position
		192, 192, 192,
		0,

		//Color 1: RGB + Position
		0, 0, 0,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 57

		//Number of FX
		8,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		40,
		//Seed
		1,


		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		10,
		//Seed
		1,


		//Active (1 bit) + FX type (7 bits)
		131,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		146,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Radius
		32,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		4,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		64,
		//Value
		8,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		128,
		//Value
		4,

		//Active (1 bit) + FX type (7 bits)
		165,
		//Destination layer (2 bits) + Source layer (2 bits)
		16,
		//Value
		16,

		//Active (1 bit) + FX type (7 bits)
		166,
		//Destination layer (2 bits) + Source layer (2 bits)
		32,
		//Value
		99,

};

#pragma pack()
