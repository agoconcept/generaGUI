#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 6,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

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
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 18

		//Number of FX
		2,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		4,
		//Seed
		1,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		16,

	//Component type
	3,		//Model

		//Model name
		'M','o','d','e','l','0',0,

		//Model size (24 network ordered bits)
		0, 0, 63

		//Number of FX
		5,

		//Active (1 bit) + FX type (7 bits)
		135,
		//Horizontal tips
		4,
		//Vertical tips
		4,
		//Minimum radius
		0,0,0,64,
		//Maximum radius
		0,0,64,64,
		//Segments
		255,
		//Rings
		255,

		//Active (1 bit) + FX type (7 bits)
		146,
		//Type (2 bits)
		4,
		//Texture
		'T','e','x','t','u','r','e','1',0,


		//Active (1 bit) + FX type (7 bits)
		138,
		//Type (2 bits)
		1,
		//Value
		0,0,64,64,
		//Texture
		'T','e','x','t','u','r','e','0',0,


		//Active (1 bit) + FX type (7 bits)
		142,
		//X
		0,0,192,63,
		//Y
		0,0,128,63,
		//Z
		0,0,192,63,

		//Active (1 bit) + FX type (7 bits)
		145,
		//Texture
		'T','e','x','t','u','r','e','2',0,


	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		131,

		//Color 0: RGB + Position
		255, 0, 0,
		0,

		//Color 1: RGB + Position
		255, 127, 0,
		21,

		//Color 2: RGB + Position
		255, 255, 255,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','1',0,

		//Texture size (24 network ordered bits)
		0, 0, 27

		//Number of FX
		5,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		32,
		//Seed
		30,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		16,

		//Active (1 bit) + FX type (7 bits)
		165,
		//Destination layer (2 bits) + Source layer (2 bits)
		0,
		//Value
		24,

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
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','2',0,

		//Texture size (24 network ordered bits)
		0, 0, 27

		//Number of FX
		4,

		//Active (1 bit) + FX type (7 bits)
		134,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Turbulence
		21, 21, 20, 21,
		//Phase
		103, 158,

		//Active (1 bit) + FX type (7 bits)
		168,
		//Destination layer (2 bits) + Source layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		145,
		//Destination layer (2 bits)
		0,
		//Value
		0,

		//Active (1 bit) + FX type (7 bits)
		145,
		//Destination layer (2 bits)
		0,
		//Value
		96,

};

#pragma pack()
