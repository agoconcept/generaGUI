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
		255, 0, 0,
		0,

		//Color 1: RGB + Position
		255, 255, 255,
		255,


	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		130,

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
		0, 0, 21

		//Number of FX
		3,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		16,
		//Seed
		2,


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
		'T','e','x','t','u','r','e','1',0,

		//Texture size (24 network ordered bits)
		0, 0, 40

		//Number of FX
		5,

		//Active (1 bit) + FX type (7 bits)
		131,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Radius
		4,


		//Active (1 bit) + FX type (7 bits)
		134,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Gradient
		'G','r','a','d','i','e','n','t','2',0,
		//Turbulence
		31, 83, 98, 89,
		//Phase
		55, 128,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		64,
		//Value
		8,

		//Active (1 bit) + FX type (7 bits)
		145,
		//Destination layer (2 bits)
		64,
		//Value
		0,

		//Active (1 bit) + FX type (7 bits)
		163,
		//Destination layer (2 bits) + Source layer (2 bits)
		16,

	//Component type
	3,		//Model

		//Model name
		'M','o','d','e','l','0',0,

		//Model size (24 network ordered bits)
		0, 0, 60

		//Number of FX
		6,

		//Active (1 bit) + FX type (7 bits)
		135,
		//Horizontal tips
		4,
		//Vertical tips
		4,
		//Minimum radius
		0,0,64,64,
		//Maximum radius
		0,0,128,64,
		//Segments
		128,
		//Rings
		128,

		//Active (1 bit) + FX type (7 bits)
		148,
		//Type (2 bits)
		4,
		//Texture
		'T','e','x','t','u','r','e','0',0,


		//Active (1 bit) + FX type (7 bits)
		147,
		//Texture
		'T','e','x','t','u','r','e','1',0,


		//Active (1 bit) + FX type (7 bits)
		144,
		//Direction (2 bits)
		0,
		//Value
		0,0,0,63,

		//Active (1 bit) + FX type (7 bits)
		142,
		//X
		0,0,0,63,
		//Y
		0,0,0,63,
		//Z
		0,0,0,63,

		//Active (1 bit) + FX type (7 bits)
		144,
		//Direction (2 bits)
		1,
		//Value
		205,204,204,62,

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
		35, 35, 142,
		255,


};

#pragma pack()
