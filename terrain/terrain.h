#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 3,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		134,

		//Color 0: RGB + Position
		50, 153, 204,
		0,

		//Color 1: RGB + Position
		50, 153, 204,
		16,

		//Color 2: RGB + Position
		204, 127, 50,
		17,

		//Color 3: RGB + Position
		35, 142, 35,
		33,

		//Color 4: RGB + Position
		192, 192, 192,
		245,

		//Color 5: RGB + Position
		255, 255, 255,
		255,


	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 35

		//Number of FX
		4,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		54,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Noise
		10,
		//Seed
		99,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		4,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		118,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		10,
		//Seed
		99,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		64,
		//Value
		4,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		0, 0, 0,
		0,

		//Color 1: RGB + Position
		255, 255, 255,
		255,


};

#pragma pack()
