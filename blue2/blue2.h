#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 2,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		130,

		//Color 0: RGB + Position
		35, 35, 142,
		0,

		//Color 1: RGB + Position
		255, 255, 255,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 35

		//Number of FX
		9,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		24,
		//Seed
		1,


		//Active (1 bit) + FX type (7 bits)
		156,
		//Destination layer (2 bits)
		0,
		//Value
		12,

		//Active (1 bit) + FX type (7 bits)
		165,
		//Destination layer (2 bits) + Source layer (2 bits)
		0,
		//Value
		64,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		164,
		//Destination layer (2 bits) + Source layer (2 bits)
		64,

		//Active (1 bit) + FX type (7 bits)
		150,
		//Destination layer (2 bits) + Emboss (3 bits)
		72,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		64,
		//Value
		4,

		//Active (1 bit) + FX type (7 bits)
		148,
		//Destination layer (2 bits)
		64,
		//Value
		255,

		//Active (1 bit) + FX type (7 bits)
		170,
		//Destination layer (2 bits) + Source layer (2 bits)
		16,

};

#pragma pack()
