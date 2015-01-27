#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 3,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		132,

		//Color 0: RGB + Position
		0, 0, 0,
		0,

		//Color 1: RGB + Position
		50, 50, 204,
		63,

		//Color 2: RGB + Position
		35, 142, 35,
		127,

		//Color 3: RGB + Position
		255, 127, 0,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 66

		//Number of FX
		14,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		42,
		//Seed
		93,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		8,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		6,
		//Seed
		36,


		//Active (1 bit) + FX type (7 bits)
		144,
		//Destination layer (2 bits)
		64,
		//Value
		154,

		//Active (1 bit) + FX type (7 bits)
		136,
		//Destination layer (2 bits)
		64,
		//Turbulence
		47, 128, 39, 103,
		//Phase
		73, 198,
		//Intensity
		8,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		64,
		//Value
		8,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		165,
		//Destination layer (2 bits) + Source layer (2 bits)
		16,
		//Value
		64,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		164,
		//Destination layer (2 bits) + Source layer (2 bits)
		192,

		//Active (1 bit) + FX type (7 bits)
		150,
		//Destination layer (2 bits) + Emboss (3 bits)
		200,

		//Active (1 bit) + FX type (7 bits)
		148,
		//Destination layer (2 bits)
		192,
		//Value
		224,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		192,
		//Value
		6,

		//Active (1 bit) + FX type (7 bits)
		170,
		//Destination layer (2 bits) + Source layer (2 bits)
		48,

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
