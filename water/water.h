#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 6,

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
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','2',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		50, 153, 204,
		0,

		//Color 1: RGB + Position
		35, 142, 107,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 47

		//Number of FX
		8,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','2',0,
		//Noise
		8,
		//Seed
		30,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		4,

		//Active (1 bit) + FX type (7 bits)
		131,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Radius
		32,


		//Active (1 bit) + FX type (7 bits)
		145,
		//Destination layer (2 bits)
		64,
		//Value
		24,

		//Active (1 bit) + FX type (7 bits)
		169,
		//Destination layer (2 bits) + Source layer (2 bits)
		144,
		//Number
		28,
		//Seed
		33,

		//Active (1 bit) + FX type (7 bits)
		166,
		//Destination layer (2 bits) + Source layer (2 bits)
		32,
		//Value
		45,

		//Active (1 bit) + FX type (7 bits)
		141,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		54,

		//Active (1 bit) + FX type (7 bits)
		143,
		//Destination layer (2 bits)
		0,
		//Horizontal and vertical tile
		2,2

	//Component type
	3,		//Model

		//Model name
		'M','o','d','e','l','0',0,

		//Model size (24 network ordered bits)
		0, 0, 53

		//Number of FX
		6,

		//Active (1 bit) + FX type (7 bits)
		135,
		//Horizontal tips
		4,
		//Vertical tips
		4,
		//Minimum radius
		0,0,128,64,
		//Maximum radius
		0,0,64,64,
		//Segments
		100,
		//Rings
		100,

		//Active (1 bit) + FX type (7 bits)
		146,
		//Type (2 bits)
		3,
		//Texture
		'T','e','x','t','u','r','e','0',0,


		//Active (1 bit) + FX type (7 bits)
		144,
		//Direction (2 bits)
		1,
		//Value
		0,0,240,66,

		//Active (1 bit) + FX type (7 bits)
		144,
		//Direction (2 bits)
		0,
		//Value
		0,0,180,66,

		//Active (1 bit) + FX type (7 bits)
		144,
		//Direction (2 bits)
		2,
		//Value
		0,0,112,66,

		//Active (1 bit) + FX type (7 bits)
		145,
		//Texture
		'T','e','x','t','u','r','e','1',0,


	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','3',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		255, 255, 255,
		0,

		//Color 1: RGB + Position
		0, 0, 0,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','1',0,

		//Texture size (24 network ordered bits)
		0, 0, 36

		//Number of FX
		4,

		//Active (1 bit) + FX type (7 bits)
		131,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','3',0,
		//Radius
		12,


		//Active (1 bit) + FX type (7 bits)
		134,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Turbulence
		27, 33, 33, 19,
		//Phase
		51, 98,

		//Active (1 bit) + FX type (7 bits)
		168,
		//Destination layer (2 bits) + Source layer (2 bits)
		80,

		//Active (1 bit) + FX type (7 bits)
		163,
		//Destination layer (2 bits) + Source layer (2 bits)
		16,

};

#pragma pack()
