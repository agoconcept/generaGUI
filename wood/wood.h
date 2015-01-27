#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 5,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		204, 127, 50,
		0,

		//Color 1: RGB + Position
		0, 0, 0,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 35

		//Number of FX
		10,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		33,
		//Seed
		1,


		//Active (1 bit) + FX type (7 bits)
		157,
		//Destination layer (2 bits)
		0,
		//Value
		49,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		147,
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
		146,
		//Destination layer (2 bits)
		0,

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
		146,
		//Destination layer (2 bits)
		0,

	//Component type
	3,		//Model

		//Model name
		'M','o','d','e','l','0',0,

		//Model size (24 network ordered bits)
		0, 0, 35

		//Number of FX
		3,

		//Active (1 bit) + FX type (7 bits)
		135,
		//Horizontal tips
		2,
		//Vertical tips
		4,
		//Minimum radius
		0,0,128,64,
		//Maximum radius
		0,0,64,64,
		//Segments
		128,
		//Rings
		128,

		//Active (1 bit) + FX type (7 bits)
		146,
		//Type (2 bits)
		3,
		//Texture
		'T','e','x','t','u','r','e','0',0,


		//Active (1 bit) + FX type (7 bits)
		145,
		//Texture
		'T','e','x','t','u','r','e','1',0,


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
		0, 0, 0,
		32,

		//Color 2: RGB + Position
		0, 0, 0,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','1',0,

		//Texture size (24 network ordered bits)
		0, 0, 23

		//Number of FX
		4,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		12,
		//Seed
		55,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		4,

		//Active (1 bit) + FX type (7 bits)
		168,
		//Destination layer (2 bits) + Source layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		145,
		//Destination layer (2 bits)
		0,
		//Value
		96,

};

#pragma pack()
